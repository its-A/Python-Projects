attendance_records = [
    {'Employee ID ': 'emp001', 'Employee Name': 'Alice', ' Attendance date ': '2026-05-01', 'Status': ' present'},
    {'Employee ID ': 'EMP002', 'Employee Name': 'Bob',   ' Attendance date ': '2026-05-01', 'Status': 'ABSENT '},
    {'Employee ID ': 'emp003', 'Employee Name': 'Eve',   ' Attendance date ': '2026-05-03', 'Status': 'Present'},
    {'Employee ID ': 'EMP004', 'Employee Name': 'Frank', ' Attendance date ': '2026-05-03', 'Status': ' present'},
]

print("Original Attendance Records:\n")
for i, record in enumerate(attendance_records):
    print(f"{i+1}. {record}")


#Standardizing Column Names
# Extract the original column names
original_columns = attendance_records[0].keys()

# Clean the column names
standard_columns = [col.strip().lower().replace(' ', '_') for col in original_columns]

# Build a new dataset with standardized column names
standardized_records = []
for record in attendance_records:
    standardized_record = {}
    for old_col, new_col in zip(original_columns, standard_columns):
        standardized_record[new_col] = record[old_col]
    standardized_records.append(standardized_record)

print("\nDataset After Standardizing Column Names:\n")
for rec in standardized_records:
    print(rec)


#Standardizing Values Inside Fields
for record in standardized_records:
    # Clean employee_id: remove spaces, make uppercase
    record['employee_id'] = record['employee_id'].strip().upper()

    # Clean status: remove spaces, capitalize the first letter
    record['status'] = record['status'].strip().capitalize()

print("\nDataset After Fixing Structural Errors in Fields:\n")
for rec in standardized_records:
    print(rec)

#Detecting Out-of-Range Values > Data Validation
attendance_records = [
    {'employee_id': 'EMP001', 'employee_name': 'Alice', 'attendance_date': '2026-05-01', 'status': 'Present', 'hours_worked': 8},
    {'employee_id': 'EMP002', 'employee_name': 'Bob',   'attendance_date': '2026-05-01', 'status': 'Absent',  'hours_worked': -1},
    {'employee_id': 'EMP003', 'employee_name': 'Eve',   'attendance_date': '2026-05-03', 'status': 'Present', 'hours_worked': 9},
    {'employee_id': 'EMP004', 'employee_name': 'Frank', 'attendance_date': '2026-05-03', 'status': 'Present', 'hours_worked': 25},
    {'employee_id': 'EMP005', 'employee_name': 'Grace', 'attendance_date': '2026-05-04', 'status': 'Present', 'hours_worked': 7.5},
]

print("Attendance Records:\n")
for i, record in enumerate(attendance_records):
    print(f"{i+1}. {record}")

#Detecting Negative Values
negative_hours = []

for record in attendance_records:
    if record['hours_worked'] < 0:
        negative_hours.append(record)

print("Records with Negative 'hours_worked':\n")
for rec in negative_hours:
    print(rec)

#Detecting Excessively High Values
excessive_hours = []

for record in attendance_records:
    if record['hours_worked'] > 16:
        excessive_hours.append(record)

print("Records with Excessively High 'hours_worked':\n")
for rec in excessive_hours:
    print(rec)


#able to combine both checks into a single loop for efficiency
out_of_range_hours = []

for record in attendance_records:
    if record['hours_worked'] < 0 or record['hours_worked'] > 16:
        out_of_range_hours.append(record)

print("\nAll Records with Out-of-Range 'hours_worked':\n")
for rec in out_of_range_hours:
    print(rec)


#REPLACING or REMOVING FAULTY VALUES
#New dataset: attendence_records with 'hours_worked' field
attendance_data = [
    {'employee_id': 'EMP001', 'project_code': 'PROJ-A', 'hours_worked': 8},
    {'employee_id': 'EMP002', 'project_code': 'PROJ-A', 'hours_worked': -1},
    {'employee_id': 'EMP003', 'project_code': 'PROJ-B', 'hours_worked': 9},
    {'employee_id': 'EMP004', 'project_code': 'PROJ-A', 'hours_worked': 25},
    {'employee_id': 'EMP005', 'project_code': 'PROJ-B', 'hours_worked': 7.5},
    {'employee_id': 'EMP006', 'project_code': 'PROJ-C', 'hours_worked': None},
    {'employee_id': 'EMP007', 'project_code': None, 'hours_worked': 8},
]

