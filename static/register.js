document.getElementById("registerForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const data = {
    username: document.getElementById("username").value,
    user_email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    role: document.getElementById("role").value
};

    try {

        const response = await fetch("/auth/register", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        if (response.ok) {

            alert("Registration Successful");

            window.location.href = "/login";

        } else {

            alert(result.detail);
        }

    } catch (error) {

        console.log(error);

        alert("Registration Failed");
    }

});