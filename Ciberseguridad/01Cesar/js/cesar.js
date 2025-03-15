// Obtener los elementos para cifrar
const desplazamiento = document.getElementById("desplazamiento");
const texto = document.getElementById("texto");
const textoCifrado = document.getElementById("cifrado");
const cifrarBtn = document.getElementById("cifrarBtn");


function cifrado() {
   
    const textoIngresado = texto.value;
    const valorDesplazamiento = parseInt(desplazamiento.value);

    textoCifrado.value = textoIngresado.split('').map(c => {
        let mayus = (c === c.toUpperCase());
        let valorEntero = c.toLowerCase().charCodeAt(0);
        
        
        if (valorEntero >= 97 && valorEntero <= 122) {
            
            if (valorEntero + valorDesplazamiento > 122) {
                valorEntero = 97 + (valorEntero - 122) + valorDesplazamiento - 1;
            } else {
                valorEntero = valorEntero + valorDesplazamiento;
            }
        }
    
        else if (c >= 'A' && c <= 'Z') {
            valorEntero = c.charCodeAt(0);
            if (valorEntero + valorDesplazamiento > 90) {
                valorEntero = 65 + (valorEntero - 90) + valorDesplazamiento - 1;
            } else {
                valorEntero = valorEntero + valorDesplazamiento;
            }
        } 
        
        else {
            return c;
        }

        
        let cifrado = String.fromCharCode(valorEntero);
        return mayus ? cifrado.toUpperCase() : cifrado;
    }).join('');
}


texto.addEventListener("keyup", cifrado);
desplazamiento.addEventListener("input", cifrado);
cifrarBtn.addEventListener("click", cifrado); 
