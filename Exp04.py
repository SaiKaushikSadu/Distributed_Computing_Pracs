# Berkeley Algorithm
import time

def to_min(txt):
    times = input(txt)
    h, m = map(int, times.split(":"))
    return h * 60 + m

def to_hhmm(mins):
    return f"{mins // 60:02d}:{mins % 60:02d}"

def berkeley_algorithm():
    print("\n--- Berkeley Clock Synchronization ---\n")
    n = int(input("Enter the number of nodes: "))
    main = to_min("Enter the main clock time (HH:MM): ")
    print(f"The main clock time is: {to_hhmm(main)}\n")

    nodes = []
    for i in range(n):
        time.sleep(0.5)
        t = to_min(f"Enter the time for the node {i+1} in (HH:MM) format : ")
        nodes.append(t)

    print("\nNode Times:")
    for i in range(n):
        print(f"Node {i + 1}: {to_hhmm(nodes[i])}")

    print("\nTime differences from the main clock:")
    diffs = []
    for i in range(n):
        d = nodes[i] - main
        diffs.append(d)
        print(f"Node {i + 1}: {d:+} minutes")

    avg = sum(diffs) // (n + 1)
    print(f"\nAverage offset from main clock: {avg:+} minutes")

    print("\nNew Synchronized Times:")
    print(f"Main Clock: {to_hhmm(main + avg)}")
    for i in range(n):
        adjustment = avg - diffs[i]
        synced_time = nodes[i] + adjustment
        print(f"Node {i + 1}: {to_hhmm(synced_time)} (adjusted by {adjustment:+} mins)")

    print("\n--- Clock Sync Complete ---")

berkeley_algorithm()
