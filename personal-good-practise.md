# Personal understanding of good-practise

* Use function annotations.
* Use logging module.(Define stream or file logging)
* Use Makefile with mypy, pylint , unittest.
* Unittest should use mocking instead of real objects, basically prevent doing any integration test.
* Multiprocessing over multithreading in cpu intensive tasks.
* Using Deque instead of Queue.
* Using numpy arrays as compared to lists due to continous memory allocation.
* Using Dictionaries more often.
* Iteration over Recursion.

## Parallel-Processing

* Better to use ProcessPoolExecutor over manually handling processes.
* Use locks when dealing with files in multiprocessing/multithreading

## Python Style Guide

* (https://google.github.io/styleguide/pyguide.html)[Google's Style Guide - Must Check out!!!]

## Pathlib vs os.path

* (How to make paths in python more clean?)[https://pbpython.com/pathlib-intro.html]
