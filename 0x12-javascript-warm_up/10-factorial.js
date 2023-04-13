#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const args = process.argv[2];
const num = parseInt(args);
const result = factorial(num);
console.log(result);
