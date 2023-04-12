#!/usr/bin/node
const msg = 'X';
const arg = process.argv[2];
const num = parseInt(arg);

if (num < 1) {
  //  do nothing
} else if (num >= 1) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write(msg);
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
