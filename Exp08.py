# Bankers Algorithm

def bankers_algorithm():
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))

    alloc = []
    max_alloc = []
    total_res = []
    avail = [0] * m
    need = [[0] * m for _ in range(n)]

    print("Enter the allocation matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        alloc.append(row)

    print("Enter the max allocation matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        max_alloc.append(row)

    print("Enter the total number of resources:")
    total_res = list(map(int, input().split()))

    for i in range(n):
        for j in range(m):
            avail[j] += alloc[i][j]

    for i in range(m):
        avail[i] = total_res[i] - avail[i]

    print("The available resources are:")
    print(avail)

    for i in range(n):
        for j in range(m):
            need[i][j] = max_alloc[i][j] - alloc[i][j]

    print("Need matrix",need)

    f = [0] * n
    ans = []

    for k in range(n):
        for i in range(n):
            if f[i] == 0:
                flag = True
                for j in range(m):
                    if need[i][j] > avail[j]:
                        flag = False
                        break
                if flag:
                    ans.append(i)
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    if all(f):
        print("No deadlock")
        print("The following is a safe sequence:")
        print(" -> ".join([f"P[{i}]" for i in ans]))
    else:
        print("Deadlock occurs")
        print("The system is not safe")

bankers_algorithm()