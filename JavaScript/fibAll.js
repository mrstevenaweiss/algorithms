

function sumFibs(num) {
      // Perform checks for the validity of the input
  if (num < 0) return -1;
  if (num === 0 || num === 1) return 1;

  let prior = 1;
  let next = 1;
  let temp = prior+next;
  let sums = []

  for (let i = 1; i<=num; i++) {
    // console.log(i)
    prior = next
    next = temp
    temp = prior + next
    if (temp <= num && temp % 2 !== 0) {
      sums.push(temp)
    }
  }
  console.log(sums)
  return sums.reduce((a, b) => {return a+b},  2)
}

sumFibs(75025);
// 135721
