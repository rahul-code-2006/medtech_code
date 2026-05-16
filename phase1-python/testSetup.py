import sys
import numpy as np
import pandas as pd

print(f"✓ Python: {sys.version}")
print(f"✓ NumPy: {np.__version__}")
print(f"✓ Pandas: {pd.__version__}")

# Your first medical data structure
patients = pd.DataFrame({
    'name':         ['Alice', 'Bob', 'Carol'],
    'age':          [34, 56, 45],
    'bp_systolic':  [120, 145, 130],
    'bp_diastolic': [80, 92, 85]
})

print("\n✓ First patient DataFrame:")
print(patients)
print(f"\n✓ Average systolic BP: {patients['bp_systolic'].mean()} mmHg")
print("\n🎉 Your environment is ready. Day 1 starts now.")