class Event:
    def __init__(self, name, payload=None):
        self.name = name
        self.payload = payload   
    class ApplicationSubmittedEvent(Event):
    def __init__(self, applicant_name, position_applied_for):
        super().__init__("ApplicationSubmittedEvent", {"applicant_name": applicant_name, "position_applied_for": position_applied_for})
      class ApplicationSubmittedEvent(Event):
        def_init_(self,name,is_confirmed)
        super()._init_("application_recived") , {"name": name, "is_confirmed": is_confirmed})

communucation_queue =[]

class Applicant
def_init_(self,firt_name, last_name, day_of_birth, address, phone_number):
self.first_name = first_name
self.last_name = last_name
self.day_of_birth = day_of_birth
self.address = address
self.phone_number = phone_number

def ask_for_application(self,date)
     event = ApplicationSubmittedEvent(self,name, date)


    communucation_queue_append(Event)
       print("Event")