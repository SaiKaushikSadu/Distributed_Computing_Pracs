# Distributed Global Averaging method

def to_min(txt):
    time = input(txt)
    h, m = map(int, time.split(":"))
    return h * 60 + m

def to_hhmm(mins):
    return f"{mins // 60:02d}:{mins % 60:02d}"

n = int(input("Enter the number of nodes: "))
nodes = []

for i in range(n):
    t = to_min(f"Enter the time for the node {i+1} in (HH:MM) format : ")
    nodes.append(t)

avg = sum(nodes) // n
print("Average time : ",to_hhmm(avg))

print("Time Differences : ")
for i in range(n):
    diff = avg - nodes[i]
    print(f"Node {i + 1}: {diff} minutes {'ahead' if diff < 0 else 'behind' if diff > 0 else 'no change'}")

print("Synchronized times: ")
for i in range(n):
    nodes[i]=avg
    print(f"Node {i + 1}: {to_hhmm(nodes[i])}")