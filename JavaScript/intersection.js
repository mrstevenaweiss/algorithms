function sym(...args) {
  // flatten the arrays
  let d = [].concat(...args);

  let symDiff = []
  // create an upper bound for the '0' array
  let upper =  Math.max.apply(null, d) 

  // create a length to then ++ based on index
  for (var i = 0; i <= upper; i++) {
    symDiff.push(0);
  }

  // ++ based on index #  
  for (var i=0; i < d.length; i++) {
    symDiff[d[i]] += 1
  }

  // 'filter' 
  let sym = []
  for (var i = 0; i < symDiff.length; i++ ) {
    if (symDiff[i] == 1) {
      sym.push(i)
    }
  }
  return sym
}
isym([1, 2, 3], [5, 2, 1, 4]);
