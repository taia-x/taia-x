// var CryptoJS = require("crypto-js");
var sha256File = require('sha256-file');

sha256File('./main.py', function (error, sum) {
  if (error) return console.log(error);
  console.log("sum:")
  console.log(sum)
})