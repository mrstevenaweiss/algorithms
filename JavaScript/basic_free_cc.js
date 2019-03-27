function repeatStringNumTimes(str, num) {
  // repeat after me
  let newString = '';
  if (num > 0) {
    for (let i = 0; i < num; i++) {
    newString += str;
    } 
  } 
  return newString;
}

console.log(repeatStringNumTimes("abc", -1))
;
