// 258. Add Digits

var addDigits = function (num) {
  while (num >= 10) {
    let q = Math.floor(num / 10);
    let r = num % 10;
    num = q + r;
  }
  return num;
};
