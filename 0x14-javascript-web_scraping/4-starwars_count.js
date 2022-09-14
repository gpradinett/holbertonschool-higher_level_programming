#!/usr/bin/node

const axios = require('axios').default;
let count = 0;

axios.get(process.argv[2]).then(
  respon => {
    for (const i of respon.data.results) {
      for (const j of i.characters) {
        if (j.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  });
