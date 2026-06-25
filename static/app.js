// =====================
// DASHBOARD STATS
// =====================

async function loadDashboardStats() {

    const activeProjects =
    document.getElementById(
        "activeProjects"
    );

    if(!activeProjects) return;

    const response =
    await fetch(
        "/projects/dashboard/stats"
    );

    const stats =
    await response.json();

    document.getElementById(
        "activeProjects"
    ).innerText =
    stats.active_projects;

    document.getElementById(
        "completedProjects"
    ).innerText =
    stats.completed_projects;

    document.getElementById(
        "totalTasks"
    ).innerText =
    stats.total_tasks;

    document.getElementById(
        "completedTasks"
    ).innerText =
    stats.completed_tasks;
}


// =====================
// RECENT PROJECTS
// =====================

async function loadRecentProjects() {

    const container =
    document.getElementById(
        "recentProjects"
    );

    if(!container) return;

    const response =
    await fetch(
        "/projects/recent"
    );

    const projects =
    await response.json();

    container.innerHTML = "";

    projects.forEach(project => {

        container.innerHTML += `

        <div class="project-card">

            <h3>

                ${project.Project_name}

            </h3>

            <p>

                Status :
                ${project.Project_Status}

            </p>

            <p>

                Deadline :
                ${project.Deadline}

            </p>

        </div>

        `;
    });
}


// =====================
// RECENT TASKS
// =====================

async function loadRecentTasks() {

    const container =
    document.getElementById(
        "recentTasks"
    );

    if(!container) return;

    const response =
    await fetch(
        "/tasks/recent"
    );

    const tasks =
    await response.json();

    container.innerHTML = "";

    tasks.forEach(task => {

        let badgeClass = "pending";

        if(
            task.Status === "Completed"
        ){

            badgeClass =
            "completed";
        }

        else if(
            task.Status === "In Progress"
        ){

            badgeClass =
            "progress";
        }

        container.innerHTML += `

        <div class="task-card">

            <h3>

                ${task.Task_name}

            </h3>

            <p>

                ${task.Description}

            </p>

            <span class="${badgeClass}">

                ${task.Status}

            </span>

        </div>

        `;
    });
}


// =====================
// USER PROFILE
// =====================

async function loadUser() {

    try {

        const response =
        await fetch(
            "/auth/me",
            {
                credentials: "include"
            }
        );

        const user =
        await response.json();

        console.log(user);

        document.getElementById(
            "username"
        ).innerText =
        user.username || "Admin";

        document.getElementById(
            "role"
        ).innerText =
        user.role || "User";

        document.getElementById(
            "userInitial"
        ).innerText =
        (user.username || "A")
        .charAt(0)
        .toUpperCase();

    }

    catch(error){

        console.log(error);
    }
}
async function buildSidebar(){

    const response =
    await fetch(
        "/auth/me"
    );

    const user =
    await response.json();

    const sidebar =
    document.querySelector(
        ".sidebar"
    );

    if(!sidebar) return;

    if(user.role==="Employee"){

        sidebar.innerHTML = `

        <h2>TaskFlow</h2>

        <a href="/employee-dashboard">

            Dashboard

        </a>

        <a href="/logout">

            Logout

        </a>

        `;
    }
}


// =====================
// LOAD EVERYTHING
// =====================

loadDashboardStats();
loadRecentProjects();
loadRecentTasks();
loadUser();
buildSidebar();