#!/usr/bin/node
const list = [];
exports.logMe = function (item) {
  list.push(item);
  const count = list.length - 1;
  console.log(`${count}: ${item}`);
};
