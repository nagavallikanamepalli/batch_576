from fastapi import FastAPI

app = FastAPI(title="Valli")

students=[
    {"id":1,"name":"a","dept":"python"},
    {"id":2,"name":"b","dept":"java"},
    {"id":3,"name":"c","dept":"c++"},
    {"id":4,"name":"d","dept":"python"},
    {"id":5,"name":"e","dept":"java"}
]

# path parameters
@app.get("/students/{student_id}")
def get_student(student_id:int):
    print(student_id)
    print(type(student_id))
    for student in students:
        if student["id"]==student_id:
            return student
    return {"error":"Student not found"}
# if i give the dept name i get all the students in that dept
# query parameters  http://127.0.0.1:8000/students?dept=python
@app.get("/students")
def get_students(dept:str):
    r=[]
    for student in students:
        if student["dept"]==dept:
            r.append(student)
    return r
@app.get("/")
def home():
    return {"message": "Hello, World!"}
@app.get("/name")
def name():
    return {"name": "FastAPI Application"}