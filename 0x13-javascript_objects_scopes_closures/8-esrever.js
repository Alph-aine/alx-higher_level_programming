#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  for (let i = 0; i < len; i++) {
    const temp = list[i];
    list[i] = list[len - 1];
    list[len - 1] = temp;
    len--;
  }
  return list;
};
