from pymongo import MongoClient

uri = "mongodb+srv://jjforsyth15:ClassLink2025@cluster1.imnisby.mongodb.net/"
client = MongoClient(uri)

db = client["CLASSLINK"]
students = db["STUDENTS"]
courses = db["COURSES"]

class Student: 
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
        self.fullName = first + " " + last
        self.myCourses = []

        if students.find_one({"firstName": first, "lastName": last}):
            print("Student already exists")
        else:
            students.insert_one({
                "firstName": first,
                "lastName": last
            })

    def __str__(self):
        return f"Student: {self.fullName}"
    
    def to_dict(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName
        }
    
    def add_course(self, courseToAdd):
        from course import Course   
        self.myCourses.append(courseToAdd)


