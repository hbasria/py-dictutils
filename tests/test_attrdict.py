from dictutils import AttrDict


def test_empty():
    assert AttrDict() == {}

    assert AttrDict(()) == {}

    assert AttrDict({}) == {}


def test_with_items():
    assert AttrDict({'foo': 'bar'}) == {'foo': 'bar'}

    assert AttrDict((('foo', 'bar'),)) == {'foo': 'bar'}

    assert AttrDict(foo='bar') == {'foo': 'bar'}

    assert AttrDict({'alpha': 'bravo'}, foo='bar') == {'foo': 'bar', 'alpha': 'bravo'}


def test_copy():
    """
    Make a dict copy of an AttrDict.
    """
    dict_a = AttrDict({'foo': {'bar': 'baz'}})

    dict_b = dict_a.copy()

    assert dict_a == dict_b

    dict_c = dict_b

    dict_b.foo.lorem = 'ipsum'

    assert dict_b == dict_c


def test_fromkeys():
    """
    make a new sequence from a set of keys.
    """

    # default value
    assert AttrDict.fromkeys(()) == {}

    assert AttrDict.fromkeys({'foo': 'bar', 'baz': 'qux'}) == {'foo': None, 'baz': None}

    assert AttrDict.fromkeys(('foo', 'baz')) == {'foo': None, 'baz': None}

    # custom value
    assert AttrDict.fromkeys((), 0) == {}

    assert AttrDict.fromkeys({'foo': 'bar', 'baz': 'qux'}, 0) == {'foo': 0, 'baz': 0}

    assert AttrDict.fromkeys(('foo', 'baz'), 0) == {'foo': 0, 'baz': 0}


def test_attribute_access():
    """
    Items can be accessed as attributes
    """
    ad = AttrDict()
    ad['x'] = 1

    assert ad.x == 1

    assert 'x' in ad

    ad._y = 2

    assert ad['_y'] == 2


def test_tree():
    tree = AttrDict({'x': {'y': {'z': 1}}})

    assert tree.x.y.z == 1
