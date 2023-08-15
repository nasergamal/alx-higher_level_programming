#!/usr/bin/node
const sq = require('./5-square');

class Square extends sq {
  charPrint (sym = 'X') {
    let x = '';
    for (let w = 0; w < this.width; w++) {
      x += sym;
    }
    for (let h = 0; h < this.height; h++) {
      console.log(x);
    }
  }
}
module.exports = Square;
