
function symDiff(args) {
  console.log('args', args, args.length)
  let aList = args
  let difference = aList[0]
                  .filter(x => !aList[1].includes(x))
                  .concat(aList[1].filter(x => !aList[0].includes(x)));
    let unique = [...new Set(difference)]; 
    return unique
}

function sym(...args) {
  let temp = []
  let aList = [...args]

  if (aList.length < 3) {
    return symDiff(aList)
  } 
  else {
    console.log(aList)
    let lastList = aList.pop()
    temp.unshift(lastList)
    console.log('aList: ', aList, 'temp: ', temp)
    let newFront = sym(...aList)
    console.log(newFront)
    aList.splice(0,2)
    console.log(aList)
    aList = [...temp]
    console.log(aList)
    aList.unshift(newFront)
    console.log(aList)
    return sym(...aList)
  }
}
