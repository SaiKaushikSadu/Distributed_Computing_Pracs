# Bully Election Algorithm

num = int(input("Enter number of processes: "))
processes = [True for i in range(num)]

crashed = int(input("Enter process that is crashed: "))
processes[crashed] = False

initiator = int(input("Enter initiator process that will initiate election: "))
print(f"Process: {initiator} is starting the election.")
print(f"Process: {crashed} is crashed.")

def send_election_message(p_id):
    print(f"Sending election message from {p_id} to higher processes")
    received_okay = False
    for i in range(p_id+1,num):
        if processes[i]:
            print(f"Okay message from {i} to {p_id}.")
            received_okay = True
            send_election_message(i)
            break
    if not received_okay:
        declare_coordinator(p_id)

def declare_coordinator(co_id):
    print(f"Final coordinator: {co_id}")
    for i in range(num):
        if i!=co_id and processes[i]:
            print(f"Message to  {i}: Coordinator is  {co_id}")

send_election_message(initiator)