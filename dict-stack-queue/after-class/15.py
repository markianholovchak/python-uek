import json
student = {
    "name": "Rajesh",
    "surname": "Doe",  
    "gender": "Male",
    "country": "India",
    "age": 21,
    "married": False,
    "univeristy": "MIT",
    "faculty": "Informatics",
    "hasScolarship": True,
    "yearOfStudies": 2,
    "points": {"calculus": 5, "programming": 4.5, "physics": 4, "PE": 5, "geometry": 5}
}

with open('student.json', "w") as f:
    f.write(json.dumps([student], indent=2))