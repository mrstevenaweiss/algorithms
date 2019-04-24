function dropElements(arr, func) {
  // Drop them elements.
  let index = 0
  for (let i = 0; i < arr.length; i++) {
    if (func(arr[i]) === false) {
      index = i+1
      break;
    }
  }
  console.log(arr.slice(index))
}

// dropElements([0, 1, 0, 1], function(n) {return n === 1; });
dropElements([1, 2, 3], function(n) {return n > 0;})
dropElements([1, 2, 3, 4], function(n) {return n > 5;}) // []
dropElements([1, 2, 3, 9, 2], function(n) {return n > 2;}) // [3, 9, 2]

  // let list = []
  // for (let number in arr) {
  //   let listNum = arr[number]
  //   if (func(listNum) === true) {
  //     list.push(listNum)
  //   } else {
  //     break
  //   }
  // }
  // console.log(list)

// function funct(a, foo){
//     foo(a) // this will return a
// }

// funct("z", function (x) { return x; });


