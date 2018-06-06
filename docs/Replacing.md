
# Replacing Functions in the Dictionary


```python
from notebook_preamble import D, J, V
```

## A long trace


```python
V('[23 18] average')
```

                                      . [23 18] average
                              [23 18] . average
                              [23 18] . [sum 1.0 *] [size] cleave /
                  [23 18] [sum 1.0 *] . [size] cleave /
           [23 18] [sum 1.0 *] [size] . cleave /
           [23 18] [sum 1.0 *] [size] . [i] app2 [popd] dip /
       [23 18] [sum 1.0 *] [size] [i] . app2 [popd] dip /
    [23 18] [[sum 1.0 *] [23 18]] [i] . infra first [[size] [23 18]] [i] infra first [popd] dip /
                  [23 18] [sum 1.0 *] . i [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                              [23 18] . sum 1.0 * [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                                   41 . 1.0 * [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                               41 1.0 . * [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                                 41.0 . [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                       41.0 [[23 18]] . swaack first [[size] [23 18]] [i] infra first [popd] dip /
                       [23 18] [41.0] . first [[size] [23 18]] [i] infra first [popd] dip /
                         [23 18] 41.0 . [[size] [23 18]] [i] infra first [popd] dip /
        [23 18] 41.0 [[size] [23 18]] . [i] infra first [popd] dip /
    [23 18] 41.0 [[size] [23 18]] [i] . infra first [popd] dip /
                       [23 18] [size] . i [41.0 [23 18]] swaack first [popd] dip /
                              [23 18] . size [41.0 [23 18]] swaack first [popd] dip /
                              [23 18] . 0 swap [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                            [23 18] 0 . swap [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                            0 [23 18] . [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                   0 [23 18] [pop ++] . step [41.0 [23 18]] swaack first [popd] dip /
                        0 23 [pop ++] . i [18] [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                                 0 23 . pop ++ [18] [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                                    0 . ++ [18] [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                                    1 . [18] [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                               1 [18] . [pop ++] step [41.0 [23 18]] swaack first [popd] dip /
                      1 [18] [pop ++] . step [41.0 [23 18]] swaack first [popd] dip /
                        1 18 [pop ++] . i [41.0 [23 18]] swaack first [popd] dip /
                                 1 18 . pop ++ [41.0 [23 18]] swaack first [popd] dip /
                                    1 . ++ [41.0 [23 18]] swaack first [popd] dip /
                                    2 . [41.0 [23 18]] swaack first [popd] dip /
                     2 [41.0 [23 18]] . swaack first [popd] dip /
                     [23 18] 41.0 [2] . first [popd] dip /
                       [23 18] 41.0 2 . [popd] dip /
                [23 18] 41.0 2 [popd] . dip /
                         [23 18] 41.0 . popd 2 /
                                 41.0 . 2 /
                               41.0 2 . /
                                 20.5 . 


## Replacing `size` with a Python version

Both `sum` and `size` each convert a sequence to a single value.

     sum == 0 swap [+] step
    size == 0 swap [pop ++] step

An efficient `sum` function is already in the library. But for `size` we can use a “compiled” version hand-written in Python to speed up evaluation and make the trace more readable.


```python
from joy.library import SimpleFunctionWrapper
from joy.utils.stack import iter_stack


@SimpleFunctionWrapper
def size(stack):
    '''Return the size of the sequence on the stack.'''
    sequence, stack = stack
    n = 0
    for _ in iter_stack(sequence):
        n += 1
    return n, stack
```

Now we replace the old version in the dictionary with the new version, and re-evaluate the expression.


```python
D['size'] = size
```

## A shorter trace
You can see that `size` now executes in a single step.


```python
V('[23 18] average')
```

                                      . [23 18] average
                              [23 18] . average
                              [23 18] . [sum 1.0 *] [size] cleave /
                  [23 18] [sum 1.0 *] . [size] cleave /
           [23 18] [sum 1.0 *] [size] . cleave /
           [23 18] [sum 1.0 *] [size] . [i] app2 [popd] dip /
       [23 18] [sum 1.0 *] [size] [i] . app2 [popd] dip /
    [23 18] [[sum 1.0 *] [23 18]] [i] . infra first [[size] [23 18]] [i] infra first [popd] dip /
                  [23 18] [sum 1.0 *] . i [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                              [23 18] . sum 1.0 * [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                                   41 . 1.0 * [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                               41 1.0 . * [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                                 41.0 . [[23 18]] swaack first [[size] [23 18]] [i] infra first [popd] dip /
                       41.0 [[23 18]] . swaack first [[size] [23 18]] [i] infra first [popd] dip /
                       [23 18] [41.0] . first [[size] [23 18]] [i] infra first [popd] dip /
                         [23 18] 41.0 . [[size] [23 18]] [i] infra first [popd] dip /
        [23 18] 41.0 [[size] [23 18]] . [i] infra first [popd] dip /
    [23 18] 41.0 [[size] [23 18]] [i] . infra first [popd] dip /
                       [23 18] [size] . i [41.0 [23 18]] swaack first [popd] dip /
                              [23 18] . size [41.0 [23 18]] swaack first [popd] dip /
                                    2 . [41.0 [23 18]] swaack first [popd] dip /
                     2 [41.0 [23 18]] . swaack first [popd] dip /
                     [23 18] 41.0 [2] . first [popd] dip /
                       [23 18] 41.0 2 . [popd] dip /
                [23 18] 41.0 2 [popd] . dip /
                         [23 18] 41.0 . popd 2 /
                                 41.0 . 2 /
                               41.0 2 . /
                                 20.5 . 
