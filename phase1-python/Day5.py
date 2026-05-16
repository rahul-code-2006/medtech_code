import numpy as np

patients = [
    {"id": 201, "name": "Aanya",  "age": 34, "weight": 68, "height": 1.62},
    {"id": 202, "name": "Bilal",  "age": 57, "weight": 82, "height": 1.74},
    {"id": 203, "name": "Ceena",  "age": 29, "weight": 54, "height": 1.58},
    {"id": 204, "name": "Danish", "age": 71, "weight": 91, "height": 1.69},
    {"id": 205, "name": "Esha",   "age": 45, "weight": 76, "height": 1.65},
    {"id": 206, "name": "Farhan", "age": 23, "weight": 48, "height": 1.71},
]

heart_rates = np.array([88, 112, 65, 145, 92, 58])
systolic_bp = np.array([118, 152, 124, 168, 136, 108])


class Patient:
    def __init__(self, id, name, age, weight, height, HR, SBP):
        self.id = id
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.HR = HR
        self.SBP = SBP
        self.Status = None
    def get_bmi(self):
        return round(self.weight / (self.height ** 2), 1)

    def bmi_category(self):
        bmi = self.get_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def vital_status(heart_rate, systolic_bp):

    if heart_rate > 140 or systolic_bp > 160 or heart_rate < 60 or systolic_bp < 110:
        return "CRITICAL"
    elif heart_rate > 100 or systolic_bp > 140:
        return "Warning"
    else:
        return "Stable"
    

def ward_report(patients, heart_rates, systolic_bp):
    print('=' * 50)
    print("       ICU Ward Management System")
    print('=' * 50)

    patient_list = []
    
    for i in patients:
        patient = Patient(i['id'], i['name'], i['age'], i['weight'], i['height'], heart_rates[i['id'] - 201], systolic_bp[i['id'] - 201])
        patient.Status = vital_status(patient.HR, patient.SBP)
        patient_list.append(patient)

    print("  ID  | Name   | Age | BMI  | Category       | Status")
    print('-' * 50)
    for i in patient_list:
        print(f"  {i.id:<7} | {i.name:<10} | {i.age:<5} | {i.get_bmi():<6} | {i.bmi_category():<15} | {i.Status::<8}")
    print('-' * 50)

    print(f"Total Patients: {len(patients)}")
    print(f"Mean HR: {np.mean(heart_rates):.1f} bpm")
    print(f"Mean SBP: {np.mean(systolic_bp):.1f} mmHg")
    print(f"Critical Alerts: {sum(1 for p in patient_list if p.Status == 'CRITICAL')}")
    print(f"Stable Patients: {sum(1 for p in patient_list if p.Status == 'Stable')}")

    print('=' * 50)
    if any(p.Status == "CRITICAL" for p in patient_list):
        print(f"⚠ CRITICAL PATIENTS — IMMEDIATE REVIEW:")
        for p in patient_list:
            if p.Status == "CRITICAL":
                print(f"  -> {p.name} (ID: {p.id}) | HR: {p.HR} | SBP: {p.SBP} mmHg")






ward_report(patients, heart_rates, systolic_bp)