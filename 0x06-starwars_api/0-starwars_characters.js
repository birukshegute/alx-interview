#!/usr/bin/node

const request = require('request');

const query = (arr, i) => {
  if (i === arr.length) return;
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      query(arr, i + 1);
    }
  });
};

request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      query(chars, 0);
    }
  }
);
