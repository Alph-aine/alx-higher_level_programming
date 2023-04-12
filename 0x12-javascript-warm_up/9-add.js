#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg1 = process.argv[2];
const a = parseInt(arg1);
const arg2 = process.argv[3];
const b = parseInt(arg2);

const result = add(a, b);
console.log(result);
