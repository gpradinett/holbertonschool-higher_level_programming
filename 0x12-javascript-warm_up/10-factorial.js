#!/usr/bin/node
// script that computes and prints a factorial

const fac = parseInt(process.argv[2]);
console.log(factorial(fac));
function factorial (fac) {
  if (isNaN(fac) || fac <= 0) {
    return 1;
  } else {
    return fac * factorial(fac - 1);
  }
}
