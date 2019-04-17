

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function caseCheck(letter, otherWord) {
  if (letter == letter.toUpperCase()) {
    return capitalizeFirstLetter(otherWord);
  }
  return otherWord;
}

function myReplace(str, before, after) {

  let n = str.indexOf(before);
  let letter = str[n]
  let change = caseCheck(letter, after)
  
  let newStr = str.replace(before, change);

  // console.log(newStr);
  return newStr;
}

myReplace("A quick brown fox Jumped over the lazy dog", "Jumped", "leaped");
