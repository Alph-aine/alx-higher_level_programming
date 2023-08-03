#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];
const data = process.argv[3];

fs.writeFile(fileName, data, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('successful');
  }
});
