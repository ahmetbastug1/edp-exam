
from event import ApplicationSubmittedEvent

class Applicant:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_of_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number

    
    def apply_for_job(self, position_applied_for):
        event = ApplicationSubmittedEvent(self.first_name + " " + self.last_name, position_applied_for)
        return event
