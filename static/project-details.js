const params =
new URLSearchParams(
    window.location.search
);

const projectId =
params.get("id");

console.log(
    "Project ID:",
    projectId
);

let currentUser = null;

async function loadCurrentUser(){
const response =
await fetch(
    "/auth/me"
);

currentUser =
await response.json();


}

async function loadTasks(){
try{

    const response =
    await fetch(

        `/tasks/project/${projectId}`

    );

    const tasks =
    await response.json();

    const container =
    document.getElementById(
        "tasksContainer"
    );

    const count =
    document.getElementById(
        "taskCount"
    );

    container.innerHTML = "";

    count.innerText =
    tasks.length;

    tasks.forEach(task=>{

        let badgeClass =
        "pending";

        if(
            task.Status==="Completed"
        ){

            badgeClass =
            "completed";
        }

        else if(
            task.Status==="In Progress"
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

            <p>

                Assigned To:
                ${task.Assigned_to}

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
            onclick="completeTask(
                ${task.Task_id}
            )">

                Complete

            </button>

            <button
            onclick="deleteTask(
                ${task.Task_id}
            )">

                Delete

            </button>

        </div>
        `;
    });


}

catch(error){

    console.log(error);

    alert(
        "Unable to load tasks"
    );

}

}

function showTaskForm(){

const form =
document.getElementById(
    "taskForm"
);

form.style.display =

form.style.display === "none"

? "block"

: "none";


}

document
.getElementById(
"createTaskForm"
)
.addEventListener(
"submit",

async function(e){

    e.preventDefault();

    const taskData = {

    project_id: parseInt(projectId),

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
    "Pending"
};

console.log(taskData);

   const response = await fetch("/tasks/",{
    method:"POST",
    headers:{
        "Content-Type":"application/json"
    },
    body:JSON.stringify(taskData)
});

const result = await response.json();

console.log(result);

    document
    .getElementById(
        "createTaskForm"
    )
    .reset();

    loadTasks();

    loadProgress();


}

);

async function completeTask(
taskId
){
await fetch(

    `/tasks/${taskId}?status=Completed`,

    {
        method:"PUT"
    }
);

loadTasks();

loadProgress();


}

async function deleteTask(
taskId
){
if(
    !confirm(
        "Delete this task?"
    )
){

    return;
}

await fetch(

    `/tasks/${taskId}`,

    {
        method:"DELETE"
    }
);

loadTasks();

loadProgress();


}

async function loadProgress(){
const response =
await fetch(

    `/projects/progress/${projectId}`

);

const data =
await response.json();

document
.getElementById(
    "progressText"
)
.innerText =
data.progress + "%";

document
.getElementById(
    "progressFill"
)
.style.width =
data.progress + "%";


}

async function uploadFile(
taskId,
file
){
const formData =
new FormData();

formData.append(
    "file",
    file
);

await fetch(

    `/attachments/${taskId}`,

    {

        method:"POST",

        body:formData
    }
);

alert(
    "File Uploaded Successfully"
);


}

async function loadAttachments(
taskId
){
const response =
await fetch(

    `/attachments/${taskId}`

);

const files =
await response.json();

let html = "";

files.forEach(file=>{

    html += `

    <a
    href="/${file.File_path}"
    target="_blank">

        ${file.File_name}

    </a>

    <br>
    `;
});

return html;


}

async function init(){
await loadCurrentUser();

loadTasks();

loadProgress();


}

init();
