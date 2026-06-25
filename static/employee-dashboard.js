async function loadMyTasks() {

    try {

        const response = await fetch("/tasks/mytasks");

        const tasks = await response.json();

        console.log("TASKS RECEIVED:", tasks);

        const container =
        document.getElementById("employeeTasks");

        container.innerHTML = "";

        if(tasks.length === 0){

            container.innerHTML =
            "<h3>No Tasks Assigned</h3>";

            return;
        }

        tasks.forEach(task => {

            container.innerHTML += `

            <div class="task-card">

                <h3>${task.Task_name}</h3>

                <p>${task.Description}</p>

                <p>Deadline: ${task.Deadline}</p>

                <p>Status: ${task.Status}</p>

            </div>

            `;
        });

    }
    catch(error){

        console.log(error);

    }
}

loadMyTasks();