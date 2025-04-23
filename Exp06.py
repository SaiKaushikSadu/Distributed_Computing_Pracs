# Raymond Tree Algo

parent_list = {}
queue_list = []
n = int(input("Enter no. of nodes: "))
root_node = -1

for i in range(0, n):
    queue_list.append(list())
    parent = int(input(f"Enter parents of node {i}: "))
    if parent == -1:
        root_node = i
    parent_list[i] = parent

print(f"Token is with the root node: {root_node}")
req = int(input("Enter the node requesting the token: "))
queue_list[req].append(req)
print(f"Node: {req} adds {req} into it's queue")
for i in range(0, n):
    print(f"Queue for node: {i} is {queue_list[i]}")

curr = req
while True:
    parent = parent_list[curr]
    print(f"Node: {parent} adds {curr}")
    queue_list[parent].append(curr)
    for i in range(0, n):
        print(f"Queue for node: {i} is {queue_list[i]}")
    if parent == root_node:
        print(f"Root Node: {parent} gives token to Node: {req}")
        break
    curr = parent


print("\n--- Token Passing ---")
token_holder = root_node
while token_holder != req:
    if queue_list[token_holder]:
        next_node = queue_list[token_holder].pop(0)
        print(f"Token passed from Node {token_holder} to Node {next_node}")
        token_holder = next_node
    else:
        break

print(f"\n Node {token_holder} enters the critical section.")