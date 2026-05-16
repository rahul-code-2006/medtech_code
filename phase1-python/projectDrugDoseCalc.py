Drugs = {
    "paracetamol": {
        "dose_per_kg": 15,
        "max_dose": 1000,
        "unit": "mg",
        "frequency": "every 6 hours"
    },
    "ibuprofen": {
        "dose_per_kg": 10,
        "max_dose": 400,
        "unit": "mg",
        "frequency": "every 8 hours"
    },
    "amoxicillin": {
        "dose_per_kg": 25,
        "max_dose": 500,
        "unit": "mg",
        "frequency": "every 8 hours"
    },
    "cetirizine": {
        "dose_per_kg": 0.25,
        "max_dose": 10,
        "unit": "mg",
        "frequency": "once daily"
    },
    "aspirin": {
        "dose_per_kg": 5,
        "max_dose": 4000,
        "unit": "mg",
        "frequency": "every 6 hours"
    }
}

def calculate_dose(weight_kg, drug_name):
    if drug_name not in Drugs:
        return None , f"Drug '{drug_name}' not found in database."
    
    Drug = Drugs[drug_name]

    Calculated_dose = weight_kg * Drug["dose_per_kg"]
    Final_dose = min(Calculated_dose, Drug["max_dose"])
    capped = Calculated_dose > Drug["max_dose"]
    return Final_dose, Drug, capped


def print_Prescription(patient_name, weight_kg, drug_name):
    dose, Drug_info , capped = calculate_dose(weight_kg, drug_name)
    
    if dose is None:
        print(f"Error: {Drug_info}")  # This will print the error message
        return

    print("\n" + "="*45)
    print(f"  PRESCRIPTION SUMMARY")
    print("="*45)
    print(f"  Patient  : {patient_name}")
    print(f"  Weight   : {weight_kg} kg")
    print(f"  Drug     : {drug_name.capitalize()}")
    print(f"  Dose     : {round(dose, 1)} {Drug_info['unit']}")
    print(f"  Schedule : {Drug_info['frequency']}")

    if capped:
        print(f"  ⚠ Note   : Calculated dose ({round(raw_dose,1)}{Drug_info['unit']}) exceeds maximum.")
        print(f"             Capped at {Drug_info['max_dose']}{Drug_info['unit']} for patient safety.")
    print("="*45 + "\n")



def main():
    print("Welcome to the Drug Dosage Calculator!")
    print(f"Available drugs: {', '.join(Drugs.keys())}\n")

    while True:

        patient_name = input("Enter patient's name (or 'exit' to quit): ")
        if patient_name.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            weight_kg = float(input("Enter patient's weight in kg: "))
        except ValueError:
            print("Invalid input for weight. Please enter a number.")
            continue

        drug_name = input("Enter drug name: ").lower()
        print_Prescription(patient_name, weight_kg, drug_name)


main()
