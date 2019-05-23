
let cipher = {
    "A": "N",
    "B": "O", 
    "C": "P", 
    "D": "Q", 
    "E": "R",
    "F": "S", 
    "G": "T",
    "H": "U", 
    "I": "V", 
    "J": "W", 
    "K": "X", 
    "L": "Y", 
    "M": "Z", 
    "N": "A", 
    "O": "B", 
    "P": "C", 
    "Q": "D", 
    "R": "E", 
    "S": "F",
    "T": "G", 
    "U": "H", 
    "V": "I", 
    "W": "J",
    "X": "K",
    "Y": "L",
    "Z": "M", 
    " ": " "
}

function isLetter(str) {
  return str.length === 1 && str.match(/[a-z]/i);
}

function rot13(word) { // LBH QVQ VG!
  let newStr = "";
  let res = word.split("");

  for (letter in res) {
    let key = res[letter]
    newStr += cipher[key]
  }
  return newStr;
}

// Change the inputs below to test
rot13("SERR PBQR PNZC")
