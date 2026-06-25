from database.db import get_connection

def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    # Total Projects
    cursor.execute("""
        SELECT COUNT(*) AS total_projects
        FROM projects
        WHERE is_deleted = FALSE
    """)
    total_projects = cursor.fetchone()

    # Active Projects
    cursor.execute("""
        SELECT COUNT(*) AS active_projects
        FROM projects
        WHERE Project_Status='Active'
        AND is_deleted=FALSE
    """)
    active_projects = cursor.fetchone()

    # Completed Projects
    cursor.execute("""
        SELECT COUNT(*) AS completed_projects
        FROM projects
        WHERE Project_Status='Completed'
    """)
    completed_projects = cursor.fetchone()

    # Total Tasks
    cursor.execute("""
        SELECT COUNT(*) AS total_tasks
        FROM tasks
    """)
    total_tasks = cursor.fetchone()

    # Pending Tasks
    cursor.execute("""
        SELECT COUNT(*) AS pending_tasks
        FROM tasks
        WHERE Status='Pending'
    """)
    pending_tasks = cursor.fetchone()

    # In Progress Tasks
    cursor.execute("""
        SELECT COUNT(*) AS progress_tasks
        FROM tasks
        WHERE Status='In Progress'
    """)
    progress_tasks = cursor.fetchone()

    # Completed Tasks
    cursor.execute("""
        SELECT COUNT(*) AS completed_tasks
        FROM tasks
        WHERE Status='Completed'
    """)
    completed_tasks = cursor.fetchone()

    connection.close()

    return {

        "total_projects":
        total_projects["total_projects"],

        "active_projects":
        active_projects["active_projects"],

        "completed_projects":
        completed_projects["completed_projects"],

        "total_tasks":
        total_tasks["total_tasks"],

        "pending_tasks":
        pending_tasks["pending_tasks"],

        "progress_tasks":
        progress_tasks["progress_tasks"],

        "completed_tasks":
        completed_tasks["completed_tasks"]
    }