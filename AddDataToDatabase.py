import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recongnition-system-default-rtdb.firebaseio.com"
})
ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassanq",
            "subject": "Electronics",
            "attendance": "",
            "starting_year": 2019,
            "total_attendance": 7,
            "grade": "A",
            "year": 4,
            "last_attendance_time": "2023-05-15 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "subject": "Economics",
            "starting_year": 2019,
            "total_attendance": 12,
            "grade": "AB",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "subject": "Physics",
            "starting_year": 2019,
            "total_attendance": 7,
            "grade": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "Photo":
    {
            "name": "Nikhil Rawat",
            "subject": "Maths",
            "starting_year": 2019,
            "total_attendance": 8,
            "grade": "A+",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
    }
}

for key, value in data.items():
    ref.child(key).set(value)