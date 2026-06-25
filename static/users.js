async function loadUsers(){
    try{
        const response = await fetch("/users/");
        const users = await response.json();

        const table = document.getElementById("usersTable");
        const count = document.getElementById("userCount");

        table.innerHTML = "";
        count.innerText = users.length;

        users.forEach(user => {
            table.innerHTML += `<tr><td>${user.User_id}</td><td>${user.Username}</td><td>${user.Mail}</td><td>${user.Role}</td></tr>`;
        });
    } catch(error){
        console.log(error);
        alert("Unable to load users");
    }
}

loadUsers();
