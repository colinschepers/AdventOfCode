# Advent of Code

[Advent of Code](https://adventofcode.com/) is an advent calendar of small programming puzzles for a 
variety of skill sets and skill levels that can be solved in any programming language. 

This Python application contains algorithms to solve the challenges of Advent of Code 2020 and 2021. 
Additionally, there are unit tests to test the validity of the solutions and the performance of 
each algorithm. 

## Getting Started

Follow the steps below to get started:

1. Install python (>=3.8)
2. Install dependencies: `pip install -r requirements.txt`
3. Set the environment variable `SESSION_COOKIE` to the cookie from the website (after logging in).

To execute an algorithm for a specific challenge, either run the corresponding file in the `challenges` 
folder or run the script `run.py` in the root of the project:

```
usage: run.py [-h] [-y YEAR] [-d DAY]

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR
  -d DAY, --day DAY
```

## Code Quality

### Testing validity

Using pytest in combination with its parametrize feature and unittest's mock module, each algorithm
is given an example (as given on the website for the specific problem) and checks if the 
expected output is returned. 

<p><div style="text-align:center;"><iframe src="https://colinschepers.github.io/AdventOfCode/tests/results/test_examples.html" width="100%" height="400pt"></iframe></div></p>

### Measuring performance

With a similar testing framework as described in the previous section, each algorithm is executed given 
the actual inputs from the website and are checked whether they finish in a reasonable amount of time. On my private
laptop with decent specifications all 50 algorithms finish in approximately half a minute. 

<p><div style="text-align:center;"><iframe src="https://colinschepers.github.io/AdventOfCode/tests/results/test_running_times.html" width="100%" height="400pt"></iframe></div></p>
