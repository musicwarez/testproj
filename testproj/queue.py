from Queue import Queue

queue = Queue()
for i in range(0, 3):
    queue.put(i)

print queue.get_nowait()
print queue.get_nowait()
print queue.get_nowait()