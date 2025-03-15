// Obtener los elementos para cifrar
const desplazamiento = document.getElementById("desplazamiento");
const texto = document.getElementById("texto");
const textoCifrado = document.getElementById("cifrado");
const cifrarBtn = document.getElementById("cifrarBtn");

// Función que se encarga del algoritmo de César
function cifrado() {
    // Obtener el texto ingresado para cifrar
    const textoIngresado = texto.value;
    const valorDesplazamiento = parseInt(desplazamiento.value);

    textoCifrado.value = textoIngresado.split('').map(c => {
        let mayus = (c === c.toUpperCase());
        let valorEntero = c.toLowerCase().charCodeAt(0);
        
        // Si el carácter es una letra (a-z)
        if (valorEntero >= 97 && valorEntero <= 122) {
            // Cifrar la letra minúscula
            if (valorEntero + valorDesplazamiento > 122) {
                valorEntero = 97 + (valorEntero - 122) + valorDesplazamiento - 1;
            } else {
                valorEntero = valorEntero + valorDesplazamiento;
            }
        }
        // Si el carácter es una letra mayúscula (A-Z)
        else if (c >= 'A' && c <= 'Z') {
            valorEntero = c.charCodeAt(0);
            if (valorEntero + valorDesplazamiento > 90) {
                valorEntero = 65 + (valorEntero - 90) + valorDesplazamiento - 1;
            } else {
                valorEntero = valorEntero + valorDesplazamiento;
            }
        } 
        // Si no es una letra, no modificarlo
        else {
            return c;
        }

        // Convertir el valor numérico a carácter
        let cifrado = String.fromCharCode(valorEntero);
        return mayus ? cifrado.toUpperCase() : cifrado;
    }).join('');
}

// Asociar el evento de los inputs y el botón
texto.addEventListener("keyup", cifrado);
desplazamiento.addEventListener("input", cifrado);
cifrarBtn.addEventListener("click", cifrado); // Evento para el botón "Cifrar"
