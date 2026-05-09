import re

# --- Data Representation ---
# We start with a list of dictionaries.
transactions = [
    {'transaction_id': 1, 'description': 'Sale of PROD-481a for $299'},
    {'transaction_id': 2, 'description': 'Item PROD-92841 sold'},
    {'transaction_id': 3, 'description': 'Returned Item (PROD-552)'},
    {'transaction_id': 4, 'description': 'Misc sale, no product code'}
]

# --- Data Preview 1: The Original Data ---
print("--- Original Sales Transactions (List of Dictionaries) ---")
# We loop through the list to print each record in its initial state.
for transaction in transactions:
    print(transaction)
print("-" * 55) # Separator for clarity

# --- The Extraction Function (Unchanged) ---
# This function uses the 're' module to find a pattern in a given string.
def extract_product_id(description):
    """
    Searches for a product ID pattern in a description string.
    The pattern looks for 'PROD-' followed by an alphanumeric code/hyphen.
    Example: PROD-481a, PROD-92841, PROD-552
    """
    # The regex r'(PROD-[\w-]+)' will correctly capture codes with letters,
    # numbers, and hyphens.
    match = re.search(r'(PROD-[\w-]+)', description)
    
    # If a match is found, return the captured group. Otherwise, return None.
    if match:
        return match.group(1)
    return None

# --- Applying the Function with a Loop and Previews ---
print("\n--- Processing Each Transaction and Extracting IDs ---")
# We use a standard 'for' loop to iterate over our list of dictionaries.
for transaction in transactions:
    # Preview of the current record being processed
    print(f"\nProcessing transaction_id: {transaction['transaction_id']}")
    
    # Access the 'description' value.
    desc = transaction['description']
    print(f"  -> Description: '{desc}'")
    
    # Call our function to get the product_id.
    product_id = extract_product_id(desc)
    print(f"  -> Extracted ID: {product_id}")
    
    # Add the new key-value pair to the dictionary.
    transaction['product_id'] = product_id
    
    # Preview of the record after modification
    print(f"  -> Record after update: {transaction}")
print("-" * 55) # Separator for clarity

# --- Data Preview 2: The Final, Transformed Data ---
print("\n--- Final Transactions after Extracting Product IDs ---")
# Print the modified list of dictionaries to see the final result.
for transaction in transactions:
    print(transaction)



# --- Additional Examples of Data Cleaning ---
#UNICODE NORMALIZATION
#removing accents and special characters
import unicodedata
name1 = 'José'
name2 = 'Jose\u0301'

print(f"Name 1: {name1}, Name 2: {name2}")
print(f"Are the strings equal? {name1 == name2}")


import unicodedata

name1 = 'José'          # A single, pre-composed character
name2 = 'Jose\u0301'    # The letter 'e' followed by a combining accent

normalized_name1 = unicodedata.normalize('NFC', name1)
normalized_name2 = unicodedata.normalize('NFC', name2)

print("\n---After Normalization Process---")
print(f"Normalized Name 1: {normalized_name1}, Normalized Name 2: {normalized_name2}")
print(f"Are the normalized strings equal? {normalized_name1 == normalized_name2}")


print("\n--- Additional Examples of Data Cleaning: Fuzzy String Matching---\n")
#Fuzzy String Matching
#sometimes the problem is a typo or a slight variation in spelling. Fuzzy string matching can help identify similar strings.
#Edit Distance: Measures the number of edits (insertions, deletions, substitutions) needed to transform one string into another.

from thefuzz import process, fuzz

# Canonical list of company names
canonical_names = ['Apple Inc.', 'Google LLC', 'Microsoft Corporation']

# Raw data with variations
raw_data = ['Apple', 'Google', 'Microsoft Corp.', 'Aple Inc.']

print("Canonical list of company names: \n", canonical_names)
print("\nRaw data with variations: \n", raw_data)

cleaned_data = {}

for name in raw_data:
    # Find the best match from the canonical list with a cutoff of 85
    match = process.extractOne(name, canonical_names, score_cutoff=85)
    #This line looks through the list of canonical names and finds the best match for the current raw string

    #The argument score_cutoff=85 means:
    #Only accept the match if the similarity score is at least 85 out of 100


    if match:
        # Map the raw name to its canonical version
        cleaned_data[name] = match[0]
    else:
        cleaned_data[name] = 'No match found'

