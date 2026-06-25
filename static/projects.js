function showProjectForm() {

    const form =
    document.getElementById(
        "projectForm"
    );

    if (
        form.style.display === "none" ||
        form.style.display === ""
    ) {

        form.style.display =
        "block";

    } else {

        form.style.display =
        "none";
    }
}

async function loadProjects() {

    try {

        const response =
        await fetch(
            "/projects/"
        );

        const projects =
        await response.json();

        const container =
        document.getElementById(
            "projectsContainer"
        );

        const count =
        document.getElementById(
            "projectCount"
        );

        container.innerHTML = "";

        if (count) {

            count.innerText =
            projects.length;
        }

        projects.forEach(project => {

            container.innerHTML += `

            <div class="project-card">

                <h3>
                    ${project.Project_name}
                </h3>

                <p>
                    ${project.Description || ""}
                </p>

                <p>
                    <strong>Status:</strong>
                    ${project.Project_Status}
                </p>

                <p>
                    <strong>Created:</strong>
                    ${project.Created_on}
                </p>

                <p>
                    <strong>Deadline:</strong>
                    ${project.Deadline}
                </p>

                <br>

                <button
                onclick="viewProject(${project.Project_id})">

                    View Tasks

                </button>

                <button
                onclick="deleteProject(${project.Project_id})">

                    Delete

                </button>

            </div>

            <br>
            `;
        });

    }

    catch(error) {

        console.log(error);

        alert(
            "Unable to load projects"
        );
    }
}

async function loadCompletedProjects() {

    try {

        const response =
        await fetch(
            "/projects/completed"
        );

        const projects =
        await response.json();

        const container =
        document.getElementById(
            "completedProjects"
        );

        container.innerHTML = "";

        projects.forEach(project => {

            container.innerHTML += `

            <div class="project-card">

                <h3>
                    ${project.Project_name}
                </h3>

                <span class="completed">

                    Completed

                </span>

            </div>

            <br>
            `;
        });

    }

    catch(error) {

        console.log(error);
    }
}

document
.getElementById(
    "createProjectForm"
)
.addEventListener(

    "submit",

    async function(e){

        e.preventDefault();

        const data = {

    project_id:
    parseInt(
        document.getElementById(
            "projectId"
        ).value
    ),

    project_name:
    document.getElementById(
        "projectName"
    ).value,

    description:
    document.getElementById(
        "description"
    ).value,

    created_on:
    document.getElementById(
        "createdOn"
    ).value,

    deadline:
    document.getElementById(
        "deadline"
    ).value
};

        try {

            const response =
            await fetch(

                "/projects/",

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

            if (!response.ok) {

                throw new Error(

                    result.detail ||

                    "Project creation failed"
                );
            }

            alert(
                result.message ||
                "Project Created Successfully"
            );

            document
            .getElementById(
                "createProjectForm"
            )
            .reset();

            document
            .getElementById(
                "projectForm"
            )
            .style.display =
            "none";

            loadProjects();

            loadCompletedProjects();

        }

        catch(error) {

            console.log(error);

            alert(
                error.message
            );
        }
    }
);

async function deleteProject(
    projectId
) {

    const confirmDelete =
    confirm(
        "Delete this project?"
    );

    if (!confirmDelete) {

        return;
    }

    try {

        const response =
        await fetch(

            `/projects/${projectId}`,

            {

                method:
                "DELETE"
            }
        );

        const result =
        await response.json();

        alert(
            result.message
        );

        loadProjects();

        loadCompletedProjects();

    }

    catch(error) {

        console.log(error);

        alert(
            "Unable to delete project"
        );
    }
}

function viewProject(projectId) {
    window.location.href =
    `/tasks-page?project_id=${projectId}`;
}

window.onload = function() {

    loadProjects();

    loadCompletedProjects();
};

async function editProject(projectId){

    const projectName =
    prompt("Project Name");

    const description =
    prompt("Description");

    const createdOn =
    prompt("Created Date");

    const deadline =
    prompt("Deadline");

    const data = {

        project_name: projectName,

        description: description,

        created_on: createdOn,

        deadline: deadline
    };

    await fetch(

        `/projects/${projectId}`,

        {

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(data)
        }
    );

    loadProjects();
}