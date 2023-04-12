#!/usr/bin/node
const msg = 'C is fun';
const arg = process.argv[2];
const num = parseInt(arg);
if (num < 1) {
  //  do nothing
} else if (num >= 1) {
  for (let i = 0; i < num; i++) {
    console.log(msg);
  }
} else {
  console.log('Missing number of occurrences');
}
