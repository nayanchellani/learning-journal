from fastapi import FastAPI , Path
import json
app = FastAPI()


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