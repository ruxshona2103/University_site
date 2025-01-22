from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

def get_data_from_table(table_name):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        return dictfetchall(cursor)


def get_kafedra_with_faculty():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT adminapp_kafedra.*, adminapp_faculty.name AS faculty_name
            FROM adminapp_kafedra
            LEFT JOIN adminapp_faculty ON adminapp_kafedra.faculty_id = adminapp_faculty.id
        """)
        return dictfetchall(cursor)


def get_teachers_with_subject():
    with closing(connection.cursor) as cursor:
        cursor.execute("""
            SELECT adminapp_teachers.*, adminapp_subjects.name AS subjects_name
            FROM adminapp_teachers
            LEFT JOIN adminapp_subject ON adminapp_teachers.subjects_id = adminapp_subjects.id
            """)
        return dictfetchall(cursor)


def get_groups_with_details():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
                SELECT adminapp_groups.*, adminapp_kafedra.name AS kafedra_name, 
                CONCAT(adminapp_teachers.first_name, " ", adminapp_teachers.last_name) AS mentor_fullname
                FROM adminapp_groups 
                LEFT JOIN adminapp_kafedra ON adminapp_groups.kafedra_id = adminapp_kafedra.id
                LEFT JOIN adminapp_teachers ON adminapp_groups.mentor_id = adminapp_teachers.id """)
        return dictfetchall(cursor)


def get_teacher_with_details():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT adminapp_teachers.*, adminapp_subjects.name AS subject_name, adminapp_kafedra.name AS kafedra_name
            FROM adminapp_teachers
            LEFT JOIN adminapp_subjects ON adminapp_teachers.subject_id = adminapp_subjects.id
            LEFT JOIN adminapp_kafedra ON adminapp_teachers.kafedra_id_id = adminapp_kafedra.id""")
        return dictfetchall(cursor)


def get_group_with_details():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT 
                adminapp_groups.*,
                adminapp_kafedra.name AS kafedra_name, 
                CONCAT(adminapp_teachers.first_name, ' ', adminapp_teachers.last_name) AS mentor_fullname
            FROM 
                adminapp_groups
            LEFT JOIN
                adminapp_kafedra ON adminapp_groups.kafedra_id = adminapp_kafedra.id
            LEFT JOIN
                adminapp_teachers ON adminapp_groups.mentor_id = adminapp_teachers.id 
        """)
        return dictfetchall(cursor)


def get_students_with_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT adminapp_students.*, adminapp_groups.name AS group_name
            FROM adminapp_students
            LEFT JOIN adminapp_groups ON adminapp_students.group_id = adminapp_groups.id""")
        return dictfetchall(cursor)
