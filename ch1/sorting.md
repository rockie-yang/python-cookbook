```python
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


from operator import itemgetter

```

 we could sort it only by fname
```python
by_fname = sorted(rows, key=itemgetter('fname'))

```

 we could sort it by fname and lname
```python
by_name = sorted(rows, key=itemgetter('fname', 'lname'))

```

 we could sort it by using lambda
```python
by_name = sorted(rows, key=lambda r: (r['fname'], r['lname']))

```

we could sort it by uid
```python
by_id = sorted(rows, key=itemgetter('uid'))

print(by_fname)
print(by_name)
print(by_id)

```

 itemgetter is an class which provide __call__ function can be applied on a dictionary like object
```python
item1 = rows[0]
print(itemgetter('fname')(item1))


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


from operator import attrgetter
u1 = User(1)
u2 = User(2)
u3 = User(3)

```

 we could get an attribute from an object
```python
print(attrgetter('user_id')(u1))

l = [u3, u1, u2]
by_id = sorted(l, key=attrgetter('user_id'))
print(by_id)
```
