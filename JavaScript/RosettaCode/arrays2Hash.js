

function arrToObj (keys, vals) {
  let obj = {}

  for (let i = 0 ; i < keys.length; i++) {
    // console.log('keys', keys[i], 'vals', vals[i])
    obj[keys[i]] = vals[i];

  }
  // console.log(obj)
  return obj;
}

// arrToObj([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]) // { 1: "a", 2: "b", 3: "c", 4: "d", 5: "e" }
arrToObj([1, 2, 3, 4, 5], ["a", "b", "c", "d"]) // { 1: "a", 2: "b", 3: "c", 4: "d", 5: undefined }
arrToObj([1, 2, 3], ["a", "b", "c", "d", "e"]) //  { 1: "a", 2: "b", 3: "c" }
// arrToObj(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5]) // { "a": 1, "b": 2, "c": 3 , "d": 4, "e": 5 }
// arrToObj(["a", "b", "c", "d", "e"], [1, 2, 3, 4]) // { "a": 1, "b": 2, "c": 3 , "d": 4, "e": undefined }
// arrToObj(["a", "b", "c"], [1, 2, 3, 4, 5]) // { "a": 1, "b": 2, "c": 3 }
