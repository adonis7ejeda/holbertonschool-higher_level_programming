#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let index = 0; index < process.argv[2]; index++) {
  console.log('X'.repeat(process.argv[2]));
}
