Check if the predicate (second argument) is truthy on all elements of a collection (first argument).

In other words, you are given an array collection of objects. The predicate pre will be an object property and you need to return true if its value is truthy. Otherwise, return false.

In JavaScript, truthy


//Advanced
function truthCheck(collection, pre) {
  // Is everyone being true?
  return collection.every(obj => obj[pre]);
}



// Mine
function checkValue(value) {
    return !!value;
}

function keyCheck(collection, pre) {
  for (let obj in collection) {
    let pass = collection[obj][pre];

    if (pre in collection[obj] == false ) {
      return false
    } else if (checkValue(pass) == false) {
      return false
    }
  }
  return true
}

function truthCheck(collection, pre) {
  return keyCheck(collection, pre)
}
