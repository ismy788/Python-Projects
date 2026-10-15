registered_users = []
failed_registrations = []

def validate_name(name):
    if len(name) >= 3:
        return True
    return False

def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

def validate_password(password):
    if len(password) < 8:
        return False
    if password == password.lower():
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

def validate_user_data(name, email, password):
    if not validate_name(name):
        raise ValueError("Invalid name: must be at least 3 characters long.")
    if not validate_email(email):
        raise ValueError("Invalid email: must contain both '@' and '.'.")
    if not validate_password(password):
        raise ValueError("Invalid password: must be at least 8 characters long, with at least one uppercase letter and one digit.")
    return True

def create_user_account(name, email, password):
    try:
        validate_user_data(name, email, password)

        for user in registered_users:
            if user["email"] == email:
                raise ValueError("Duplicate email")

        user = {"name": name, "email": email, "password": password, "status": "active"}
        registered_users.append(user)
        return user

    except ValueError as e:
        failed_registrations.append({"email": email, "error": str(e)})
        return None

print("Test 1: Valid registration")
print(create_user_account("Dan", "dan@example.com", "Hello123"))

print("\nTest 2: Duplicate email")
print(create_user_account("Bob", "bob@example.com", "Hello123"))

print("\nTest 3: Invalid name")
print(create_user_account("Sarah", "sarah@example.com", "Hello123"))

print("\nTest 4: Invalid email")
print(create_user_account("Chloe", "chloeexample.com", "Hello123"))

print("\nTest 5: Weak password")
print(create_user_account("Michael", "michael@example.com", "hello"))

print("\nFinal registered_users:")
print(registered_users)

print("\nFinal failed_registrations:")
print(failed_registrations)