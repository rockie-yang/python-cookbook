Besides the default dictionary, there are few other dictionaries are fairly useful.


defaultdict is one of them.
For none existed items, it will create an empty collection (list for the following example).
```python
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)  # 'a' will be automatically created

d['b']  # 'b' will be automatically create even for read access
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
OrderDict keeps the order, but be aware of double space needed
```python
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for k in d:
    print(k, d[k])


```

*zip* function can be used pair key and value together used for other operation.
Like for get minimum, it is most likely that not only the smallest one, but also who is the smallest.
```python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

sorted_by_key = sorted(zip(prices.keys(), prices.values()))
print(sorted_by_key)


```

The keys function will return dict_key in python3 which has set function supported.
In python2, we can manually convert to a set to do those operation.
```python
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
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.keys() | b.keys())
```
