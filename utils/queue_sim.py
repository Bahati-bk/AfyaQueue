import random
import threading
import time

# Global queue
queue = []

def add_patient(patient_name, urgency):
    queue.append({"name": patient_name, "urgency": urgency})

def remove_patient():
    if queue:
        queue.pop(0)

def get_current_queue_length():
    return len(queue)

def predict_waiting_time():
    """
    Predict waiting time based on queue length.
    High urgency patients are prioritized.
    """
    total_time = 0
    for p in queue:
        if p['urgency'] == "High":
            total_time += 5
        elif p['urgency'] == "Medium":
            total_time += 10
        else:
            total_time += 15
    return total_time

# Auto-update queue in background
def simulate_queue_flow():
    while True:
        # Randomly patients arrive
        if random.random() < 0.5:
            add_patient(f"Patient{random.randint(1,100)}", random.choice(["Low","Medium","High"]))
        # Randomly patients are served
        if random.random() < 0.7:
            remove_patient()
        time.sleep(5)  # update every 5 seconds

# Start simulation in background
threading.Thread(target=simulate_queue_flow, daemon=True).start()