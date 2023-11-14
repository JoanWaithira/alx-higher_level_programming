#!/usr/bin/node

const args = process.argv.slice(2);
let maxInt = 0;

if (args.length > 1) {
  const numbers = args.map(Number).sort((a, b) => b - a);
  maxInt = numbers[1];
}
console.log(maxInt);
