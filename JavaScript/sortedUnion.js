

Write a function that takes two or more arrays and returns a new array of unique values in the order of the original provided arrays.

function uniteUnique(...args) {
  let newSet = [].concat(...args)
  let unique = [...new Set(newSet)]; 
  // var unique = myArray.filter((v, i, a) => a.indexOf(v) === i); 
  return unique;
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);


