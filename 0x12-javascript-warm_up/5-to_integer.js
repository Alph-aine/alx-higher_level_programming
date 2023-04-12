#!/usr/bin/node
const args = process.argv[2];
const num = parseInt(args);
if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
