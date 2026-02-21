# utils/hospital.py
import pandas as pd

def get_hospital_queue(hospital_id):
    df = pd.read_excel("hospitals.xlsx")
    hospital = df[df['HospitalID'] == hospital_id].iloc[0]
    return load_queue_from_excel(hospital['ExcelQueuePath'])