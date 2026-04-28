from pydantic import BaseModel , Field , EmailStr , AnyUrl
from typing import List , Dict , Optional
class Patient(BaseModel):
    name: str = Field(max_length=50)
    age: int
    weight: float = 0.0
    married: bool = False
    contact: Dict[str , str]
    allergies: Optional[List[str]]

def insert_patient_record(patient: Patient):
    print(patient.model_dump())
    print(f"Inserted data of {patient.name}")
    
    

def update_patient_record(patient: Patient):
      
      print(f"Updated data of {patient.name}")

patient1_info = {"name":"Harsh", "age":20,"weight": 45.8, "married": False,"contact": {'phone': '123', 'email': 'abc'}, "allergies":["allergy1","allergy2"]}
patient2_info = {"name":"Aryan", "age":23,"weight": 78.8,"married": False,"contact": {'phone': '456', 'email': 'xyz'}, "allergies":["allergy1","allergy2"]}


patient1= Patient(**patient1_info)
patient2= Patient(**patient2_info)

insert_patient_record(patient1)
insert_patient_record(patient2)
update_patient_record(patient2)



