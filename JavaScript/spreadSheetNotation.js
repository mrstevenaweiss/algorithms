'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'getSpreadsheetNotation' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts LONG_INTEGER n as parameter.
 */

function getSpreadsheetNotation(variable) {
    var str = variable;
    var patt1 = /[a-zA-Z]/g;
    var patt2 = /[0-9]/g;
    var letters = str.match(patt1);
    var numbers = str.match(patt2);
    console.log(letters, numbers)

    let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let row = (numbers.join('') * 702) - 701

    if (letters.length < 2) {
        return row + alphabet.indexOf(letters[0])
    } else {
        let front_letter = alphabet.indexOf(letters[0])
        let back_letter = alphabet.indexOf(letters[1])
        return ((front_letter + 1) * 26) + row + back_letter

    }

}

getSpreadsheetNotation('2AA')


function main() {
