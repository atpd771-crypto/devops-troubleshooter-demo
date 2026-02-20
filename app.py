def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def get_user(user_id):
    users = {"1": "Alice", "2": "Bob"}
    if user_id not in users:
        return "Error: User not found"
    return users[user_id]

def process_data(data):
    if "value" not in data:
        return "Error: Missing value key"
    result = data["value"] * 2
    return result
