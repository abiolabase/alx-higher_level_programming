#!/usr/bin/node
const { argv } = require('node:process');

let num = argv[2];
if (Number(num).type !== Number) {
	console.log("Not a number");
} else {
	console.log(`My number: ${num}`);
}
