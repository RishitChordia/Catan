# Balanced Catan Board Generator
Creating a balanced catan board setup with random hexes and number tokens each time.
Makes sure no particular intersections, areas of the board or particular resources are too rich or too poor.
Avoids hexes of the same resource being all next to each other or getting the same number tokens.
Customizable as per your needs.

## How to use:
Make sure you have tkinter installed.
### To generate a single board for use
- Run the main.py file, a board will be displayed soon.
### To create multiple boards and save them for later
- Run the main.py file and click on the board once created. It will generate another board.
- You can find all the boards in the catan_boards folder later, copy them elsewhere for your use.
### To generate setups for the extension board
- Go to main.py and comment out the draw_board function calls on lines 21 and 48.
- Then uncomment the draw_board function calls right after these lines.
- Then go to catan_board.py and change the global variables at the top as indicated.
