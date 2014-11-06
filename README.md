Sudoku Solver 
=============
Takes a [sudoku puzzle](http://www.sudoku.name/rules/en) in a csv file, solves it, and prints it to a csv file in the same directory. Zeros represent empty spaces and numbers 1-9 represent filled in values of the puzzle. 


Quick Start
-----------
sudoku_solver.py takes one .csv file as an argument. 

``` bash 
python sudoku_solver.py test_board.csv
```
Resulting answer will be in 'solved_sudoku.csv' in the same directory.


Example 
--------
A .csv file containing this starting puzzle: 
``` bash 
0,3,5,2,9,0,8,6,4
0,8,2,4,1,0,7,0,3
7,6,4,3,8,0,0,9,0
2,1,8,7,3,9,0,4,0
0,0,0,8,0,4,2,3,0
0,4,3,0,5,2,9,7,0
4,0,6,5,7,1,0,0,9
3,5,9,0,2,8,4,1,7
8,0,0,9,0,0,5,2,6
```
Yields a .csv file containing this completed puzzle:
``` bash
1,3,5,2,9,7,8,6,4
9,8,2,4,1,6,7,5,3
7,6,4,3,8,5,1,9,2
2,1,8,7,3,9,6,4,5
5,9,7,8,6,4,2,3,1
6,4,3,1,5,2,9,7,8
4,2,6,5,7,1,3,8,9
3,5,9,6,2,8,4,1,7
8,7,1,9,4,3,5,2,6
```
