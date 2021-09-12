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

# Student documents to insert

# Student 1 
Captain = {
    "student_id": "1007",
    "first_name": "Captain",
    "last_name": "America",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "August 2, 2021",
            "end_date": "October 5, 2021",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Professor Donoho",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations & Forensics",
                    "instructor": "Professor Waldrep",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Student 2
Black = {
    "student_id": "1008",
    "first_name": "Black",
    "last_name": "Widow",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.0",
            "start_date": "August 2, 2021",
            "end_date": "October 5, 2021",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Professor Donoho",
                    "grade": "B+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations & Forensics",
                    "instructor": "Professor Waldrep",
                    "grade": "B-"
                }
            ]
        }
    ]
}

# Student 3
Baby = {
    "student_id": "1009",
    "first_name": "Baby",
    "last_name": "Yoda",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "2.0",
            "start_date": "August 2, 2021",
            "end_date": "October 5, 2021",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Professor Donoho",
                    "grade": "C"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations & Forensics",
                    "instructor": "Professor Waldrep",
                    "grade": "C"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
Captain_student_id = students.insert_one(Captain).inserted_id
print("  Inserted student record Captain America into the students collection with document_id " + str(Captain_student_id))

Black_student_id = students.insert_one(Black).inserted_id
print("  Inserted student record Black Widow into the students collection with document_id " + str(Black_student_id))

Baby_student_id = students.insert_one(Baby).inserted_id
print("  Inserted student record Baby Yoda into the students collection with document_id " + str(Baby_student_id))

input("\n\n End of program, press any key to exit... ")
