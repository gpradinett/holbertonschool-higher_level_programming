#!/usr/bin/node
// script that prints a square

const square = (process.argv[2]);

if (isNaN(square)) {
  console.log('Missing size');
}
for (let i = 0; i < square; i++) {
  console.log('X'.repeat(square));
}
