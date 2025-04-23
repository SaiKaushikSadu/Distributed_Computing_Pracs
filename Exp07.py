# Ricart Agrarwal Algorithm

n = int(input("Enter total number of sites/processes: "))

req_set = {}
for i in range(1, n+1):
    lst = []
    for j in range(1, n+1):
        if i != j:
            lst.append(j)
    req_set[i] = lst

m = int(input("Enter number of sites requesting CS: "))

reqs = []
for _ in range(m):
    ts, sid = map(int, input("Enter timestamp and site no.: ").split())
    reqs.append((ts, sid))

reqs.sort()

queue = []
for ts, sid in reqs:
    queue.append(sid)

site_queues = {}
for i in range(1, n+1):
    site_queues[i] = []

print("\n--- Sending Requests ---")
for ts, sid in reqs:
    print(f"\nQueue: {queue}")
    for other in req_set[sid]:
        print(f"Site {sid} sends REQUEST to Site {other}")
        site_queues[other].append((ts, sid))
        print(f"Site {other} adds ({ts}, {sid}) to its queue")

print("\n--- Sending Replies and Entering CS ---")
for ts, sid in reqs:
    print(f"\nQueue: {queue}")
    for other in req_set[sid]:
        reply = False
        if other not in queue:
            reply = True
        else:
            for ts2, sid2 in reqs:
                if sid2 == other:
                    if ts2 > ts:
                        reply = True
                    break

        if reply:
            print(f"Site {other} sends REPLY to Site {sid}")

    print(f"Site {sid} enters CS")
    print(f"Site {sid} exits CS")
    queue.remove(sid)