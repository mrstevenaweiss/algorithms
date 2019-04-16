//Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.

var globalTitle = "The_Andy_<wbr>Griffith_Show"

function spinalCase(str) {
  let yum = str.replace(/<(.|\n)*?>/g, "").replace(/([a-z])([A-Z])/g, '$1 $2').replace(/_/g, " ")
  let arr = yum.trim().split(/\s+/)
  
  let lowerWords = arr.map(word => word.toLowerCase())
  return lowerWords.join("-")
}

spinalCase(globalTitle);
spinalCase(another);
