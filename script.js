// alert("Hola mundo")
console.log("Holaaaaaaaaaaaaaaaaaaa")

let number = 5
let texto = "Hola"
number = number + 1
console.log(number)

let frutas = ["manzana", "naranja", "personalbar", "platano"]

console.log(frutas)

const elementoP = document.getElementById("mitexto")
console.log(elementoP)

elementoP.innerText = number.toString()

function aumentarContador() {
    const elementoP = document.getElementById("mitexto")
    let number = elementoP.innerText
    number++
    elementoP.innerText = number
}

function crearCeldaHeader(text) {
    return "<th>" + text + "</th>"
}

function crearCeldaDatos(text) {
    return "<td>" + text + "</td>"
}

const tabla = document.getElementById("tabla")
console.log(tabla)

let celdas = "<tr>"
celdas = celdas + "<th> Nombre </th>"
celdas += "<th> Apellidos </th>"
celdas += "<th> DNI </th>"
celdas += "</tr>"

let nombres = ["Juanmi", ""]

for (let index = 0; index <= 10; index++) {
    console.log("El indice en esta iteración es ", index)
    celdas += "<tr>"
    celdas += crearCeldaDatos("Juanmi")
    celdas += crearCeldaDatos("Garcia")
    celdas += crearCeldaDatos("77134321K")
    celdas += "</tr>"
    
}

tabla.innerHTML = celdas

