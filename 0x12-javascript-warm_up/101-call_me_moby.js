#!/usr/bin/node

exports.callMeMoby = (a, b) => {
  while (a > 0) {
    b(a);
    a--;
  }
};
