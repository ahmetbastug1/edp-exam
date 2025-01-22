class Event:
    def __init__(self, name, payload=None):
        self.name = name 
        self.payload = payload
class ApplicationSubmittedEvent(Event):
    def __init__(self, applicant_name, position_applied_for):
        super().__init__("ApplicationSubmittedEvent",{"applicant_name": applicant_name,"position_applied_for": position_applied_for})

class ApplicationRejectedEvent(Event):
    def __init__(self, applicant_name, position_applied_for):
        super().__init__("ApplicationRejectedEvent",{"applicant_name": applicant_name, "position_applied_for": position_applied_for})

        