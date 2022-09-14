#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
You must use the module axios
*/

// Include process module
const process = require('process'); // add the process module to use the "argv" function.
const args = process.argv; // I define args as process.argv
const axios = require('axios').default; // import axios module

const URL = args[2]; // The first argument is the API URL of the Star wars API

// We use the "axios" module to make a GET request from the HTTP protocol
axios.get(URL)
  .then(function (response) {
    // handle success
    const data = response.data;
    const dict = {};

    // We go through the characters of each movie
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        // dd
        if (dict[data[i].userId] !== undefined) {
          dict[data[i].userId] = dict[data[i].userId] += 1;
        } else {
          dict[data[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  });
// .catch(function (error) {
// handle error - to access the status of the error, it is through the response (response)
//  console.log(`code: ${error.response.status}`);
// });
