Priority Queue is a algorithm with excellent push/pop performance O( log(n) ).
It is very useful algorithm for many application, requiring push item and already pop minimum items.
Python heapq is a minimum priority queue implementation.


heapq does not use a collection inside the class.
It's users responsibility to give a list to heapq.
The function heapify will change a list to a heap so that it can be used as heap later on.
The first item of the list will be smallest, while others only have priority queue property but not ordered.
We should ONLY use heapq's function after heapify a list.
Change the list directly will destroy the priority queue property of the list.
```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)


```

after heappop an item, the smallest for the remaining list will still be the first one.
heappop function will keep the priority queue property.
```python
print(heapq.heappop(nums))
print(nums)


```

nlargest and nsmallest will not change the order (heapify) the list
```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(nums)


```

the following solution does NOT work
for trying to work as maximum priority queue
```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq._heapify_max(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))


```

This is a simple solution for a maximum priority queue (or negative priority queue)
We first change the sign of items.
For item returned by heappop, we need change the sign back.
For item we want add to the queue, we first change the sign, then we heappush it.
```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
reversed_nums = [-num for num in nums]
heapq.heapify(reversed_nums)
print(-heapq.heappop(reversed_nums))
num = 38
heapq.heappush(reversed_nums, -num)
print(-heapq.heappop(reversed_nums))


```

We can implement a PriorityQueue very easy.
Although there is an existing queue.PriorityQueue in standard library.
```python
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


```

queue.PriorityQueue is just a wrapper on top of heapq
the first item of parameter for the put is the priority, the second is read data
```python
import queue

pq = queue.PriorityQueue()

pq.put((1, 3))  # 1 is priority, 3 is data
pq.put((2, 4))  # 2 is priority, 4 is data
pq.put((3, 5))  # 2 is priority, 5 is data
print(pq.get(), str(pq))
print(pq.get(), str(pq))
```
