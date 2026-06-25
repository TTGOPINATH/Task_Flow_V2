document.getElementById("loginForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const formData = new FormData();

    formData.append(
        "email",
        document.getElementById("email").value
    );

    formData.append(
        "password",
        document.getElementById("password").value
    );

    const response = await fetch(
        "/auth/login",
        {
            method: "POST",
            body: formData,
            credentials: "include"
        }
    );

    const data = await response.json();

    if(response.ok){

        if(data.role === "Admin"){

            window.location.href = "/";

        }else{

            window.location.href =
            "/employee-dashboard";
        }

    }else{

        alert(JSON.stringify(data));
    }

});