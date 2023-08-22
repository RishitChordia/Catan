
def bfs(starti, startj, endi, endj, mat):
    directions = [[0,1] , [1,0] , [0,-1] , [-1,0]]
    curr_coordinates = [[starti, startj]]
    reached = [[starti, startj]]
    while len(curr_coordinates) > 0:
        print(curr_coordinates)
        print("\n")
        next_coordinates = []
        for coordinate in curr_coordinates:
            i = coordinate[0]
            j = coordinate[1]
            for direction in directions:
                new_coordinate_i = i + direction[0]
                new_coordinate_j = j + direction[1]
                # i,j
                # directions = [[0,1] , [1,0] , [0,-1] , [-1,0]]
                # i+0 , j+1
                # i+1 , j+0
                # i+0 , j-1
                # i-1 , j+0
                
                # checking if coordinate is out of matrix, if it is, i continue to next iteration
                if new_coordinate_i < 0 or new_coordinate_i > 4:
                    continue
                if new_coordinate_j < 0 or new_coordinate_j > 4:
                    continue
                # checking if i can travel to this new coordinate, that is, if it is zero, if not, i continue to next iteration
                if mat[new_coordinate_i][new_coordinate_j] != 0:
                    continue
                
                already_reached = False
                for coordinate in reached:
                    if coordinate[0] == new_coordinate_i and coordinate[1] == new_coordinate_j:
                        already_reached = True
                        break
                    
                if already_reached:
                    continue
                
                if new_coordinate_i == endi and new_coordinate_j == endj:
                    return True
                
                next_coordinates.append([new_coordinate_i, new_coordinate_j])
                reached.append([new_coordinate_i, new_coordinate_j])
                
        curr_coordinates = next_coordinates
    
    return False
    # curr_coordinates = [ [0,0] , [1,1] , [1,0] , [2,3] , [4,0] , ..... kitne bhi]
        

mat = [
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]

print(bfs(0,0,4,4,mat))

