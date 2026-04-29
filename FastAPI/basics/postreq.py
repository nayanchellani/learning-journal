from fastapi import FastAPI, HTTPException , Path
from pydantic import BaseModel , Field , computed_field
import json
app = FastAPI()

class Patient(BaseModel):
    name:str = Field(max_length=50)
    city:str
    age:int = Field(gt=0,lt=70)
    gender:str
    height:float
    weight:float
    
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
        
    @computed_field
    @property
    def verdict(self):
        if self.bmi < 18.5:
            print("Underweight")
        elif self.bmi < 30:
            print("Normal")
        else: print("Obese")

def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
        return data


@app.get("/view")
def view_patients():
    data = load_data()
    return data

@app.get("/view/{patient_id}")

def view_patient(patient_id : str = Path(..., description='ID of the patient in the database',examples='P003')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error": "patient not found"}
    
    
@app.post('/create')
def create_patient(patient: Patient):
    data = load_data
    if patient.id in data:
        raise HTTPException(status_code=400, description="Patient ID already exists.")
    elif ??how do i put the data in the json file 