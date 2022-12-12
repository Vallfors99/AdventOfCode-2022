import numpy as np
with open("day8\input.txt") as infile:
    lines = [[int(elem) for elem in line.strip()] for line in infile]
grid = np.array(lines)
visibility_grid = np.zeros(grid.shape)

visibility_scores = {}
for row in range(len(grid)):
    for col in range(len(grid[0])):
        # define tree parameters
        tree_height = grid[row][col]
        left_row = grid[row][0:col][::-1]
        right_row = grid[row][col+1:len(grid[0])]
        up_row = grid[:,col][0:row][::-1]
        down_row = grid[:,col][row+1:len(grid)]

        # get visibility score
        direction_scores = []
        for trees in left_row,right_row,up_row,down_row:
            direction_score = 0
            for i in range(len(trees)):
                if trees[i] >= tree_height:
                    direction_score +=1
                    break
                else:
                    direction_score += 1

            direction_scores.append(direction_score)
        # save visibility score
        visibility_score = direction_scores[0]*direction_scores[1]*direction_scores[2]*direction_scores[3]
        visibility_scores[(row,col)] = visibility_score
        visibility_grid[row,col] = visibility_score
print(visibility_grid)
print(max(visibility_scores.values()))
