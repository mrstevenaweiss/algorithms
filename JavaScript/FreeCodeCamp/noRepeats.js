// procedure generate(k : integer, A : array of any):
//     if k = 1 then
//         output(A)
//     else
//         // Generate permutations with kth unaltered
//         // Initially k == length(A)
//         generate(k - 1, A)

//         // Generate permutations for kth swapped with each k-1 initial
//         for i := 0; i < k-1; i += 1 do
//             // Swap choice dependent on parity of k (even or odd)
//             if k is even then
//                 swap(A[i], A[k-1]) // zero-indexed, the kth is at k-1
//             else
//                 swap(A[0], A[k-1])
//             end if
//             generate(k - 1, A)

//         end for
//     end if

function allEqual(input) {
    return input.split('').every(char => char === input[0]);
}

function heaps(input) {
  let heap = []
  var rawLetters = input.split("")
  console.log(rawLetters)

  // let word = rawLetters[0] + rawLetters[1]
  // heap.push(word)

  // // word = rawLetters[0] + ['ba']
  // // heap.push(word)

  // console.log(heap);


}




function permAlone(str) {
  if (str.length == 1) {
    return 1
  } else {
    if ( allEqual(str)) {
      return 0
    } else {
      return heaps(str)
    }
  }
}

permAlone("ab")  // should return 2.
// permAlone("aaa") // should return 0.
// permAlone("aabb") // should return 8.
// permAlone("abcdefa")  // should return 3600.
// permAlone("abfdefa") // should return 2640.
// permAlone("zzzzzzzz") // should return 0.
// permAlone("aaab") // should return 0.
// permAlone("aaabb") // should return 12.


