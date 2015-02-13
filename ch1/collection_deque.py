# deque is a LIFO collection, last in first out.
# It can specify the max length of the queue, older item will be removed.
# If not max length specified, then it is unbounded.


from collections import deque

deque_fix_size = deque(maxlen=3)

for i in range(4):
    deque_fix_size.append(i)

print(deque_fix_size)

print(deque_fix_size.pop(), deque_fix_size)  # pop is from the right
print(deque_fix_size.popleft(), deque_fix_size)


deque_variable_size = deque()
for i in range(100):
    deque_variable_size.append(i)

print(len(deque_variable_size))