#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
let data = [];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body).characters;
    fprint();
  }
});
async function fprint () {
  for (const i in data) {
    request(data[i], function (error, response2, body2) {
      if (error) {
        console.log(error);
      } else {
        console.log(JSON.parse(body2).name);
      }
    });
  }
}
