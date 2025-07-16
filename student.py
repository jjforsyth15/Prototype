from pymongo import MongoClient
import bcrypt

uri = "mongodb+srv://jjforsyth15:ClassLink2025@cluster1.imnisby.mongodb.net/"
client = MongoClient(uri)

db = client["CLASSLINK"]
students = db["STUDENTS"]
courses = db["COURSES"]

class Student: 
    def __init__(self, first, last, username, password):
        self.firstName = first
        self.lastName = last
        # self.fullName = first + " " + last
        # self.myCourses = course if courses is not None else []
        self.userName = username
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        if students.find_one({"firstName": first, "lastName": last}):
            print("Student already exists")
        else:
            students.insert_one({
                "firstName": first,
                "lastName": last,
                "userName": username,
                "passwordHashed": hashed,
                # "courses": course
            })

    def __str__(self):
        return f"Student: {self.firstName} {self.lastName}, Courses: {', '.join(self.myCoursesourses)}"
    
    # def to_dict(self):
    #     return {
    #         "firstName": self.firstName,
    #         "lastName": self.lastName,
    #         "courses": self.myCourses
    #     }
    
    def add_course(self, courseToAdd):
        from course import Course   
        self.myCourses.append(courseToAdd)
        result = students.update_one(
            {"firstName": self.firstName, "lastName": self.lastName},
            {"$push": {"courses": courseToAdd}}
        )
        print("Added course: ")
        print(courseToAdd)



