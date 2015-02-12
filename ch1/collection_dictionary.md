
```python
from collections import defaultdict
d = defaultdict(list)
```

 'a' does not existed in the dictionary yet. it will automatically create an item
```python
d['a'].append(1)

```

 even a simple access, it will create an item
```python
d['b']
print(d)

```

 the following solution could solve the problem for empty items
 but its less elegant
```python
d = {}
d.setdefault('a', []).append(1)
print(d)
d.setdefault('a', []).append(2)
print(d)

```

 default dictionary does not keep the insert order
 OrderDict keeps the order, but need double space
```python
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for k in d:
    print(k, d[k])


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
```

 order by prices
```python
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

sorted_by_key = sorted(zip(prices.keys(), prices.values()))
print(sorted_by_key)


a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
```

 the following operation does not working in python2
 because keys() in python2 returns list, while in python3 return dict_keys
 in python2, it can convert to set to do those set operation.
```python
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.keys() | b.keys())
```
