import json
from collections import deque
from typing import Dict, Tuple, List, Optional

# Define the board connections (bidirectional)
CONNECTIONS = {
    0: [1],
    1: [0, 2],
    2: [1, 4],
    3: [4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5, 7, 8],
    7: [6],
    8: [6, 9],
    9: [8, 10],
    10: [9]
}

def is_valid_state(state: str) -> bool:
    """Check if a state string is valid."""
    if len(state) != 11:
        return False
    return all(c in '012' for c in state)

def get_possible_moves(state: str) -> List[Tuple[int, int]]:
    """Get all possible moves from the current state."""
    moves = []
    empty_spaces = [i for i, c in enumerate(state) if c == '0']
    
    for from_pos in range(11):
        if state[from_pos] == '0':
            continue
            
        # Find all reachable empty spaces
        for to_pos in empty_spaces:
            if from_pos == to_pos:
                continue
                
            # Check if path is clear
            if is_path_clear(state, from_pos, to_pos):
                moves.append((from_pos, to_pos))
    
    return moves

def is_path_clear(state: str, from_pos: int, to_pos: int) -> bool:
    """Check if there's a clear path between two positions."""
    visited = set()
    queue = deque([from_pos])
    
    while queue:
        current = queue.popleft()
        if current == to_pos:
            return True
            
        visited.add(current)
        
        for neighbor in CONNECTIONS[current]:
            # Only move through empty spaces (0)
            if neighbor not in visited and state[neighbor] == '0':
                queue.append(neighbor)
    
    return False

def apply_move(state: str, move: Tuple[int, int]) -> str:
    """Apply a move to the state."""
    from_pos, to_pos = move
    state_list = list(state)
    # When moving backwards, we're actually moving the box from to_pos to from_pos
    state_list[from_pos] = state_list[to_pos]
    state_list[to_pos] = '0'
    return ''.join(state_list)

def visualize_state(state: str) -> str:
    """Visualize the state in the required format."""
    lines = [
        f"{state[3]}{state[4]}{state[5]}{state[6]}{state[7]}",
        f" {state[2]} {state[8]} ",
        f"{state[0]}{state[1]} {state[9]}{state[10]}"
    ]
    return '\n'.join(lines)

def find_shortest_paths():
    """Find shortest paths from all states to the final state."""
    final_state = "22200000111"
    start_state = "11100000222"
    
    # Map from state to (steps, next_state)
    state_map: Dict[str, Tuple[int, Optional[str]]] = {final_state: (0, None)}
    queue = deque([final_state])
    found_start = False
    steps = 0
    
    while queue and not found_start:
        current_state = queue.popleft()
        current_steps = state_map[current_state][0]
        steps += 1
        
        if steps % 1000 == 0:
            print(f"Processed {steps} states, queue size: {len(queue)}")
        
        # Try all possible moves to get to previous states
        for from_pos, to_pos in get_possible_moves(current_state):
            # Create the previous state by moving the box back
            prev_state = apply_move(current_state, (to_pos, from_pos))
            
            if prev_state not in state_map:
                state_map[prev_state] = (current_steps + 1, current_state)
                queue.append(prev_state)
                
                if prev_state == start_state:
                    found_start = True
                    print(f"Found start state after {steps} steps!")
                    break
    
    if not found_start:
        print("Could not find path from start to final state!")
        return
    
    # Save the state map
    with open('state_map.json', 'w') as f:
        json.dump(state_map, f, indent=2)
    
    # Find and save the path from start to final
    path = []
    current = start_state
    while current is not None:
        path.append(current)
        current = state_map[current][1]
    
    print(f"Found path with {len(path) - 1} steps")
    
    # Save the path visualization
    with open('shortest_path.txt', 'w') as f:
        for state in path:
            f.write(visualize_state(state))
            f.write('\n\n')

if __name__ == "__main__":
    find_shortest_paths() 