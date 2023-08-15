#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
