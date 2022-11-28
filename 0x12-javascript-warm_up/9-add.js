#!/usr/bin/node
const args = process.argv.slice(2);
const c = parseInt(args[0]);
const d = parseInt(args[1]);
function add (a, b) {
  return a + b;
}
const sum = add(c, d);
console.log(sum);
