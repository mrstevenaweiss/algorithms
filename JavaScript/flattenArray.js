// function steamrollArray(arr1) {

//    return arr1.reduce((acc, val) => Array.isArray(val) ? acc.concat(steamrollArray(val)) : acc.concat(val), []);
// }

function steamrollArray(arr) {
  let finished = []
  console.log('\n')
  let first;
  let newFront;
  // console.log('inside loop', arr);

  for (let i = 0; i <= arr.length+5; i++) {
    console.log('inside loop', arr);
  // while (arr.length !== 0 ) {
    // console.log('arr', arr.length)
    console.log('\n')
  // if front is NOT an array (== false), append the number to the finished list
  if (Array.isArray(arr[0]) == false) {
    console.log('front', arr[0])
    console.log(arr[0], 'not a list/to be added to finished')
    first = arr.shift();
    finished.push(first);
    console.log('finished after loop', finished);
  }
  // if front is a list (=== true), pop out of list format
  else if (Array.isArray(arr[0]) == true) { 
    console.log('front', arr[0])
    console.log('item to be unlisted', arr[0])
    newFront = arr[0][0];
    console.log(newFront)
    console.log(arr[0])
    console.log('shift', arr.shift())
    console.log('arr after shift', arr);
    arr.unshift(newFront)
    console.log('finished after loop', finished);
  }

  }
  return finished;
}

// // steamrollArray([ 2, [2] ])
steamrollArray( [1, [2], [3, [[4]]]] );

// // if (arr.length === 1) {
//   //   finished.push(arr[0])
//   // } else {
//   //   console.log(arr.length)
//   // }
  
//   // console.log(finished);
