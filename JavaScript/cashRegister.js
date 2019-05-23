

function checkCashRegister(price, cash, cid) {
  var change;
  // Here is your change, ma'am.
  return change;
}function inRegister(change, cid) {
  let cidReverse = cid.reverse()
  // let money = 0
  let list = []

  for (let register in cidReverse) {
    // console.log(cid[register][1])
    if (cid[register][1] > change) {
      continue; 
    } else if (cid[register][1] <= change) {
      list.push(cid[register])
      change -= cid[register][1]
      console.log(change)
    }
  //   money += cid[register][1]
  }
  console.log(list)
}

function checkCashRegister(price, cash, cid="money back") {
  let change = cash - price;
  let orderedRegister = cid;
  let moneyInRegister = inRegister(change, cid);
  // console.log(moneyInRegister);

  if (moneyInRegister < change) {
    return {status: "INSUFFICIENT_FUNDS", change: []}
  } else if (moneyInRegister == change) {
    return {status: "CLOSED", change: orderedRegister}
  } else if (moneyInRegister > change) {
    return {status: "OPEN", change: orderedRegister}
  }
}

checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])

// checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) should return {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}
