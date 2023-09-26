#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < data.length; i++) {
      data[i].characters.forEach((c) => {
        if (c.includes('18')) {
          count += 1;
        }
      });
    }
    console.log(count);
  }
});
