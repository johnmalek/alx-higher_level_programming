#!/usr/bin/node
let i;
const args = process.argv.slice(2);
let x = args[0];
if (x) {
  let x2 = parseInt(x);
  for (i=0; i<x2; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
