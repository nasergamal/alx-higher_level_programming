#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
function factorial (a) {
  if (!a || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(num1));
