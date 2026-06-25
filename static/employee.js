async function loadEmployeeTasks(){

    const userResponse =
    await fetch(
        "http://127.0.0.1:8000/auth/me"
    );

    const user =
    await userResponse.json();

    const response =
    await fetch(

        `http://127.0.0.1:8000/tasks/employee/${user.email}`

    );

    const tasks =
    await response.json();

    const container =
    document.getElementById(
        "employeeTasks"
    );

    container.innerHTML="";

    tasks.forEach(task=>{

        let badgeClass=
        "pending";

        if(
            task.Status==="Completed"
        ){
            badgeClass=
            "completed";
        }

        else if(
            task.Status==="In Progress"
        ){
            badgeClass=
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

            <p>

                Deadline:
                ${task.Deadline}

            </p>

            <span class="${badgeClass}">

                ${task.Status}

            </span>

            <br><br>

            <button
            onclick="updateStatus(
                ${task.Task_id},
                'In Progress'
            )">

                Start
            </button>

            <button
            onclick="updateStatus(
                ${task.Task_id},
                'Completed'
            )">

                Complete
            </button>

        </div>

        `;
    });
}

async function updateStatus(
    taskId,
    status
){

    await fetch(

        `http://127.0.0.1:8000/tasks/${taskId}?status=${status}`,

        {
            method:"PUT"
        }
    );

    loadEmployeeTasks();
}

loadEmployeeTasks();

if(data.role==="Admin"){

    window.location.href="/";

}
else{

    window.location.href=
    "/employee-dashboard";
}