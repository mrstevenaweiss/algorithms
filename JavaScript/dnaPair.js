

function pair(letter) {
  if (letter == "A") {
    return ['A', 'T']
  } else if (letter == "T") {
    return ['T', 'A']
  } else if (letter == "C") {
    return ['C', 'G'] 
  } else {
    return ['G', 'C']
  }
}

function pairElement(str) {
  let array = [...str];
  let dna = []
  for (let i = 0; i < str.length; i++) {
    dna.push(pair(array[i]));
  }
  return dna;
}

pairElement("GCG");


