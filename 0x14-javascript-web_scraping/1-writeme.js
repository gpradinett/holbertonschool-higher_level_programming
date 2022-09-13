#!/usr/bin/node
/*
Write a script that writes a string to a file:
- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in utf-8
- If an error occurred during while writing, print the error object
Info write a file: https://nodejs.dev/en/learn/writing-files-with-nodejs/
*/

// Include process module
const process = require('process');
const args = process.argv; // I define args as process.argv

const path = args[2]; // file where the content will be written
const texto = args[3]; // content to write
const fs = require('fs'); // load fs class

fs.writeFile(path, texto, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
