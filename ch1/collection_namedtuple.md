
 using tuple can represent a record
```python
sub = ('rockie@example.com', '2012-10-01')
```

 but access it need some magic number
```python
print('email=', sub[0], 'joined at', sub[1])

```

 named tuple is a wrapper on top of tuple, it can remove those magic numbers
 it is like a light weighted class
```python
from collections import namedtuple
Subscriber=namedtuple('Subscriber', ['email', 'joined'])
sub1 = Subscriber('rockie@example.com', '2012-10-01')
print(sub1.email)
print('number of attributes', len(sub1))

```

 this can not be executed, because it's read only
 sub1.email = 'rockie@example2.com'

 it can also replace as a read only dictionary more efficiently then normal dictionary
