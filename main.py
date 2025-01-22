import time
from applicant import Applicant
from company import Company
from event import ApplicationSubmittedEvent
from communication_queue import add_to_queue, process_queue

def event_loop():
    while True:
        
            process_queue()
            time.sleep(1)

if __name__ == "__main__":
    company = Company("Tech Corp")
    applicant = Applicant("John", "Doe", "1990-01-01", "1234 Elm St", "123-456-7890")
    event = applicant.apply_for_job("Software Engineer")
    add_to_queue(event)

company.review_application(event)
print("Starting event loop...")
event_loop()