function validation() {
    var username = document.getElementById("admin_username");
    var password = document.getElementById("admin_password");

    if (username.value.trim() == "" || password.value.trim() == "") {
        alert("username or password is blank");
        return false;
    } else if (password.value.trim().length<8) {
        alert("password too short");
        return false;
    } else {
        true;
    }
}