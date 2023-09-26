#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
let data;
function fprint (i) {
  request(data[i], function (error, response2, body2) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body2).name);
      if (i < data.length - 1) {
        fprint(i + 1);
      }
    }
  });
}
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body).characters;
    fprint(0);
  }
});
