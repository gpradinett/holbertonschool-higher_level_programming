#!/usr/bin/node

const axios = require('axios').default; // import axios module

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]).then(
  response => {
    const list = response.data.characters;
    list.forEach((item) => {
      axios.get(item).then(
        response2 => {
          console.log(response2.data.name);
        });
    });
  });
