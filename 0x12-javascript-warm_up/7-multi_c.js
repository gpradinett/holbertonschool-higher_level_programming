#!/usr/bin/node
// script that prints x times “C is fun”

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
