

// Find the missing letter in a string input

function fearNotLetter(str) {
  let abc = "abcdefghijklmnopqrstuvwxyz";;
  let front = abc.indexOf(str[0]);
  let end = abc.indexOf(str[str.length-1]);
  let slicedAbc = abc.slice(front, end+1)
  let missing = undefined;
  
  for (let i = 0; i <= slicedAbc.length; i++) {
    console.log(i, slicedAbc[i], str[i])
    if (slicedAbc[i] !== str[i]) {
      console.log(i, 'inside', slicedAbc[i])
      missing = slicedAbc[i]   
      break;
    }
  
  }
  
  return missing;
}

fearNotLetter("bcdf")
