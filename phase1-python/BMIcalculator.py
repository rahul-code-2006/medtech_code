def classify_bmi(weight_kg, height_m):
    bmi = round(weight_kg / (height_m ** 2), 1)

    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi <= 24.9:
        return bmi, "Normal"
    elif bmi <= 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"


# Test with 3 patients
patients = [
    ("Rahul",  58, 1.75),
    ("Priya",  90, 1.60),
    ("Arjun",  48, 1.70),
]

for name, weight, height in patients:
    bmi, category = classify_bmi(weight, height)
    print(f"{name}: BMI {bmi} → {category}")
