from fastapi import FastAPI, HTTPException , Path
from pydantic import BaseModel , Field , computed_field
import json
app = FastAPI()

class Patient(BaseModel):
    id: str
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
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        else: return "Obese"

def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
        return data


@app.get("/view")
def view_patients():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
def view_patient(patient_id : str = Path(..., description='ID of the patient in the database', examples=['P003'])):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    
@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists.")
    else: 
        patient_dict = patient.model_dump()
        data[patient.id] = patient_dict
        with open('patients.json','w') as f:
            json.dump(data,f,indent=4)
        return "Patient created successfully"

    
    
    