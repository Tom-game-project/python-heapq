# Class Based Heapq Algorithm

## Install

```sh
pip install python-heapq
```

## How to use

```python
from python_heapq import priorityq

queue = priorityq([]) # init heapq data

queue.push(2)
queue.push(4)
queue.push(1)
queue.push(7)

while queue.data:
    poped = queue.pop()
    print(poped)

# 1
# 2
# 4
# 7
```

