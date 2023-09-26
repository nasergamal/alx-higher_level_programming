#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    data.forEach((c) => {
      request(c, function (error, response2, body2) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body2).name);
        }
      });
    });
  }
});
