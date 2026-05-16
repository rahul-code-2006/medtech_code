import numpy as np

patient_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112])
heart_rates = np.array([72, 110, 58, 145, 88, 62, 99, 130, 55, 78, 102, 91])


def ward_hr_monitor(ids, rates):

    print("="*45)
    print("\n     Ward Heart Rate Monitor")
    print("="*45)


    total_patients = len(ids)
    print(f"\nTotal number of patients: {total_patients}")
    mean_hr = np.mean(rates)
    print(f"Mean HR: {mean_hr:.1f} bpm")
    max_hr = np.max(rates)
    print(f"Highest HR: {max_hr} bpm (Patient {ids[np.argmax(rates)]})")
    min_hr = np.min(rates)
    print(f"Lowest HR: {min_hr} bpm (Patient {ids[np.argmin(rates)]})")


    print('\n\n', '-'*3 , "Risk classification" , '-'*3)
    bradycardia_mask = rates < 60
    tachycardia_mask = rates > 100
    bradycardic_patients = ids[bradycardia_mask]
    tachycardic_patients = ids[tachycardia_mask]
    normal_patients = (rates <= 100) & (rates >= 60)
    normal_patients = ids[normal_patients]
    print(f"Bradycardic (<60 bpm): {len(bradycardic_patients)} -> IDs: {bradycardic_patients}")
    print(f"Normal (60-100 bpm): {len(normal_patients)} -> IDs: {normal_patients}")
    print(f"Tachycardic (>100 bpm): {len(tachycardic_patients)} -> IDs: {tachycardic_patients}")
    critical_mask = rates > 140
    critical_patients = ids[critical_mask]
    
    
    if len(critical_patients) > 0:
        print(f"\n\n⚠ CRITICAL ALERT: {len(critical_patients)} Patient(s) with HR > 140 bpm:" , "\n  -> Immediate review:Patient IDs: " , critical_patients)


def main(ids, rates):
    ward_hr_monitor(ids, rates)


main(patient_ids, heart_rates)