print("\nAfter of Fuzzy String Matching:\n",cleaned_data)


print("\n--- Additional Examples of Data Cleaning: Chaining String Operations---\n")

# Raw data simulating manual entries, stored as a list of dictionaries.
# Each dictionary represents a student's registration record.
data = [
    {'student_id': 1001, 'course_code': '  cs-101  ', 'semester': 'fall 2023'},
    {'student_id': 1002, 'course_code': 'math 105', 'semester': 'Fall-2023'},
    {'student_id': 1003, 'course_code': '  PHY_202', 'semester': ' spring 2024'},
    {'student_id': 1004, 'course_code': 'chem-101  ', 'semester': 'SPRING_2024'}
]

print("--- Original Data (List of Dictionaries) ---")
for record in data:
    print(record)

# --- Reusable Cleaning Function ---
def normalize_text(text_string):
    """
    Applies a chain of string methods to clean and standardize a string.
    1. Removes leading/trailing whitespace.
    2. Converts to uppercase.
    3. Replaces spaces with hyphens.
    4. Replaces underscores with hyphens.
    """
    return text_string.strip().upper().replace(' ', '-').replace('_', '-')

# --- Applying the Cleaning Logic ---
# We will create a new list to hold the final, cleaned data.
cleaned_data = []

print("\n--- Processing and Cleaning Each Record ---")

# Iterate through each dictionary in our original data list
for record in data:
    # Extract the original values
    original_code = record['course_code']
    original_semester = record['semester']

    # Apply the cleaning function using method chaining
    cleaned_code = normalize_text(original_code)
    cleaned_semester = normalize_text(original_semester)

    # Combine the cleaned parts to create the final ID
    standardized_id = f"{cleaned_code}_{cleaned_semester}"

    # Create a new dictionary with the clean data
    new_record = {
        'student_id': record['student_id'],
        'standardized_id': standardized_id
    }

    # Add the newly created clean record to our list
    cleaned_data.append(new_record)

    # Preview the transformation for this specific record
    print(f"\nProcessing student_id: {record['student_id']}")
    print(f"  Original: ('{original_code}', '{original_semester}')")
    print(f"  Cleaned:  ('{cleaned_code}', '{cleaned_semester}')")
    print(f"  -> Final ID: {standardized_id}")


# --- Final Standardized Output ---
print("\n--- DataFrame After Cleaning and Standardization ---")
for record in cleaned_data:
    print(record)



print("\n--- Additional Examples of Data Cleaning: Splitting & Joining Strings---\n")
#.split() – breaks a string into pieces,
#.split(separator) breaks a string into a list, splitting every time it finds the separator.

sku = "SHOES-RUNNING-BLUE"
parts = sku.split("-")

print(parts)

#.join() – puts several strings back together.
#The method separator.join(list_of_strings) does the opposite. It takes several strings and joins them into one string, using the separator between them

words = ["Blue", "Running"]
description = " ".join(words)

print(description)


print("\n--- Additional Examples of Data Cleaning: SHandling Date and Time Strings---\n")
#parsing – converting a string into a datetime object > strptime()
#formatting – converting a datetime object back into a readable string > strftime()

from datetime import datetime

# Step 1
log_data = [
    {'user_id': 'user_a', 'login_time_str': '14/Jul/2025:09:30:15'},
    {'user_id': 'user_b', 'login_time_str': '14/Jul/2025:11:05:45'},
    {'user_id': 'user_c', 'login_time_str': '15/Jul/2025:14:22:05'},
    {'user_id': 'user_d', 'login_time_str': '15/Jul/2025:08:55:10'}
]

print("Original data:\n")
for record in log_data:
    print(record)

# Step 2
format_code = '%d/%b/%Y:%H:%M:%S'

for record in log_data:
    raw_time = record['login_time_str']
    
    parsed_time = datetime.strptime(raw_time, format_code)
    
    record['login_time'] = parsed_time

print("\nAfter parsing:\n")
for record in log_data:
    print(record)

# Step 3
print("\nAfternoon logins:\n")

for record in log_data:
    if record['login_time'].hour >= 12:
        print(record)

# Step 4
print("\nFormatted output:\n")

for record in log_data:
    readable = record['login_time'].strftime('%A, %B %d, %Y at %I:%M %p')
    print(f"{record['user_id']} -> {readable}")