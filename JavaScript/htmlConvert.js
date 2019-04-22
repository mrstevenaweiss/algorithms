

function change(letter) {
  if (letter == '&') {
    return '&​amp;' 
  } else if (letter == '<' ) {
    return '&​lt;'
  } else if (letter == '>' ) {
    return '&​gt;'
  } else if (letter == '"') {
    return '&​quot;';
  } else if (letter == "'") {
    return '&​apos;'
  } else {
    return letter
  }
}

function convertHTML(str) {
  let newStr = ''  
  let letters = str.split('');

  for (let i = 0; i < letters.length; i++) {
    newStr += change(letters[i])
  }
  console.log(newStr)
  return newStr;
}


function convertHTML(str) {
//Chaining of replace method with different arguments
  str = str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,"&apos;");
return str;
}

convertHTML('Dolce & Gabbana');
