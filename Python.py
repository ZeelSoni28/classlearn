import random

# Function to generate a random maze
def generate_maze(size):
    maze = []
    for i in range(size):
        row = ['#' if random.random() < 0.3 else ' ' for _ in range(size)]
        maze.append(row)
    # Place exit at a random position
    maze[random.randint(0, size - 1)][size - 1] = 'E'
    return maze

# Function to print the maze
def print_maze(maze, player_position):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_position:
                print('P', end=' ')
            else:
                print(cell, end=' ')
        print()

# Function to check if the player has reached the exit
def is_exit_reached(player_position, maze_size):
    return player_position[1] == maze_size - 1

# Function to move the player in the maze
def move_player(direction, player_position, maze_size):
    x, y = player_position
    if direction == 'up' and x > 0:
        x -= 1
    elif direction == 'down' and x < maze_size - 1:
        x += 1
    elif direction == 'left' and y > 0:
        y -= 1
    elif direction == 'right' and y < maze_size - 1:
        y += 1
    return (x, y)

# Main function to run the game
def main():
    maze_size = 10
    player_position = (0, 0)
    maze = generate_maze(maze_size)

    print("Welcome to the Maze Game!")
    print("Find the exit 'E' to win the game.")
    print_maze(maze, player_position)

    while not is_exit_reached(player_position, maze_size):
        direction = input("Enter direction (up/down/left/right): ").lower()
        if direction in ['up', 'down', 'left', 'right']:
            player_position = move_player(direction, player_position, maze_size)
            print_maze(maze, player_position)
        else:
            print("Invalid direction! Please enter 'up', 'down', 'left', or 'right'.")

    print("Congratulations! You have reached the exit.")

if __name__ == "__main__":
    main()
