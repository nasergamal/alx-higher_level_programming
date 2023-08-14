#!/usr/bin/node

const nums = [];
const args = process.argv.splice(2, process.argv.length);
const len = args.length;
if (len <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < len; i++) {
    nums[i] = args[i];
  }
  nums.sort((a, b) => a - b);
  console.log(nums[len - 2]);
}
