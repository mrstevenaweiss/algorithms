
let coin = {
  'ONE HUNDRED' : 100,
  'TWENTY': 20,
  'TEN': 10,
  'FIVE': 5,
  'ONE': 1,
  'QUARTER': 0.25,
  'DIME': 0.1,
  'NICKEL': 0.05,
  'PENNY': 0.01
}

function makeChange(change, cid) {
  let drawerTotal = 0

  let cidReverse = cid.reverse()
  let list = []

  for (let register in cidReverse) {
    let currencyTotal = cid[register][1]
    drawerTotal += cid[register][1]
    let key = coin[cid[register][0]]

    if (key > change) {
      continue;
    } else {
      if (currencyTotal < change) {
        
        change = Number((change -  currencyTotal).toFixed(2))
        
        list.push(cid[register])

      } else if (currencyTotal > change) {
        
        let multiply = Math.floor(change / key)
        let currencyUsed = key * multiply
        
        change = Number((change - currencyUsed).toFixed(2))
        
        let nList = []
        nList.push(cid[register][0])
        nList.push(currencyUsed)
        list.push(nList)
      }
    }
  }

  if (change == drawerTotal) {
    return ["CLOSED", list] 
  } else if (change < drawerTotal) {
      return ["OPEN", list] 
  } else {
      return "NAH"
  }
}

function checkCashRegister(price, cash, cid="money back") {
  let change = cash - price;
  // let orderedRegister = inRegister(change, cid)
  let yourChangeInBills = makeChange(change, cid);

  if (yourChangeInBills == "NAH") {
    return {status: "INSUFFICIENT_FUNDS", change: []}
  } else if (yourChangeInBills[0] == 'CLOSED') {
    return {status: "CLOSED", change: yourChangeInBills[1]}
  } else if (yourChangeInBills[0] == 'OPEN') {
    return {status: "OPEN", change: yourChangeInBills[1]}
  }
}

checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) 

