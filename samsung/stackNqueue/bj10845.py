import queue

n = int(input())
q = queue.Queue()
for _ in range(n):
    a = input().split()
    if a[0] == 'push':
        q.put(int(a[1]))
    elif a[0] == 'pop':
        print(q.get() if not q.empty() else -1)
    elif a[0] == 'front':
        print(q.queue[0] if not q.empty() else -1)
    elif a[0] == 'size':
        print(q.qsize())
    elif a[0] == 'empty':
        print(1 if q.empty() else 0)
    else :
        print(q.queue[-1] if not q.empty() else -1)