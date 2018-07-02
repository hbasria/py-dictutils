from .attr import AttrDict
from .ordered_attr import OrderedAttrDict
from .xml import xml_to_dict


def rget_with_default(object, name, default=None):
    if hasattr(object, name):
        return getattr(object, name, default)
    else:
        return default


def rget(obj, attr, separator='.'):
    return reduce(rget_with_default, attr.split(separator), obj)


__all__ = ['rget', 'xml_to_dict', 'AttrDict', 'OrderedAttrDict']
