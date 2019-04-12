

console.log('hello steven');


// Diff Two Arrays
// Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. In other words, return t// he symmetric difference of the two arrays.

function diffArray(arr1, arr2) {
  var newArr = arr1.concat(arr2);
  console.log(newArr);
  // Same, same; but different.
  let map = {}
  let objArr = [];
  
  for (let i = 0; i , newArr.length ;i++) {
    if (newArr[i] in map) {
      map[newArr[i]]++;
    } else {
      map[newArr[i]] = 1
    }
  }

  for (let key in map) {
    if (map[key] == 1) {
      objArr.push(key);
    }
  }

  return objArr;
}

console.log(diffArray([1, "calf", 3, "piglet"], [7, "filly"]))

function diffArray(arr1, arr2) {
	return arr1
        .concat(arr2)
        .filter(
            item => !arr1.includes(item) || !arr2.includes(item)
        )
    }
