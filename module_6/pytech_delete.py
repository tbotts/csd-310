# Title: pytech_delete.py
# Author: Tara Botts
# Date: September 5, 2021
# Description: Assignment 6.3

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

# Test document 
test_doc = {
    "student_id": "1010",
    "first_name": "Black",
    "last_name": "Panther"
}

# insert the test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# call the find_one() method by student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")