print("--- Initial Dataset with Multiple Error Types ---")
for record in attendance_data:
    print(record)

#STEP 1: MARK INVALID VALUES as MISSING
for record in attendance_data:
    hours = record.get('hours_worked')
    if hours is not None and (hours < 0 or hours > 16):
        print(f"FLAGGING invalid hours_worked: {hours} for {record.get('employee_id')}")
        record['hours_worked'] = None

print("\n--- After Marking Invalid Values as None ---")
for record in attendance_data:
    print(record)


 #STEP 2: Imputing Missing Values with the Median   
 # Extract valid hours
valid_hours = [
    record['hours_worked'] for record in attendance_data
    if record.get('hours_worked') is not None
]

valid_hours.sort()

# Calculate the median manually
n = len(valid_hours)
if n == 0:
    median_hours = 0
elif n % 2 == 1:
    median_hours = valid_hours[n // 2]
else:
    mid1 = valid_hours[n // 2 - 1]
    mid2 = valid_hours[n // 2]
    median_hours = (mid1 + mid2) / 2

print(f"\nCalculated Median for 'hours_worked': {median_hours}")

# Fill missing values with the median
for record in attendance_data:
    if record.get('hours_worked') is None:
        print(f"IMPUTING hours_worked for {record.get('employee_id')} with median value {median_hours}")
        record['hours_worked'] = median_hours

print("\n--- After Imputing 'hours_worked' with Median ---")
for record in attendance_data:
    print(record)
#median imputation > fill in a reasonable value so the dataset stays larger and more complete

#Step 3: Removing Records with Critical Missing Data 
final_cleaned_data = []

for record in attendance_data:
    if record.get('project_code') is not None:
        final_cleaned_data.append(record)
    else:
        print(f"REMOVING record for {record.get('employee_id')} due to missing critical data (project_code)")

print("\n--- Final Cleaned Data ---")
for record in final_cleaned_data:
    print(record)


#VALIDATION DATA WITH CONDITIONALS
#adding total_billed_usd > checking whether each employee generated at least $12 per hour
#calculating the hourly billing rate for each record, compare it with the threshold, and store the result in a field such as is_valid

attendance_data = [
    {'employee_id': 'EMP001', 'project_code': 'PROJ-A', 'hours_worked': 8,   'total_billed_usd': 96},
    {'employee_id': 'EMP002', 'project_code': 'PROJ-A', 'hours_worked': -1,  'total_billed_usd': 20},
    {'employee_id': 'EMP003', 'project_code': 'PROJ-B', 'hours_worked': 9,   'total_billed_usd': 90},
    {'employee_id': 'EMP004', 'project_code': 'PROJ-A', 'hours_worked': 25,  'total_billed_usd': 200},
    {'employee_id': 'EMP005', 'project_code': 'PROJ-B', 'hours_worked': 7.5, 'total_billed_usd': 120},
    {'employee_id': 'EMP006', 'project_code': 'PROJ-C', 'hours_worked': None,'total_billed_usd': 90},
    {'employee_id': 'EMP007', 'project_code': None,     'hours_worked': 8,   'total_billed_usd': 60},
]

print("\n--- Initial Dataset (Pre-Validation) ---")
for rec in attendance_data:
    print(rec)

# Define the billing rate threshold

MIN_HOURLY_RATE = 12.0

for record in attendance_data:
    hours = record.get('hours_worked')
    billed = record.get('total_billed_usd')

    if hours is not None and hours > 0:
        hourly_rate = billed / hours
        record['hourly_rate'] = round(hourly_rate, 2)
        record['is_valid'] = hourly_rate >= MIN_HOURLY_RATE
    else:
        record['hourly_rate'] = None
        record['is_valid'] = False
        print(f"WARNING: Invalid or missing hours_worked for {record['employee_id']}")

print("\n--- After Calculating Hourly Rate and Applying Rule ---")
for rec in attendance_data:
    print(rec)

#Separating Valid & Invalid Records
valid_records = []
invalid_records = []

for rec in attendance_data:
    if rec.get('is_valid'):
        valid_records.append(rec)
    else:
        invalid_records.append(rec)

print("\nValid Records:")
for rec in valid_records:
    print(rec)

print("\nInvalid Records:")
for rec in invalid_records:
    print(rec)    