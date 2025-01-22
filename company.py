
from event import ApplicationRejectedEvent
from communication_queue import add_to_queue

class Company:
    def __init__(self, name):
        self.name = name

    def review_application(self, event):
        """Başvuru olayını incele ve sonucu işleme al."""
        if event.payload['position_applied_for'] == "Software Engineer":
            print(f"Rejecting application for {event.payload['applicant_name']} for the position of {event.payload['position_applied_for']}")
            rejection_event = ApplicationRejectedEvent(event.payload['applicant_name'], event.payload['position_applied_for'])
            add_to_queue(rejection_event)
        else:
            print(f"Accepting application for {event.payload['applicant_name']} for the position of {event.payload['position_applied_for']}")

        