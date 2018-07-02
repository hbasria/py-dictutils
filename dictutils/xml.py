"""XML as lists and dictionaries, via cElementTree objects.

Based on: http://code.activestate.com/recipes/573463/

Namespace removal cleanups made locally.
"""

from __future__ import absolute_import

import re
from xml.etree import cElementTree

from dictutils import AttrDict

xmlParseExceptionMessagePattern = None


def _f(tag):
    """Remove XML namespaces from text (as introduced by ElementTree)."""
    if tag.startswith('{'):
        # Strip the namespace from the beginning of the tag
        return tag[tag.find('}') + 1:]
    else:
        return tag


def _convert_xml_to_dict_recurse(node, dictclass):
    nodedict = dictclass()

    if len(node.items()) > 0:
        # if we have attributes, set them
        nodedict.update(dict(node.items()))

    for child in node:
        # recursively add the element's children
        newitem = _convert_xml_to_dict_recurse(child, dictclass)
        if nodedict.has_key(_f(child.tag)):
            # found duplicate tag, force a list
            if type(nodedict[_f(child.tag)]) is type([]):
                # append to existing list
                nodedict[_f(child.tag)].append(newitem)
            else:
                # convert to list
                nodedict[_f(child.tag)] = [nodedict[_f(child.tag)], newitem]
        else:
            # only one, directly set the dictionary
            nodedict[_f(child.tag)] = newitem

    if node.text is None:
        text = ''
    else:
        text = node.text.strip()

    if len(nodedict) > 0:
        # if we have a dictionary add the text as a dictionary value
        # (if there is any)
        if len(text) > 0:
            nodedict['_text'] = text
    else:
        # if we don't have child nodes or attributes, just set the text
        nodedict = text
    return nodedict


def xml_to_dict(root, dictclass=AttrDict):
    """Converts an XML string or ElementTree Element to a dictionary."""
    # If a string is passed in, try to parse it

    global xmlParseExceptionMessagePattern

    if type(root) == type(''):
        try:
            root = cElementTree.fromstring(root)
        except Exception as e:

            if xmlParseExceptionMessagePattern is None:
                xmlParseExceptionLineNumber = 'xmlParseExceptionLineNumber'
                xmlParseExceptionColumnNumber = 'xmlParseExceptionColumnNumber'
                xmlParseExceptionMessagePattern = re.compile(
                    '[\S\s]+line\s(?P<' + xmlParseExceptionLineNumber + '>[\d]+),\scolumn\s(?P<' + xmlParseExceptionColumnNumber + '>[\d]+)')

            match = re.match(xmlParseExceptionMessagePattern, e.message)
            line = int(float(match.group(xmlParseExceptionLineNumber)))
            column = int(float(match.group(xmlParseExceptionColumnNumber)))
            if line == 1:
                brokenChar = root[column:column + 1]
                root = root.replace(brokenChar, '')
                root = cElementTree.fromstring(root)
            else:
                raise e

        result = dictclass({_f(root.tag): _convert_xml_to_dict_recurse(root, dictclass)})
        return result
