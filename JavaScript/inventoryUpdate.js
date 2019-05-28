
function updateInventory(curInv, newInv) {
    // All inventory must be accounted for or you're fired!
 
    let curList;
    let newList;
    let counter;
    for (let newIdx in newInv) {
    // console.log(newIdx)
      counter = 0

      for (let curIdx in curInv) {
        curList = curInv[curIdx]
        newList = newInv[newIdx]
        // console.log(curList);
        counter += 1
        if (newList[1] == curList[1]) {
          // console.log('NEW: ', newList, 'CURRENT: ', curList)  
          curList[0] += newList[0]      
          // console.log('CURRENT: ', curList)  
          counter = 0
          break
        }  
      }
      if (counter > 0) {
        curInv.push(newList)
        counter = 0
      }
    }
  return curInv;
}
