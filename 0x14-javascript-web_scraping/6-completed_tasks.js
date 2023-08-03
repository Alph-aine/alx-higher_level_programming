#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (err) console.error(err);
  const todos = JSON.parse(body);
  const completed = {};

  todos.forEach((todo) => {
    if (todo.completed && completed[todo.userId] === undefined) {
      completed[todo.userId] = 1;
    } else if (todo.completed) {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
