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