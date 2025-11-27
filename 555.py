queue = []
front = -1
rear = -1

def is_empty():
    return front == -1 and rear == -1

def enqueue(item):
    global front, rear, queue
    # If queue is empty
    if is_empty():
        front = 0
        rear = 0
        queue.append(item)
    else:
        rear += 1
        queue.append(item)

def dequeue():
    global front, rear, queue
    if is_empty():
        return -1
    item = queue[front]
    front += 1

    # When queue becomes empty after dequeue
    if front > rear:
        front = -1
        rear = -1
        queue = []

    return item

# Enqueue items
n=int(input())
arr = list(map(int, input().split()))[:n]

for i in range(n):
    enqueue(arr[i])

# Dequeue and print items
while not is_empty():
    print(dequeue())