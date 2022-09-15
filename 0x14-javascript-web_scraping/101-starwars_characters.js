#!/usr/bin/node

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2]).then(
  async resp => {
    const list = resp.data.characters;
    const len = list.length;
    for (let i = 0; i <= len - 1; i++) {
      await axios.get(list[i]).then(
        resp2 => {
          console.log(resp2.data.name);
        });
    }
  });
