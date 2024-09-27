# WordleSolver
Small unoptimized Wordle solver.

# Usage
Pretty self-explanatory.
launch program using python :
```
python3 solver.py
```
Start by entering your starting word. The NYTimes bot recommends "Slate" as a starting word.
Each turn, enter in the website the word given to you by the solver, then give the solver the hints received, in the following format:

'-' represents a non-existent letter.

'x' represents a misplaced letter.

'o' represents a correctly placed letter.

You can replace dict file by any other dictionary of 5-letters-long words you'd like. Not my fault if no solutions are found if you do tho.

Disclaimer : I do not guarantee that a solution will be found with the default dictionary provided with this program.
