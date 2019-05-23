
let singles = {
    0: "",
    1: "I",
    2: "II", 
    3: "III",
    4: "IV", 
    5: "V", 
    6: "VI", 
    7: "VII", 
    8: "VIII", 
    9: "IX"
}

let doubles = {
    0: "",
    1: "X",
    2: "XX", 
    3: "XXX",
    4: "XL", 
    5: "L", 
    6: "LX", 
    7: "LXX", 
    8: "LXXX", 
    9: "XC"
}

let triple = {
    0: "",
    1: "C",
    2: "CC", 
    3: "CCC",
    4: "CD", 
    5: "D", 
    6: "DC", 
    7: "DCC", 
    8: "DCCC", 
    9: "CM"
}

let quad = {
    0: "",
    1: "M",
    2: "MM", 
    3: "MMM",
    4: "MV", 
    5: "V", 
    6: "MV", 
    7: "MVV", 
    8: "MVVV", 
    9: "MX"
}


function convertToRoman(num) {
    let n = num.toString();

    if (n.length == 1) {
        return singles[n];
    } else if (n.length == 2) {
        console.log(doubles[n[0]] + singles[n[1]] )
        return doubles[n[0]] + singles[n[1]]
    } else if (n.length == 3) {
        console.log(triple[n[0]] + doubles[n[1]] + singles[n[2]] )
        return triple[n[0]] + doubles[n[1]] + singles[n[2]]
    } else if (n.length == 4) {
        return quad[n[0]] + triple[n[1]] + doubles[n[2]] + singles[n[3]]
    } 
}

convertToRoman(400);
convertToRoman(36);
