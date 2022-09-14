#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module axios
*/

// Include process module
const process = require('process'); // add the process module to use the "argv" function.
const args = process.argv; // I define args as process.argv
const axios = require('axios').default; // import axios module
const fs = require('fs'); // load fs class
const URL = args[2]; // The first argument is the URL to request
const filepath = args[3]; // The second argument the file path to store the body response

// We use the "axios" module to make a GET request from the HTTP protocol
axios.get(URL)
  .then(function (response) {
    // handle success
    const data = response.data;
    fs.writeFile(filepath, data, (error) => {
      if (error) {
        console.log(`Error: ${error}`);
      }
    });
    // console.log(response.data);
  })
  .catch(function (error) {
  // handle error - to access the status of the error, it is through the response (response)
    console.log(`code: ${error.response.status}`);
  });
