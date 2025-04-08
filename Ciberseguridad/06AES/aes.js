var mensaje  = "pan con nutella";
var passoword = "qwertyuiqwertyuiqwertyui";
var cifrado = CryptoJS.AES.encrypt(mensaje, passoword);
var decifrado = CryptoJS.AES.decrypt(cifrado, passoword);

//para que se vea

document.getElementById("demo00").innerHTML = mensaje;
document.getElementById("demo01").innerHTML = cifrado;
document.getElementById("demo02").innerHTML = decifrado;
document.getElementById("demo03").innerHTML = decifrado.toString(CryptoJS.enc.Utf8);