#!/usr/bin/node
const request = require('request');

const requestURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(requestURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
