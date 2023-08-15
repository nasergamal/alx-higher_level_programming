#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
const file = fs.readFileSync(arg[2], 'utf8').toString();
const file2 = fs.readFileSync(arg[3], 'utf8').toString();
fs.writeFileSync(arg[4], file + file2);
