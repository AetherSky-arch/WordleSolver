# WordleSolver
Small unoptimized Wordle solver.

## Usage
Pretty self-explanatory.

launch program using the python interpreter :
```
python3 solver.py
```
Start by entering your starting word. The NYTimes bot recommends "Slate" as a starting word.
Each turn, enter in the website the word given to you by the solver, then give the solver the hints received, in the following format:

```
'-' represents a non-existent letter.

'x' represents a misplaced letter.

'o' represents a correctly placed letter.
```

You can replace dict file by any other dictionary of 5-letters-long words you'd like.

## How it works
To make a guess, this solver will simply pick the first word it finds in its dict file that matches the hints given so far.

## How it could be improved
- By listing all possible guesses, and making the one containing the most common letters.
- By making guesses that might not match the given hints in the second turn in order to eliminate a lot of common letters.
- By interacting directly with the Wordle webpage via a library such as selenium instead of requiring user inputs.
