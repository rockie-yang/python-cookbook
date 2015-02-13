ChainMap is a class to chain multiple maps together to work like one map.
itertools.chain can be used to change other objects together.


chain map is just chain maps together, it will not generate a real map
```python
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = {'a': 2, 'x': 4 }

from collections import ChainMap
chain = ChainMap(a, b, c)
print(chain)


```

the length will remove the duplicate items
so it's not a O(1) constant time operation
```python
print(len(chain))


```

it will return the first value if there are more then one in dictionaries
```python
print(chain['x'])


```

it will raise an exception if there is no item in all dictionaries.
print(chain['b'])

update will only change the first map
```python
chain['x'] = 5
print(chain, c)


```

chain map can be used as scoped object
it will first look up in the closest scope, if not exist it will continue one level up
it will raise exception at least if it does not exist in all level
```python
frame1 = chain.new_child()
frame1['j'] = 6
frame1['j'] = 6
print(frame1)

frame2 = frame1.new_child({'i': 3})
print(frame2)


```

we can merge a chain map by create a new dictionary
```python
merged = dict(frame2)
print(merged)
```
