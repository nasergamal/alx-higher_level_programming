#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const di = {};
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        di[data[i].userId] = di[data[i].userId] + 1 || 1;
      }
    }
    console.log(di);
  }
});
