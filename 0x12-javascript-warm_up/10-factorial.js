#!/usr/bin/node
const args = process.argv.slice(2);
const n = parseInt(args[0]);
function fact (x) {
  if (x === 1 || x === 0) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
if (n) {
  const result = fact(n);
  console.log(result);
} else {
  console.log(1);
}
