# JSON Deep Equal

https://leetcode.com/problems/json-deep-equal/description/

Given two values `o1` and `o2`, return a boolean value indicating whether two values, `o1` and `o2`, are **deeply equal**.

For two values to be **deeply equal**, the following conditions must be met:

- If both values are primitive types, they are **deeply equal** if they pass the `===` equality check.
- If both values are arrays, they are **deeply equal** if they have the same elements in the same order, and each element is also **deeply equal** according to these conditions.
- If both values are objects, they are **deeply equal** if they have the same keys, and the associated values for each key are also **deeply equal** according to these conditions.

You may assume both values are the output of `JSON.parse`. In other words, they are valid JSON.

Please solve it without using lodash's `_.isEqual()` function

 

**Example 1:**

```
Input: o1 = {"x":1,"y":2}, o2 = {"x":1,"y":2}
Output: true
Explanation: The keys and values match exactly.
```

**Example 2:**

```
Input: o1 = {"y":2,"x":1}, o2 = {"x":1,"y":2}
Output: true
Explanation: Although the keys are in a different order, they still match exactly.
```

**Example 3:**

```
Input: o1 = {"x":null,"L":[1,2,3]}, o2 = {"x":null,"L":["1","2","3"]}
Output: false
Explanation: The array of numbers is different from the array of strings.
```

**Example 4:**

```
Input: o1 = true, o2 = false
Output: false
Explanation: true !== false
```

 

**Constraints:**

- `1 <= JSON.stringify(o1).length <= 105`
- `1 <= JSON.stringify(o2).length <= 105`
- `maxNestingDepth <= 1000`



**Reflections**:

1. array is object, to detect array: use `Array.isArray(obj)`
2. null is object, check null by `obj == null`



## Solution

```javascript
/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function (o1, o2) {
    if (o1 === o2) return true

    if (o1 == null || typeof o1 != 'object' || 
        o2 == null || typeof o2 != 'object') return false

    // if both are arrays
    if (Array.isArray(o1) && Array.isArray(o2)) {
        if (o1.length != o2.length) return false

        for (let i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[i], o2[i])) return false
        }
    } else if (!Array.isArray(o1) && !Array.isArray(o2)) {
        // both are objects
        if (Object.keys(o1).length != Object.keys(o2).length) return false

        for (let key in o1) {
            if (!(key in o2) || !areDeeplyEqual(o1[key], o2[key])) return false
        }

    } else {
        return false
    }

    return true
};
```

TC: O(n)

SC: O(D), D is the maximum depth of recursion