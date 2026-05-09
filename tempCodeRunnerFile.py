#Using set() for Fast Membership Testing
login_attempts = ['user123', 'user456', 'user789', 'user999', 'user000']
blacklisted_ids = set(['user000', 'user888', 'user123', 'user777'])

for user_id in login_attempts:
    if user_id in blacklisted_ids:
        print(f"Access denied for {user_id} (blacklisted)")
    else:
        print(f"Access granted for {user_id}")