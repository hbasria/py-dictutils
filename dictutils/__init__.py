from .attr_dict import AttrDict
from .ordered_attr_dict import OrderedAttrDict
from .utils import deep_getattr
from .xml_dict import xml_to_dict


def rget_with_default(object, name, default=None):
    if hasattr(object, name):
        return getattr(object, name, default)
    else:
        return default


def rget(obj, attr, separator='.'):
    return reduce(deep_get_with_default, attr.split(separator), obj)


__all__ = ['rget', 'xml_to_dict', 'AttrDict', 'OrderedAttrDict']
