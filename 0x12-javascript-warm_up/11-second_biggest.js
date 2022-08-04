#!/usr/bin/node
//  script that searches the second biggest integer in the list of arguments.

const argv = process.argv;
let ordArr = [];

if (argv.length <= 3) { console.log(0); } else {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (isNaN(num)) { continue; } else { ordArr.push(num); }
  }
}

if (ordArr.length > 1) {
  ordArr = [...new Set(ordArr)];
  ordArr = ordArr.sort(function (a, b) { return a - b; });
  console.log(ordArr[ordArr.length - 2]);
}
