# ithelps

Efficient iteration helpers for Python

# Contents
```
>>> import ithelps as ih
>>> seq = [1, 2, 3, 4]
>>> 
>>> sequential_pairs = ih.munch(seq, 2)
>>> [list(pair) for pair in sequential_pairs]
[[1, 2], [3, 4]]
>>> 
>>> sliding_pairs = ih.slide(seq, 2)
>>> [list(pair) for pair in sliding_pairs]
[[1, 2], [2, 3], [3, 4]]
```