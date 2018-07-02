from collections import OrderedDict


class OrderedAttrDict(OrderedDict):
    def __getattr__(self, name):
        """Getting ad.x gets ad['x']"""
        if name.startswith('__') or name.startswith('_OrderedDict__'):
            return super(OrderedAttrDict, self).__getattr__(name)
        else:
            try:
                return self[name]
            except KeyError:
                raise AttributeError(name)

    def __setattr__(self, name, value):
        """Setting ad.x sets ad['x']"""
        if name.startswith('__') or name.startswith('_OrderedDict__'):
            return super(OrderedAttrDict, self).__setattr__(name, value)
        self[name] = value

    def __delattr__(self, name):
        """Deleting ad.x deletes ad['x']"""
        if name.startswith('__') or name.startswith('_OrderedDict__'):
            return super(OrderedAttrDict, self).__delattr__(name)
        del self[name]
