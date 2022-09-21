import Maze
def __init__(self):
    my_maze = Maze()

def main():
    try:
        file_name = input("Enter file name: ")
    except:
        print("File not found")
    executive(file_name)

def executive(file_name):
    input_file = open(f"{file_name}")
    maze_info = []
    for line in input_file:
        each_string = []
        for string in line.split(" "):
            each_string.append(string.rstrip("\n"))
        maze_info.append(each_string)
    rows = int(maze_info[0][0])
    if rows < 1:
        raise RuntimeError("Rows error")
    cols = int(maze_info[0][1])
    if cols < 1:
        raise RuntimeError("Columns error")
    s_rows = int(maze_info[1][0])
    if s_rows >= rows or s_rows < 0:
        raise RuntimeError("Incorrect index row for starting position")
    s_cols = int(maze_info[1][1])
    if s_cols >= cols or s_cols < 0:
        raise RuntimeError("Incorrect index column for starting position")
    maze_info.pop(0)
    maze_info.pop(0)
    print(maze_info)

    for each_char in maze_info:
        print(each_char)

main()
