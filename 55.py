from collections import deque

# Function to reverse first k elements of queue
def reverse_k(q, k):
    stack = []

    # Step 1: Push first k elements into stack
    for i in range(k):
        stack.append(q.popleft())

    # Step 2: Pop from stack and add back to queue
    while stack:
        q.append(stack.pop())

    # Step 3: Move remaining elements to back to maintain order
    size = len(q)
    for i in range(size - k):
        q.append(q.popleft())

    return q


# ---- MAIN CODE ----
n, k = map(int, input().split())
arr = list(map(int, input().split()))

q = deque(arr)

result = reverse_k(q, k)

# Print result
for x in result:
    print(x, end=" ")