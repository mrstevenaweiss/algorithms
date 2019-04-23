// inefficient solution for large numbers


// gcd of two numbers 
function gcd(a,b) {
    if (a == b) {
      return a;
    }
    if (a > b) {
      return gcd(a-b, b) 
    } else {
      return gcd(a, b-a) 
    }
}

// lcm using gcd
function lcm(a,b) {
  return (a*b) / gcd(a,b) 
} 

// process of recursively call the numbers
//  0  1  2  3 
// [2, 3, 4, 5]
// multis = []
// result = str[0]
// multis.push[result]
// result = lcm(result, i+1)

// lcm(2, 3) => result = 6
// lcm(6, 4) => result = 12
// lcm(12, 5) => result = 60
// lcm(12, 5)

function smallestCommons(arr) {
  let front = arr[0]
  let back = arr[1]

  if (arr[1] < arr[0]) {
    front = arr[1]
    back = arr[0]
  }

  // create the necessary consecutive ints
  let range = []
  for (let i = front; i <= back; i++) {
    range.push(i)
  }

  // scan through range and get lcm of each consectutive pair
  let multis = []
  let result = range[0]
  for (let i = 0; i < range.length; i++) {
    result = lcm(result, range[i])
    multis.push(result)
  }

  return multis[multis.length-1]
}
smallestCommons([13,1]);
