# Arrays


A array is a data structure with a list of values of similar data type. In python we can store data of multiple types.

- Arrays are accessed by index values, the index starts from 0. The lookup of index = `O(1)`

- Array traversal = `O(n)`

- Array insertion = `O(n)`. To insert an element the array values are shifted and then the value is inserted.

```python
 arr.insert(1, 200);
```

- Array deletion = `O(1)`. Similar to insertion, we traverse to the index given, remove the element and shift the array values forward.

```python
 arr.remove(1);
```

- In python the array we use is `Dyanamic Array`. Dynamic array when initialized create a capacity with certain number, when we try to add values beyond the intial capacity, the array creates a new array with the double capacity and copy all the values from first array to the new array.