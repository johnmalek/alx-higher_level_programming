#!/usr/bin/node
const args = process.argv.slice(2);
let i;
const x = args[0];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
