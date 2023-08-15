#!/usr/bin/node

exports.esrever = function (list) {
  let end = list.length - 1;
  let start = 0;
  const newList = [];
  while (end >= 0) {
    newList[start] = list[end];
    end--;
    start++;
  }
  return (newList);
};
