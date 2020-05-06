var singleNumber = function (nums) {
  let obj = {};
  nums.forEach(num => {
    obj[num] = obj[num] ? obj[num] += 1 : 1;
  });
  for (let key in obj) {
    if (obj[key] === 1) return key;
  }
};