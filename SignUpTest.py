#import modules & MongoDB
from student import Student
from course import Course
from pymongo import MongoClient
import bcrypt

#Set up MongoDB for use
uri = "mongodb+srv://jjforsyth15:ClassLink2025@cluster1.imnisby.mongodb.net/"
client = MongoClient(uri)

db = client["CLASSLINK"]
students = db["STUDENTS"]
courses = db["COURSES"]


def SignUpTest(): 
    while True:
        print("=== Menu ===")
        print("1. Sign Up\n2. Login\n3. End Program")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            print("Signing Up\n-------")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            user_name = input("Enter a username: ")
            while True:
                if(students.find_one({"userName": user_name})):
                    user_name = input("Username already exists. Enter another username: ")
                else:
                    break
            password = input("Enter a password:")

            new_student = Student(first_name, last_name, user_name, password)
            print("New student login created: ",
                  students.find_one({"userName": user_name})["userName"])
            print("Log in to access account")
            
        elif choice == "2": 
            print("Logging in\n-------")
            user_name = input("Enter username: ")
            while True:
                if not (students.find_one({"userName": user_name})):
                    user_name = input("Username does not exist. Enter again: ")
                else:
                    break
            user = students.find_one({"userName": user_name})
            stored_hash = user["passwordHashed"]

            password = input("Enter password: ")
            
            while True: 
                if bcrypt.checkpw(password.encode(), stored_hash):
                    print("Login successful. Welcome, ", students.find_one({"userName": user_name},
                                                                        {"firstName": 1, "_id": 0})["firstName"])
                    break
                else:
                    password = input("Incorrect password try again: ")


        elif choice == "3":
            print("Ending Program.")
            break
        
        else:
            print("Invalid input. Try again.")


        
SignUpTest()

