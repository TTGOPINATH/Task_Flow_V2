const params =
new URLSearchParams(
    window.location.search
);

const projectId =
params.get("project_id");
let allTasks = [];

function toggleTaskForm() {

    const form =
    document.getElementById(
        "taskForm"
    );

    if (
        form.style.display === "none" ||
        form.style.display === ""
    ) {

        form.style.display = "block";

    } else {

        form.style.display = "none";
    }
}

async function loadTasks() {

    try {

        let response;

if(projectId){

    response =
    await fetch(
        `/tasks/project/${projectId}`
    );

}
else{

    response =
    await fetch("/tasks/");
}

        allTasks =
        await response.json();

        displayTasks(allTasks);

        document.getElementById(
            "taskCount"
        ).innerText =
        allTasks.length;

    } catch (error) {

        console.log(error);

        alert(
            "Unable to load tasks"
        );
    }
}

function displayTasks(tasks) {

    const pending =
    document.getElementById(
        "pendingTasks"
    );

    const progress =
    document.getElementById(
        "progressTasks"
    );

    const completed =
    document.getElementById(
        "completedTasks"
    );

    pending.innerHTML = "";
    progress.innerHTML = "";
    completed.innerHTML = "";

    tasks.forEach(task => {

        const html = `

        <div class="task-card">

            <h3>${task.Task_name}</h3>

            <p>${task.Description || ""}</p>

            <p>
                <b>Assigned To:</b>
                ${task.Assigned_to}
            </p>

            <p>
                <b>Deadline:</b>
                ${task.Deadline}
            </p>

            <p>
                <b>Status:</b>
                ${task.Status}
            </p>

            <div class="task-actions">

                <button onclick="updateTask(${task.Task_id}, 'Pending')">
                    Pending
                </button>

                <button onclick="updateTask(${task.Task_id}, 'In Progress')">
                    In Progress
                </button>

                <button onclick="updateTask(${task.Task_id}, 'Completed')">
                    Completed
                </button>

                <button onclick="deleteTask(${task.Task_id})">
                    Delete
                </button>

            </div>

        </div>

        <br>
        `;

        if (task.Status === "Pending") {

            pending.innerHTML += html;

        } else if (
            task.Status === "In Progress"
        ) {

            progress.innerHTML += html;

        } else {

            completed.innerHTML += html;
        }
    });
}

function searchTasks() {

    const search =
    document.getElementById(
        "searchTask"
    ).value.toLowerCase();

    const filtered =
    allTasks.filter(task =>

        task.Task_name
        .toLowerCase()
        .includes(search)

    );

    displayTasks(filtered);
}

async function updateTask(
    taskId,
    status
) {

    try {

        await fetch(

            `/tasks/${taskId}?status=${encodeURIComponent(status)}`,

            {
                method: "PUT"
            }
        );

        loadTasks();

    } catch (error) {

        console.log(error);
    }
}

async function deleteTask(
    taskId
) {

    const confirmDelete =
    confirm(
        "Delete this task?"
    );

    if (!confirmDelete) {

        return;
    }

    try {

        await fetch(

            `/tasks/${taskId}`,

            {
                method: "DELETE"
            }
        );

        loadTasks();

    } catch (error) {

        console.log(error);
    }
}

document
.getElementById(
    "createTaskForm"
)
.addEventListener(

    "submit",

    async function(e) {

        e.preventDefault();

        const data = {

            project_id:
            parseInt(
                document.getElementById(
                    "projectId"
                ).value
            ),

            task_name:
            document.getElementById(
                "taskName"
            ).value,

            description:
            document.getElementById(
                "description"
            ).value,

            assigned_by:
            document.getElementById(
                "assignedBy"
            ).value,

            assigned_to:
            document.getElementById(
                "assignedTo"
            ).value,

            deadline:
            document.getElementById(
                "deadline"
            ).value,

            status:
            document.getElementById(
                "status"
            ).value
        };

        try {

            const response =
            await fetch(

                "/tasks/",

                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                        "application/json"
                    },

                    body:
                    JSON.stringify(
                        data
                    )
                }
            );

            const result =
            await response.json();

            alert(
                result.message
            );

            document
            .getElementById(
                "createTaskForm"
            )
            .reset();

            loadTasks();

        } catch (error) {

            console.log(error);

            alert(
                "Task creation failed"
            );
        }
    }
);

async function editTask(taskId){

    const taskName =
    prompt("Task Name");

    const description =
    prompt("Description");

    const assignedBy =
    prompt("Assigned By");

    const assignedTo =
    prompt("Assigned To");

    const deadline =
    prompt("Deadline");

    const status =
    prompt(
        "Pending / In Progress / Completed"
    );

    const data = {

        project_id:0,

        task_name:taskName,

        description:description,

        assigned_by:assignedBy,

        assigned_to:assignedTo,

        deadline:deadline,

        status:status
    };

    await fetch(

        `/tasks/edit/${taskId}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(data)
        }
    );

    loadTasks();
}

loadTasks();