#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) console.error(err);
  const results = JSON.parse(body).results;
  let count = 0;
  for (const i in results) {
    const characters = results[i].characters;
    for (const c in characters) {
      if (characters[c].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
