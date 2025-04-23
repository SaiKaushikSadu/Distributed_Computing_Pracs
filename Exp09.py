import random

# Dictionary representing servers and their current load (number of connections)
server_load = {'Server1': 2, 'Server2': 5, 'Server3': 1}
number_of_tasks = 6  # Total tasks to assign

# --- Round Robin Load Balancer ---
def round_robin():
    print("\n-- Round Robin --")
    servers = list(server_load.keys())
    print("Server load: ", servers)
    index = 0  # Start from the first server
    for task_id in range(1, number_of_tasks + 1):
        selected_server = servers[index]
        print(f"Task {task_id} -> {selected_server}")
        index = (index + 1) % len(servers)  # Move to the next server circularly

# --- Random Load Balancer ---
def random_choice():
    print("\n-- Random --")
    servers = list(server_load.keys())
    for task_id in range(1, number_of_tasks + 1):
        selected_server = random.choice(servers)
        print(f"Task {task_id} -> {selected_server}")

# --- Least Connections Load Balancer ---
def least_connections():
    print("\n-- Least Connections --")
    for task_id in range(1, number_of_tasks + 1):
        # Pick the server with the fewest current connections
        selected_server = min(server_load, key=server_load.get)
        print(f"Task {task_id} -> {selected_server}")
        server_load[selected_server] += 1  # Simulate the task being assigned

# --- The Least Time Load Balancer ---
def least_time():
    print("\n-- Least Time --")
    server_time = {'Server1': 0.3, 'Server2': 0.7, 'Server3': 0.2}
    for task_id in range(1, number_of_tasks + 1):
        selected_server = min(server_time, key=server_time.get)
        print(f"Task {task_id} -> {selected_server}")
        server_time[selected_server] += random.uniform(0.05, 0.2)

chosen_method = 1

# Call the selected method
if chosen_method == 1:
    round_robin()
elif chosen_method == 2:
    random_choice()
elif chosen_method == 3:
    least_connections()
elif chosen_method == 4:
    least_time()
else:
    print("Invalid choice!")