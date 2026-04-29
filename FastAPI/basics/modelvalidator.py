from pydantic import BaseModel , Field , model_validator
from typing import List , Dict , Optional
class Patient(BaseModel):
    name: str 
    age: int 
    email: str
    weight: float 
    married: bool 
    contact: Dict[str , str]
    allergies: Optional[List[str]]
    
    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age> 60 and 'emergency' not in model.contact:
            raise ValueError("Patients older than 60 years of age should have a emergency contact number.")
    
        
def insert_patient_record(patient: Patient):
    print(patient.model_dump())
    print(f"Inserted data of {patient.name}")
    
    

def update_patient_record(patient: Patient):
      
      print(f"Updated data of {patient.name}")

patient1_info = {"name":"Harsh", "age":70,"email":"xyz@icici.com ","weight": 45.8, "married": False,"contact": {'phone': '123', 'email': 'abc'}, "allergies":["allergy1","allergy2"]}
patient2_info = {"name":"Aryan", "age":23,"email":"abc@gmail.com ","weight": 78.8,"married": False,"contact": {'phone': '456', 'email': 'xyz'}, "allergies":["allergy1","allergy2"]}


patient1= Patient(**patient1_info)
patient2= Patient(**patient2_info)

insert_patient_record(patient1)
insert_patient_record(patient2)
update_patient_record(patient2)