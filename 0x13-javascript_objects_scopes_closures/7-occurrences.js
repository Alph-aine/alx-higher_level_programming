#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const newList = [];
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      newList.push(list[i]);
    }
  }
  return newList.length;
};
