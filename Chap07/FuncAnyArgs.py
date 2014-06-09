def agv(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(agv(1, 2))
print(agv(1, 2, 3, 4))


import html


def make_element(name, value, **attrs):
    keyvals = [' %s=%s' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


print(make_element('item', 'Albatross', size='large', quality=6))
print(make_element('p', '<spam>'))
