#!/usr/bin/node

exports.addMeMaybe = (a, b) => {
  a++;
  b(a);
};
