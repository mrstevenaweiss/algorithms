

function vowel(letter) {
  if (letter === 'a'|| letter === 'e' || letter === 'i' || letter === 'o' || letter === 'u' ) {
    return true
  } 
  return letter;
}

function translatePigLatin(str) {
  let cluster = ''
  
  for (let i = 0; i < str.length; i++) {  
    let letter = str[i]
    let checker = vowel(letter)

    if (checker == true && i == 0) {
      return str.slice(i, str.length) + 'w' + 'ay'
    } 
    else {
      if ( checker == true )  {
        return str.slice(i, str.length) + cluster + 'ay'
      } else {
        cluster = cluster + checker
      }
    }
  }
  return str + 'ay';
}

console.log(translatePigLatin("bdfghql"))


