communication_queue = []

def add_to_queue(event):
    communication_queue.append(event)
    
def process_queue():
    event = communication_queue.pop(0)
    print(f"Processing event: {event.name}")
