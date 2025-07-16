#import modules & MongoDB
from student import Student
from course import Course
from pymongo import MongoClient

#Set up MongoDB for use
uri = "mongodb+srv://jjforsyth15:ClassLink2025@cluster1.imnisby.mongodb.net/"
client = MongoClient(uri)

db = client["CLASSLINK"]
students = db["STUDENTS"]
courses = db["COURSES"]

#Main
def main():
    # #Just practice examples
    # james = Student("James", "Madison")
    # print(james)

    # history = Course("History 101", "1024")

    # print(students.find_one({"firstName": james.firstName, "lastName": james.lastName}))

    # print(history)
    # print(courses.find_one({"courseName": history.courseName, "courseNumber": history.courseNumber}))

    #Menu loop
    while True:
        print("\n=== Menu ===\n1. Make new student\n2. Search student by first name\n3. Make new course\n4. Search course by number\n5. End program")
        choice = input("Choose an option: ")
        
        #If user picks 1 - make a new student to add to database
        if choice == "1":
            print("1")
            first = input("Enter first name of student: ")
            last = input("Enter last name of student: ")
            user_name = input("Enter a username: ")
            password = input("Enter a password: ")
            new_student = Student(first, last, user_name, password)
            print("New student has been made: ", 
                  students.find_one({"firstName": first, "lastName": last}))
        
        #If user picks 2 - search for a student by first name
        elif choice == "2":
            print("2")

            searchName = input("Enter first name of student: ")
            results = students.find({"firstName": {"$regex":searchName}})
            found = False
            for student in results:
                print(student)             
                found = True

            if not found:
                print("No student found")

        #If user picks 3 - make a new course to add to database
        elif choice =="3": 
            print("3")
            course_name = input("Enter course name: ")
            course_num = input("Enter course number: ")
            new_course = Course(course_name, course_num)
            print("New course has been made: ", 
                  courses.find_one({"courseName": course_name, "courseNumber": course_num}))
            
        #If user picks 4 - search by course number
        elif choice == "4":
            print("")

            search_num = input("Enter course number: ")
            results = courses.find({"courseNumber": search_num})
            found = False

            for course in results:
                print(course)
                found = True
            
            if not found:
                print("No course found")

        # If user picks 5 - end program
        elif choice =="5":
            print("Ending program")
            break
        else:
            print("Invalid input. Try again")


main()

