Maze Solver made using Python
-----------------------------

Description:

This project uses the Tkinter framework to graphically display a randomized (unless supplied with a given seed) maze which the program then traverses to determine whether or not is solvable. The graphical interface uses a red line to display the solution path and a gray line to display cells in the maze which were traveresed but weren't used in the final solution path.

How to use:

num_rows = set to amount of desired rows of cells for the maze

num_cols = set to amount of desired columns of cells for the maze

margin = set to amount of pixels to offset maze from the border of the graphical interface

screen_x = set to amount of desired horizontal pixels to display the graphical interface

screen_y = set to amount of desired vertical pixels to display the graphical interface

cell_size_x = (screen_x - 2 * margin) / num_cols -> default formula to set the desired horizontal size of each cell in the maze

cell_size_y = (screen_y - 2 * margin) / num_rows -> default formula to set the desired vertical size of each cell in the maze

win = Window(screen_x, screen_y) -> Used to create a window for the graphical display (can be set in constructor call of Maze)

maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed) -> Creates a maze using the specified arguments above, the final argument "seed" is optional but is used to prevent the randomization of the maze layout, if not specified the maze layout will be randomly generated upon each run of the code

win.wait_for_close() -> Place at the end of the main() function to prevent the graphical interface from closing upon maze completion

Testing:

The tests.py file is used to write tests for the functions in the code, can be ignored or used to further test functionality
