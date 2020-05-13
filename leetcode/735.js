// 735. Asteroid Collision
/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
const asteroidCollision = function (asteroids) {
  let output = []; // stack [5, 10]
  for (let i = 0; i < asteroids.length; i++) {
    let a = output.pop();
    let b = asteroids[i];
    if (a) {
      if (a > 0 && b < 0) {
        if (Math.abs(a) > Math.abs(b)) {
          output.push(a);
        } else if (Math.abs(a) < Math.abs(b)) {
          i--;
        }
      } else {
        output.push(a, b);
      }
    } else {
      output.push(b);
    }
  }
  return output;
};
