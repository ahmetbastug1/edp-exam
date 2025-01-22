communication_queue = []

def add_to_queue(event):
    communication_queue.append(event)
    
def process_queue():
    if communication_queue:  
        event = communication_queue.pop(0)  
        print(f"Processing event: {event.name}")
        if event.name == "ApplicationSubmittedEvent":
            print(f"Application submitted for: {event.payload['applicant_name']} applying for {event.payload['position_applied_for']}")
        elif event.name == "ApplicationRejectedEvent":
            print(f"Application rejected for: {event.payload['applicant_name']} for the position of {event.payload['position_applied_for']}")
    else:
        print("No events in the queue to process.")
