import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()

def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", user_id)
    conn.commit()

def calculate_age(birth_year):
    return 2024 / (2024 - birth_year)
```

This file has 3 real bugs:
- SQL injection vulnerability
- Missing parameter tuple in delete
- Division error in calculate_age

Click **Commit changes** then go to the agent and type:
```
Please analyze database.py for bugs and create a GitHub issue
