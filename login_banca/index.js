let docTitle = document.title;
window.addEventListener("blur",()=>{
    document.title = "torna qui;(";
});

window.addEventListener("focus",()=>{
return
});



console.log("script ok");



function generateOTP(){
    var digits = '724942';   // '0123456789'
    let OTP='';
    for (let i =0; i<6; i++){
        OTP +=digits[Math.floor(Math.random()*10)]
    }
    return OTP
}

generateOTP() // '724942'
generateOTP()// '761294'


function login() {
    // Ottenere i valori inseriti dall'utente
    const username = document.getElementById("Username").value;
    const password = document.getElementById("Password").value;
    
    // Verificare se i valori inseriti sono validi
    if (username === "" || password === "") {
      alert("Inserisci un username e una password validi");
      return false;
    }
    
    // Effettuare la chiamata AJAX per verificare le credenziali dell'utente
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/login");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        if (response.success) {
          // L'utente è autenticato, effettua il redirect alla homepage
          window.location.href = "/homepage";
        } else {
          alert("Credenziali errate");
        }
      }
    };
    xhr.send(JSON.stringify({username: username, password: password}));
  }
  
