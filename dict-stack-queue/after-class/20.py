import json

with open("students.json") as f:
    students = json.load(f)
   
with open("limited.json", "w") as f:
    limitedInfoStudents = []
    for student in students:
        limitedInfo = {
            "student_id": student["student_id"],
            "first_name": student["first_name"],
            "last_name": student["last_name"],
        }
        limitedInfoStudents.append(limitedInfo)
    f.write(f"{json.dumps(limitedInfoStudents, indent=2)}\n")