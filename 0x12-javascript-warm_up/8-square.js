#!/usr/bin/node

const arg = parseInt(process.argv[2]);
let x = 'X';
if (!arg) {
  console.log('Missing size');
} else {
  for (let n = 1; n < arg; n++) {
    x += 'X';
  }
  for (let i = 0; i < arg; i++) {
    console.log(x);
  }
}
