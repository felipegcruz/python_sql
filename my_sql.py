import mysql.connector
import csv

# Connect to MySQL database
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="220664",
    database="new_schema"
)
cursor = connection.cursor()

# Example: Query to get all columns from the employees table
query = "SELECT * FROM employees"
cursor.execute(query)
data = cursor.fetchall()

# Get column names
columns = [desc[0] for desc in cursor.description]

# Display data in a table-like format
for row in data:
    print("\t".join(str(value) for value in row))

# Export data to a CSV file
csv_file_path = "employees_data.csv"
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(columns)
    
    # Write data
    csv_writer.writerows(data)

print(f"Data exported to CSV file: {csv_file_path}")

# Close MySQL connection
cursor.close()
connection.close()
