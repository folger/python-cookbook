from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(5)
print(q)

print('right = ' + str(q.pop()))
print('left = ' + str(q.popleft()))
print(q)
