# Title: mongodb_test.py
# Author: Tara Botts
# Date: August 29, 2021
# Description: Assignment 5.3

# Import statements
from pymongo import MongoClient
import certifi

if __name__ == "__main__":
    # MongoDB connection string
    url = "mongodb+srv://admin:admin@cluster0.hyosd.mongodb.net/pytech"
    
    # Connect to the MongoDB cluster
    client = MongoClient(url, tlsCAFile=certifi.where())
    
    # Connect pytech database
    db = client.pytech

    # Get the students collection 
    students = db.students

# Find all students in the collection 
student_list = students.find({})

# Display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Find document by student_id
Captain = students.find_one({"student_id": "1007"})

# Output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + Captain["student_id"] + "\n  First Name: " + Captain["first_name"] + "\n  Last Name: " + Captain["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")