
import pandas as pd

# Load the original and audited datasets
original = pd.read_csv("cmu-sleep.csv")
audit = pd.read_csv("cmu_sleep_audit_75.csv")

print("Original dataset:", len(original), "records")
print("Audited dataset:", len(audit), "records")

# Check how many records came from each study group
print("\nRecords per study group:")
print(audit["study"].value_counts().sort_index())

# Check that all 75 records came from the original dataset
id_columns = ["study", "cohort", "subject_id"]

original_ids = original[id_columns].drop_duplicates()
selected_ids = audit[id_columns].drop_duplicates()

matched = selected_ids.merge(
    original_ids,
    on=id_columns,
    how="left",
    indicator=True
)

print("\nRecords found in original dataset:")
print((matched["_merge"] == "both").sum(), "out of", len(audit))

# Check the sleep duration conversion from minutes to hours
# Allow small differences caused by rounding to 2 decimal places
calculated_hours = audit["TotalSleepTime"] / 60

hours_correct = (
    (calculated_hours - audit["sleep_hours_derived"]).abs() <= 0.0051
).all()

print("\nSleep hours calculated correctly:", hours_correct)

# Check sleep data coverage categories
def categorize_coverage(fraction):
    if fraction >= 0.80:
        return "high (>= 80%)"
    elif fraction >= 0.50:
        return "moderate (50%-<80%)"
    else:
        return "low (<50%)"

calculated_coverage = audit["frac_nights_with_data"].apply(
    categorize_coverage
)

coverage_correct = (
    calculated_coverage == audit["sleep_data_coverage_audit"]
).all()

print("Sleep coverage categories correct:", coverage_correct)

# Calculate average nightly sleep
average_sleep = audit["sleep_hours_derived"].mean()

print("\nAverage nightly sleep:")
print(round(average_sleep, 2), "hours")

# Count records in each sleep coverage category
print("\nSleep data coverage:")
print(audit["sleep_data_coverage_audit"].value_counts())

# Check for missing values in the original columns
original_columns = original.columns.tolist()
missing_values = audit[original_columns].isna().sum()

print("\nMissing values in original columns:")
print(missing_values[missing_values > 0])

# Final summary
print("\nAudit check complete!")
