#!/usr/bin/node
const args = process.argv.splice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const num = args.map(Number);
  num.sort(function (a, b) { return b - a; });
  console.log(num[1]);
}
