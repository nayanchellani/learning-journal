from pydantic import BaseModel , Field , EmailStr , AnyUrl , field_validator
from typing import List , Dict , Optional
class Patient(BaseModel):
    name: str 
    age: int 
    email: str
    weight: float 
    married: bool 
    contact: Dict[str , str]
    allergies: Optional[List[str]]
    
    
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domains=["hdfc.com", "icici.com"]
        domain_name= value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("not a valid email address")
        
        else: return value
        
    
    

def insert_patient_record(patient: Patient):
    print(patient.model_dump())
    print(f"Inserted data of {patient.name}")
    
    

def update_patient_record(patient: Patient):
      
      print(f"Updated data of {patient.name}")

patient1_info = {"name":"Harsh", "age":20,"email":"xyz@icici.com ","weight": 45.8, "married": False,"contact": {'phone': '123', 'email': 'abc'}, "allergies":["allergy1","allergy2"]}
patient2_info = {"name":"Aryan", "age":23,"email":"abc@gmail.com ","weight": 78.8,"married": False,"contact": {'phone': '456', 'email': 'xyz'}, "allergies":["allergy1","allergy2"]}


patient1= Patient(**patient1_info)
patient2= Patient(**patient2_info)

insert_patient_record(patient1)
insert_patient_record(patient2)
update_patient_record(patient2)