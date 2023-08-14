#!/usr/bin/node

let max = process.argv[2];
let max2;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max2 = max;
      max = process.argv[i];
    } else if (process.argv[i] < max && (!max2 || process.argv[i] > max2)) {
      max2 = process.argv[i];
    }
  }
  console.log(max2);
}
