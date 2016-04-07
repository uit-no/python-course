# Farm Survey

(Note: This is an unfinished example which would show how a messy program
could be rewritten to be well organized idiomatic Python.  There was
not enough time to complete the code.)

The farm inspector demands an annual report on all animals on your
farm:

```
Animals in house: cat (1), dog (1)
Animals not in house: sheep (2)
Required food: fish (1), meat (1), grass (2)

Warning: fox on farm! (Eats chicken)
```

You have your animals in a CSV (comma separated values) file:

```
species;food;home
dog;meat;house
cat;fish/mice;house
sheep;grass;field
sheep;grass;field
fox;chicken;
```

Complications:

* some animals eat more than one type of food
* some animals don't belong on your farm (home is '')
