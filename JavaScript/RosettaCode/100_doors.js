let toggleDoors = {}

function makeDoors(n) {
  for (let i=1; i <= n; i++) {
    toggleDoors[i] = false;
  }
}

function finalDoors() {
  let doors = []
  // iterate through the object and push it into a list...
  Object.keys(toggleDoors).forEach(function (door) {
	  // console.log(door, toggleDoors[door]); // key, value
    if (toggleDoors[door] == true) {
      doors.push(door)
    }
  });
  return doors
}

function changeDoors(numDoors) {
  let insidePlus = 1
  let skipper = 1
  for (let i = 1; i <= numDoors; i += 1) {
    for (let j = insidePlus; j <= numDoors; j += skipper) {
      toggleDoors[j] = !toggleDoors[j];
      // if (toggleDoors[j] == false) {
      //   toggleDoors[j] = true
      // } else {
      //   toggleDoors[j] = false
      // }
    }
    insidePlus++
    skipper++
  }
}

function getFinalOpenedDoors(numDoors) {  
  makeDoors(numDoors)
  changeDoors(numDoors)
  return finalDoors();
}

getFinalOpenedDoors(100)



