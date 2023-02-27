let docTitle = document.title;
window.addEventListener("blur",()=>{
    document.title = "torna qui;(";
});

window.addEventListener("focus",()=>{
return
});



console.log("script ok");

//eseguo un chiamata rest api sito unicredit
fetch('/page', {
    // assuming we're on https://javascript.info
    // we can set any Referer header, but only within the current origin
    referrer: "https://www.unicredit.it/it/privati.html"
  });

document.getElementById('submit').onclick = function (e) {
 
    var error = false;

    if(login('username')) error = true;
    if(login('password')) error = true;

    if(error) e.preventDefault();

}

function login(id) {

if(document.getElementById(id).value == '')
{
document.getElementById('error_' + id).innerHTML = 'Campo obbligatorio';
return true;
}
else
{
document.getElementById('error_' + id).innerHTML = '';
return false;
}

}
