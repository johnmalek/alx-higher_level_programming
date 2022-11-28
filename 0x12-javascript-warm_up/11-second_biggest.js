#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('1');
} else {
  const array = args.sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
