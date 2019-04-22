function sumPrimes(num) {
  return num;
}

sumPrimes(10);function isPrime(n) {
    if (n == 1) { return false}
    if (n == 2) { return true }
    if (n == 3) { return true }
    if (n % 2 == 0) { return false } 
    if (n % 3 == 0) { return false }

    let i = 5
    let w = 2

    while (i * i <= n) {
      if (n % i == 0) {
        return false 
      }
      i += w
      w = 6 - w
    }
    return true
}

function sumPrimes(num) {
  if (num <= 1) {return "Nah"}

  let primes = [...Array(num+1).keys()].filter((num) => { return num % 2 !== 0 }).filter((num) => { return num % 5 !== 0 })
  primes.unshift(2, 5)

  let newBull = []
  for (let i = 0; i < primes.length; i++) {
    if ( isPrime(primes[i]) == true ) {
      let number = primes[i]
      newBull.push(number);
    }
  } 
  return newBull.reduce((a, b) => { return a+b}, 0)
}

// sumPrimes(10) //=> 17
sumPrimes(977) //=> 73156
