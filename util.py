
def student_function():
    students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 92},
    {"name": "Eva", "grade": 88},
    {"name": "Frank", "grade": 80},
    {"name": "Grace", "grade": 95},
    {"name": "Helen", "grade": 87},
    {"name": "Ivan", "grade": 83},
    {"name": "Jane", "grade": 91}
]

    j = 0
    for i in range(len(students)):
        if students[i]["grade"] > 85:
            print(students[i]["name"], students[i]["grade"])
            j += 1
        i+1
    print(j)
