class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():

                    if isinstance(v, dict):
                        self[k] = AttrDict(v)
                    else:
                        self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, item):
        self.__delitem__(item)

    def __setitem__(self, key, value):
        super(AttrDict, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delitem__(self, key):
        super(AttrDict, self).__delitem__(key)
        del self.__dict__[key]
