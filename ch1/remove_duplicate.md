```python
a = [1, 5, 2, 1, 9, 1, 5, 10]
no_duplicate_not_reserve_order = set(a)
print(no_duplicate_not_reserve_order)


def remove_duplicate(items):
    '''remove duplicate and reserve the order'''
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


no_duplicate_reserve_order = remove_duplicate(a)
print(list(no_duplicate_reserve_order))


def remove_duplicate_unhashable(items, key=None):
    '''if the item in items is not hashable, then it can not be added to a set.
    we need a function map from unhashable(e.g. map) to hashable(e.g. tuple)'''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
no_duplicate_unhashable = remove_duplicate_unhashable(a, key=lambda d: (d['x'], d['y']))
print(list(no_duplicate_unhashable))
```
