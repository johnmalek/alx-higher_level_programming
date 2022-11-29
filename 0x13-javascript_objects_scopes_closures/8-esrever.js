#!/usr/bin/node
exports.esrever = function esrever (list) {
  const reversedList = [];
  while (list.length) {
    reversedList.push(list.pop());
  }
  return reversedList;
};
