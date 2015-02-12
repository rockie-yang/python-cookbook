
```python
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
```

 heapify will change a list to a heap
 so that it can be used as heap later on
```python
heapq.heapify(nums)
```

 the order changed, the smallest item will be the first
 but other are not ordered
```python
print(nums)

print(heapq.heappop(nums))
```

 after pop an item, the smallest will still be the first one
```python
print(nums)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
```

 nlargest and nsmallest will not change the order (heapify) the list
```python
print(nums)

```

 the following solution does NOT work
 for trying to work as maximum priority queue
```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq._heapify_max(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))


class PriorityQueue:
    def __init__(self):
        self._queue = []

    # insert priority to -priority can change to max priority queue
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[1]

    def __str__(self):
        return str(self._queue)

pq = PriorityQueue()
pq.push(3, priority=1)
pq.push(4, priority=2)
pq.push(5, priority=3)
print(pq.pop(), pq)

import queue
```

 queue.PriorityQueue is just a wrapper on top of heapq
```python
pq = queue.PriorityQueue()

```

 the first item is the priority, the second is read data
```python
pq.put((1, 3))
pq.put((2, 4))
pq.put((3, 5))
print(pq.get(), str(pq))
print(pq.get(), str(pq))
```
