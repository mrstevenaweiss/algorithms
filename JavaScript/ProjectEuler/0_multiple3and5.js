
function multiplesOf3and5(number) {

  let multi = []
  for (let i = 0; i< number ; i++) {
    if (i % 5 == 0) {
      multi.push(i);
    } else if (i % 3 == 0) {
      multi.push(i)
    }
  }
  
  const sum = multi.reduce((total, amount) => total + amount); 

  console.log(sum)
}

multiplesOf3and5(49);
// multiplesOf3and5(1000);
