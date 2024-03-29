#!/usr/bin/node
/*
Write a script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object
process.argv --> https://www.geeksforgeeks.org/node-js-process-argv-property/
*/

// Include process module
const process = require('process');
const args = process.argv; // I define args as process.argv

const path = args[2];

const fs = require('fs'); // load fs class

fs.readFile(path, 'utf-8', (err, content) => {
  if (err) {
    return console.log(err);
  }
  console.log(content);
});
