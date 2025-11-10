"""
Master script - Run complete analysis pipeline
"""

import os

print("=" * 70)
print(" E-COMMERCE ANALYTICS - COMPLETE PIPELINE")
print("=" * 70)

# Create output folders
os.makedirs('output', exist_ok=True)
os.makedirs('output/charts', exist_ok=True)

scripts = [
    ('generate_sample_data.py', 'Data Generation'),
    ('ecommerce_analysis.py', 'Basic Analysis'),
    ('rfm_analysis.py', 'RFM Segmentation'),
    ('visualizations.py', 'Visualizations'),
    ('forecasting.py', 'Sales Forecasting')
]

for script, name in scripts:
    print(f"\n{'=' * 70}")
    print(f"Running: {name}")
    print('=' * 70)
    exec(open(script).read())
    print(f"\n✅ {name} complete!")

print("\n" + "=" * 70)
print(" ALL ANALYSES COMPLETE!")
print("=" * 70)
print("\n📁 Check the 'output' folder for results:")
print("   • rfm_segmentation.csv")
print("   • segment_summary.csv")
print("   • sales_forecast.csv")
print("   • charts/ folder with all visualizations")