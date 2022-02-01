/*
chapter 1
excercise 1
Problem:
Find average of all the elements in a list.
*/

const avg = (numbers) => {
  if (numbers.length > 0) {
    return (
      numbers.reduce((total, item) => total + item, 0) / numbers.length
    ).toFixed(2);
  }
  return undefined;
};

nums = [2, 4, 6, 6, 7, 9, 90, 45, 23, 67, 89];

console.log(`Average: ${avg(nums)}`);
