function updateInventory(curInv, newInv) {
    let curList;
    let newList;
    let counter;
    console.log(curInv)
    if (curInv.length == 0) {
            newInv.sort(function (a, b) {
          if (a[1] > b[1]) {
              return 1;
          }
          if (a[1] < b[1]) {
              return -1;
          }
          return 0;
      });
      return newInv
    }

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

    curInv.sort(function (a, b) {
        if (a[1] > b[1]) {
            return 1;
        }
        if (a[1] < b[1]) {
            return -1;
        }
        return 0;
    });
    
    return curInv;
}


