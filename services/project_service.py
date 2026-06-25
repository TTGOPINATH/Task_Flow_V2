from database.db import get_connection


# GET ACTIVE PROJECTS


def get_projects():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM projects
        WHERE Project_Status='Active'
        AND is_deleted=FALSE
        ORDER BY Project_id DESC
        """
    )

    projects = cursor.fetchall()

    connection.close()

    return projects


# CREATE PROJECT


def create_project(data):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
    """
    INSERT INTO projects(

        Project_name,
        Description,
        Created_on,
        Deadline

    )

    VALUES(%s,%s,%s,%s)
    """,

    (

        data.project_name,

        data.description,

        data.created_on,

        data.deadline

    )
    )

    connection.commit()

    connection.close()

    return {

        "message":
        "Project Created Successfully"
    }


# SOFT DELETE PROJECT


def delete_project(project_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE projects

        SET is_deleted=TRUE

        WHERE Project_id=%s
        """,

        (project_id,)
    )

    connection.commit()

    connection.close()

    return {

        "message":
        "Project Deleted Successfully"
    }


# COMPLETED PROJECTS


def get_completed_projects():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *

        FROM projects

        WHERE Project_Status='Completed'

        AND is_deleted=FALSE

        ORDER BY Project_id DESC
        """
    )

    projects = cursor.fetchall()

    connection.close()

    return projects


# UPDATE PROJECT STATUS


def update_project_status(
    project_id
):

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT Status

        FROM tasks

        WHERE Project_id=%s
        """,

        (project_id,)
    )

    tasks = cursor.fetchall()

    if len(tasks) == 0:

        status = "Active"

    elif all(

        task["Status"] == "Completed"

        for task in tasks

    ):

        status = "Completed"

    else:

        status = "Active"

    cursor.execute(
        """
        UPDATE projects

        SET Project_Status=%s

        WHERE Project_id=%s
        """,

        (
            status,
            project_id
        )
    )

    connection.commit()

    connection.close()


# PROJECT PROGRESS %

def get_project_progress(
    project_id
):

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT COUNT(*) AS total_tasks

        FROM tasks

        WHERE Project_id=%s
        """,

        (project_id,)
    )

    total = cursor.fetchone()

    cursor.execute(
        """
        SELECT COUNT(*) AS completed_tasks

        FROM tasks

        WHERE Project_id=%s

        AND Status='Completed'
        """,

        (project_id,)
    )

    completed = cursor.fetchone()

    connection.close()

    total_tasks = total["total_tasks"]

    completed_tasks = completed["completed_tasks"]

    if total_tasks == 0:

        return {
            "progress": 0
        }

    progress = int(

        (
            completed_tasks
            /
            total_tasks
        ) * 100

    )

    return {

        "progress":
        progress
    }


# DASHBOARD STATS


def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT COUNT(*) AS total_projects

        FROM projects

        WHERE Project_Status='Active'

        AND is_deleted=FALSE
        """
    )

    active_projects = cursor.fetchone()

    cursor.execute(
        """
        SELECT COUNT(*) AS total_projects

        FROM projects

        WHERE Project_Status='Completed'

        AND is_deleted=FALSE
        """
    )

    completed_projects = cursor.fetchone()

    cursor.execute(
        """
        SELECT COUNT(*) AS total_tasks

        FROM tasks
        """
    )

    total_tasks = cursor.fetchone()

    cursor.execute(
        """
        SELECT COUNT(*) AS completed_tasks

        FROM tasks

        WHERE Status='Completed'
        """
    )

    completed_tasks = cursor.fetchone()

    connection.close()

    return {

        "active_projects":
        active_projects["total_projects"],

        "completed_projects":
        completed_projects["total_projects"],

        "total_tasks":
        total_tasks["total_tasks"],

        "completed_tasks":
        completed_tasks["completed_tasks"]
    }


def update_project(project_id, data):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE projects

        SET

            Project_name=%s,
            Description=%s,
            Created_on=%s,
            Deadline=%s

        WHERE Project_id=%s
        """,
        (
            data.project_name,
            data.description,
            data.created_on,
            data.deadline,
            project_id,
        ),
    )

    connection.commit()

    connection.close()

    return {"message": "Project Updated Successfully"}
