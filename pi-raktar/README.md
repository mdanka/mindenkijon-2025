# Pi-Raktar Puzzle Solver

This program solves the Pi-Raktar puzzle, finding the shortest path from the initial state to the final state.

## Puzzle Description

The puzzle consists of 11 squares/nodes arranged in a specific pattern. Each square can be:
- Empty (marked with 0)
- Contains a green box (marked with 1)
- Contains a brown box (marked with 2)

The squares are connected in the following way:
```
03 04 05 06 07
   02    08    
00 01    09 10
```

In one move, you can lift any one box and move it to any empty space, provided that the path to the space is empty (i.e., you can only move through empty spaces).

The goal is to get from the initial state `11100000222` to the final state `22200000111` in the minimum number of moves.

## How to Run

1. Make sure you have Python 3 installed
2. Run the solver:
   ```bash
   python puzzle_solver.py
   ```

## Output Files

The program generates two output files:

1. `state_map.json`: Contains all possible states and their distances from the final state
   - Each state is mapped to a tuple of (steps_required, next_state)
   - The steps_required is the minimum number of moves needed to reach the final state
   - The next_state is the state to move to next to reach the final state in the minimum number of moves

2. `shortest_path.txt`: Shows the sequence of states from initial to final
   - Each state is visualized in the following format:
     ```
     00000
      1 2 
     11 22
     ```
   - The first line shows positions 3,4,5,6,7
   - The second line shows positions 2 and 8
   - The third line shows positions 0,1,9,10
   - Empty spaces are shown as 0
   - Green boxes are shown as 1
   - Brown boxes are shown as 2

## Solution Interpretation

The solution shows the sequence of moves needed to transform the board from the initial state to the final state. Each move follows these rules:
1. Only one box can be moved at a time
2. Boxes can only move through empty spaces
3. The path must be clear (no other boxes blocking the way) 