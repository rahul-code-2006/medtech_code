class Patient:
    def __init__(self, name, age, weight_kg, height_m):
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.diagnoses = []

    def calculate_bmi(self):
        if self.height_m <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = round(self.weight_kg / (self.height_m ** 2),1)
        return bmi
    
    def add_diagnosis(self, diagnosis):
        self.diagnoses.append(diagnosis)

    def summary(self):
        self.calculate_bmi()
        diag_text = ", ".join(self.diagnoses) if self.diagnoses else "None"
        return(
            f"Patient : {self.name} | Age: {self.age} | BMI: {self.calculate_bmi()} | Diagnoses: {diag_text}"
        )
    

class ICUpatient(Patient):
    def __init__(self, name, age, weight_kg, height_m, icu_bed):
        super().__init__(name, age, weight_kg, height_m)
        self.icu_bed = icu_bed
        self.ventilated = False
    
    def put_on_ventilator(self):
        self.ventilated = True
        print(f"Patient {self.name} is now on a ventilator bed {self.icu_bed}.")

    def summary(self):
        base = super().summary()
        vent_status = "Ventilated" if self.ventilated else "Breathing independently"
        print(f"{base} | ICU Bed: {self.icu_bed} | {vent_status}")


class PaediatricPatient(Patient):
    def __init__(self, name, age, weight_kg, height_m, guardian_name):
        super().__init__(name, age, weight_kg, height_m)
        self.guardian_name = guardian_name
    
    def is_Underweight(self):
        bmi = self.calculate_bmi()
        return True if bmi < 16 else False

    def summary(self):
        base = super().summary()
        return f"{base} | Guardian: {self.guardian_name} | Underweight: {'Yes' if self.is_Underweight() else 'No'}"



icu_p = ICUpatient("Arjun", 55, 78, 1.72, icu_bed=4)
icu_p.add_diagnosis("Septic Shock")
icu_p.put_on_ventilator()

pp_1 = PaediatricPatient("Mia", 8, 25, 1.2, guardian_name="Sarah")
pp_1.add_diagnosis("Asthma")

pp_2 = PaediatricPatient("Liam", 5, 18, 1.0, guardian_name="David")
pp_2.add_diagnosis("Malnutrition")

p1 = Patient("John Doe", 30, 80, 1.75)

print(p1.summary())
print(icu_p.summary())
print(pp_1.summary())
print(pp_2.summary())