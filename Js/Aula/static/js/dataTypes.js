// Tipos de dados
/*
    number -> Valor numérico
    string -> Caracteres
    boolean -> Verdadeiro ou Falso
    null -> Vazio (none)
    undefined -> Quando não é atribuido um valor
*/

// Variaveis
// var valor = 1 Não utilizar
let number = 1;
let string = "Hello, world!";
let boolean = true;
let nothing = null;
let notDefined;

console.log(typeof number);
console.log(typeof string);
console.log(typeof boolean);
console.log(typeof nothing);
console.log(typeof notDefined);


// type casting
console.log(typeof String(number))
console.log(Number('10.a'))
console.log(+'10.a')

const ANO_ATUAL = 2023;
ANO_ATUAL = 2024;
console.log(ANO_ATUAL);