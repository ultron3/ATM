let docTitle = document.title;
window.addEventListener("blur",()=>{
    document.title = "torna qui;(";
});

window.addEventListener("focus",()=>{
return
});



console.log("script ok");



function generateOTP(){
    var digits = '0123456789';
    let OTP='';
    for (let i =0; i<6; i++){
        OTP +=digits[Math.floor(Math.random()*10)]
    }
    return OTP
}

generateOTP() // '724942'
generateOTP()// '761294'
