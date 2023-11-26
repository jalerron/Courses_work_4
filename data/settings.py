import os

DBdata = {
    "db_name": ["postgres", "course_work_5"],
    "db_user": "postgres",
    "db_password": os.getenv('DBPass'),
    "db_host": "localhost"
}
