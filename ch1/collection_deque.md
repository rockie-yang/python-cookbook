
```python
from collections import deque

```

 deque is a LIFO collection, last in first out

 it can specify the max length of the queue, older item will be removed
```python
deque_fix_size = deque(maxlen=3)

for i in range(4):
    deque_fix_size.append(i)

print(deque_fix_size)

```

 and the direction is to the right, it means append with be from right by default
```python
print(deque_fix_size.pop(), deque_fix_size)
print(deque_fix_size.popleft(), deque_fix_size)


```

 if not max length specified, then it is unbounded
```python
deque_variable_size = deque()
for i in range(100):
    deque_variable_size.append(i)

print(len(deque_variable_size))
```
