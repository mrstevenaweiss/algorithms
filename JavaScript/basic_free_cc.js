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



// Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a// ... ending.
function truncateString(str, num) {
  // Clear out that junk in your trunk
  if (num < str.length) {
    return str.slice(0, num)+'...';
  } else {
    return str;
  }
}
console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8));



Create a function that looks through an array (first argument) and returns the first element in the array that passes a truth test (second argument). If no element passes the test, return undefined.

function findElement(arr, func) {
  let numbers = arr.filter(func);
  return numbers[0];
}

findElement([1, 2, 3, 4], num => num % 2 === 0);


//Check if a value is classified as a boolean primitive. Return true or false.

function booWho(bool) {
  // What is the new fad diet for ghost developers? The Boolean.
  return typeof bool == 'boolean';
}

booWho(false);















