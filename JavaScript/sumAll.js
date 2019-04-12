

let name = process.argv;

console.log('hello world ' + name[2]);

// Sum All Numbers in a Range
// We'll pass you an array of two numbers. Return the sum of those two numbers plus the sum of all the numbers between them.


function sumAll(arr) {
  let range = Math.abs(arr[0]-arr[1])
  let multiple = Math.round(range/2)
  return (multiple)  * (arr[0] + arr[1])
}

console.log(sumAll([5, 10]))



