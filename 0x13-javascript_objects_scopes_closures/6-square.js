#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}
module.exports = Square;
