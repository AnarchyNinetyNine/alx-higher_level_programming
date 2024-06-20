#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (const element of list) {
    if (element === searchElement) {
      occurence += 1;
    }
  }
  return occurence;
};
