#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err, i) => {
      if (err) console.log(err);
    });
  }
});
