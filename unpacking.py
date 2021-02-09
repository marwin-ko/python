# unpack range object
[*range(1,3)]
# [1,2]

# unpack enumerate
[*enumerate('abc')]
[(0, 'a'), (1, 'b'), (2, 'c')]

# unpack enumerate and turn into dict
dict([*enumerate('abc')])
{0: 'a', 1: 'b', 2: 'c'}


# TODO
# - funct w/ *args
# - funct w/ **kwargs
