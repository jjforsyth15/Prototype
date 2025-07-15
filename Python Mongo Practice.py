from pymongo import MongoClient

uri = "mongodb+srv://jjforsyth15:ClassLink2025@cluster1.imnisby.mongodb.net/"
client = MongoClient(uri)

db = client["CLASSLINK"]
students = db["STUDENTS"]

students.insert_one({
    "firstName": "Alice",
    "lastName": "Smith"
})

for students in students.find():
    print(students)


