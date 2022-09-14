#!/usr/bin/node
/*
Write a script that display the status code of a GET request:
- The first argument is the URL to request (GET)
- The status code must be printed like this: code: <status code>
- You must use the module axios
Info axios: https://github.com/axios/axios
*/

// Include process module
const process = require('process'); // add the process module to use the "argv" function.
const args = process.argv; // I define args as process.argv
const axios = require('axios').default; // import axios module

const URL = args[2];

// We use the "axios" module to make a GET request from the HTTP protocol
axios.get(URL)
  .then(function (response) {
    // handle success
    console.log(`code: ${response.status}`);
  })
  .catch(function (error) {
    // handle error - to access the status of the error, it is through the response (response)
    console.log(`code: ${error.response.status}`);

  });
