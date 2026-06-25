from database.db import get_connection
from services.project_service import update_project_status
from services.email_service import send_task_email

def get_tasks():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM tasks
        ORDER BY Task_id DESC
        """
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks


def get_completed_tasks():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE Status='Completed'
        ORDER BY Task_id DESC
        """
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks


def create_task(data):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(

            Project_id,
            Task_name,
            Description,
            Assigned_by,
            Assigned_to,
            Deadline,
            Status

        )

        VALUES(
            %s,%s,%s,%s,%s,%s,%s
        )
        """,

        (

            data.project_id,
            data.task_name,
            data.description,
            data.assigned_by,
            data.assigned_to,
            data.deadline,
            data.status

        )
    )

    connection.commit()

    connection.close()

    try:

        send_task_email(

            data.assigned_to,
            data.task_name,
            data.project_id,
            data.deadline

        )

    except Exception as e:

        print("Email Error:", e)

    update_project_status(
        data.project_id
    )

    return {

        "message":
        "Task Created Successfully"
    }


def delete_task(task_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT Project_id
        FROM tasks
        WHERE Task_id=%s
        """,

        (task_id,)
    )

    project = cursor.fetchone()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE Task_id=%s
        """,

        (task_id,)
    )

    connection.commit()

    connection.close()

    if project:

        update_project_status(
            project[0]
        )

    return {

        "message":
        "Task Deleted Successfully"
    }


def update_task_status(
task_id,
status
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET Status=%s
        WHERE Task_id=%s
        """,

        (
            status,
            task_id
        )
    )

    cursor.execute(
        """
        SELECT Project_id
        FROM tasks
        WHERE Task_id=%s
        """,

        (task_id,)
    )

    project = cursor.fetchone()

    connection.commit()

    connection.close()

    if project:

        update_project_status(
            project[0]
        )

    return {

        "message":
        "Task Updated Successfully"
    }


def get_tasks_by_project(
project_id
):


    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE Project_id=%s
        ORDER BY Task_id DESC
        """,

        (project_id,)
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def get_tasks_by_employee(
email
):

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE Assigned_to=%s
        ORDER BY Task_id DESC
        """,

        (email,)
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks

def get_recent_tasks():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM tasks
        ORDER BY Task_id DESC
        LIMIT 5
        """
    )

    tasks = cursor.fetchall()

    connection.close()

    return tasks


def edit_task(task_id, data):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks

        SET

            Task_name=%s,
            Description=%s,
            Assigned_by=%s,
            Assigned_to=%s,
            Deadline=%s,
            Status=%s

        WHERE Task_id=%s
        """,
        (
            data.task_name,
            data.description,
            data.assigned_by,
            data.assigned_to,
            data.deadline,
            data.status,
            task_id,
        ),
    )

    connection.commit()

    connection.close()

    return {"message": "Task Updated Successfully"}
