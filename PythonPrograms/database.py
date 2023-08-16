import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create a new user in the database
def create_user(name, email):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)
    db.commit()
    print("User created successfully!")

# Read a user from the database
def read_user(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("User ID:", result[0])
        print("Name:", result[1])
        print("Email:", result[2])
    else:
        print("User not found")

# Update a user in the database
def update_user(id, name, email):
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    values = (name, email, id)
    cursor.execute(sql, values)
    db.commit()
    print("User updated successfully!")

# Delete a user from the database
def delete_user(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    db.commit()
    print("User deleted successfully!")

# Create a new user
create_user("Alice", "alice@example.com")

# Read the user we just created
read_user(1)

# Update the user's name and email
update_user(1, "Alice Smith", "alice.smith@example.com")

# Read the user again to verify the changes
read_user(1)

# Delete the user from the database
delete_user(1)

# Try to read the user again (should fail)
read_user(1)

# Close the database connection
db.close()
