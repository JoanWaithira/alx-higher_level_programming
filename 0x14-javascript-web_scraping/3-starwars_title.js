#!/usr/bin/node
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
const Id = process.argv[2];

request(apiUrl + Id, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
