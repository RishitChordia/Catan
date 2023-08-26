import random
from resource_type import Resource
from hex import Hex

# HAS TO BE MINIMUM 0 FOR REGULAR AND 4 FOR EXTENSION
MAX_ADJACENT_RESOURCES = 0
MAX_NUMBER_REPETITIONS = 1
NO_RED_ADJACENT = True
NO_SAME_ADJACENT = True


class HexNode:
    def __init__(self, hex, coordinates=None):
        self.hex: Hex = hex
        self.coordinates: tuple[int] = coordinates
        self.neighbors: set[HexNode] = set()
        
    
    def get_token_probability(self):
        return 6-abs(7-self.hex.number_token)


    def __repr__(self) -> str:
        return super().__repr__()


class CatanBoard:
    def __init__(
        self,
        board_sizes=[3, 4, 5, 4, 3],
        token_numbers={12: 1, 11: 2, 10: 2, 9: 2, 8: 2, 6: 2, 5: 2, 4: 2, 3: 2, 2: 1},
        resource_counts={
            Resource.SHEEP: 4,
            Resource.WOOD: 4,
            Resource.BRICK: 3,
            Resource.HAY: 4,
            Resource.ORE: 3,
            Resource.DESERT: 1,
        },
    ):
        self.board_sizes = board_sizes
        self.token_numbers = token_numbers
        self.board = [[Hex()] * i for i in board_sizes]
        self.rows = len(board_sizes)
        self.columns = max(i for i in board_sizes)
        self.resource_counts = resource_counts

    def __get_neighbors(self, hex_node_board, hex_node_map):
        for i, row in enumerate(hex_node_board):
            for j, hex_node in enumerate(row):
                if i > 0:
                    if (i - 1, j) in hex_node_map:
                        hex_node.neighbors.add(hex_node_map[(i - 1, j)])
                    direction = (
                        -1 if self.board_sizes[i - 1] < self.board_sizes[i] else 1
                    )
                    if (i - 1, j + direction) in hex_node_map:
                        hex_node.neighbors.add(hex_node_map[(i - 1, j + direction)])
                if i < self.rows - 1:
                    if (i + 1, j) in hex_node_map:
                        hex_node.neighbors.add(hex_node_map[(i + 1, j)])
                    direction = (
                        -1 if self.board_sizes[i + 1] < self.board_sizes[i] else 1
                    )
                    if (i + 1, j + direction) in hex_node_map:
                        hex_node.neighbors.add(hex_node_map[(i + 1, j + direction)])
                
                if (i, j + 1) in hex_node_map:
                    hex_node.neighbors.add(hex_node_map[(i, j + 1)])
                if (i, j - 1) in hex_node_map:
                    hex_node.neighbors.add(hex_node_map[(i, j - 1)])
                

    def resource_balance_score(self, hex_node_map):
        adjacency_count = 0
        for hex_node in hex_node_map.values():
            for neighbor in hex_node.neighbors:
                if neighbor.hex.resource_type == hex_node.hex.resource_type:
                    adjacency_count += 1
        
        print(adjacency_count)
        return adjacency_count


    def number_balance_score(self, hex_node_map):
        resource_numbers = dict()
        repetitions = 0
        for hex_node in hex_node_map.values():
            if not hex_node.hex.resource_type in resource_numbers:
                resource_numbers[hex_node.hex.resource_type] = set()
            if hex_node.hex.number_token in resource_numbers[hex_node.hex.resource_type]:
                repetitions += 1
            else:
                resource_numbers[hex_node.hex.resource_type].add(hex_node.hex.number_token)
        
        if repetitions > MAX_NUMBER_REPETITIONS:
            return float('inf')

        total_error = 0
        adjacent_tokens = 0
        for hex_node in hex_node_map.values():
            
            if hex_node.hex.resource_type == Resource.DESERT:
                continue
            
            token_sum = hex_node.get_token_probability()
            token_count = 1+len(hex_node.neighbors)
            tokens = [hex_node.hex.number_token]
            
            for neighbor in hex_node.neighbors:
                if neighbor.hex.resource_type == Resource.DESERT:
                    token_count -= 1
                    continue
                
                token_sum += neighbor.get_token_probability()
                
                if neighbor.hex.number_token == hex_node.hex.number_token:
                    if NO_SAME_ADJACENT:
                        print("hehe")
                        return float('inf')
                    adjacent_tokens += 1
                tokens.append(neighbor.hex.number_token)
                
            avg_token_number = token_sum/token_count
            if NO_RED_ADJACENT and ((6 in tokens and 8 in tokens) or (tokens.count(6) > 1) or (tokens.count(8) > 1)):
                print("oops")
                return float('inf')
                
            if avg_token_number <= 2:
                total_error += 2 - avg_token_number
                
            if avg_token_number >= 4:
                total_error += avg_token_number - 4
        
        print(total_error*10)
        return total_error*10
            

        
        
        
                

    def get_balanced_board(self):
        hex_node_board = []
        hex_node_map: dict[tuple[int], HexNode] = dict()
        while True:
            hex_node_board = []
            hexes = self.__get_shuffled_resources()
            hex_index = 0
            for index_i, i in enumerate(self.board):
                hex_row = []
                for index_j, j in enumerate(i):
                    hex_row.append(HexNode(Hex(hexes[hex_index]), (index_i, index_j)))
                    hex_node_map[(index_i, index_j)] = hex_row[-1]
                    hex_index += 1
                hex_node_board.append(hex_row)
            
            self.__get_neighbors(hex_node_board, hex_node_map)
            if self.resource_balance_score(hex_node_map) < MAX_ADJACENT_RESOURCES*2+1:
                break
            # count till 100 iterations, keep track of best board so far, if you dont get desired,
            # then just return the best you could do in that time to save time

        self.__get_neighbors(hex_node_board, hex_node_map)

        while True:
            numbers = self.__get_shuffled_numbers()
            number_index = 0
            for i in hex_node_board:
                for j in i:
                    if j.hex.resource_type == Resource.DESERT:
                        continue
                    j.hex.number_token = numbers[number_index]
                    number_index += 1

            if self.number_balance_score(hex_node_map) < 1:
                break

        balanced_board = [[node.hex for node in row] for row in hex_node_board]
        return balanced_board

    def get_random_board(self):
        hexes = self.__get_shuffled_resources()
        numbers = self.__get_shuffled_numbers()
        hex_index, number_index = 0, 0
        random_board = []
        for i in self.board:
            hex_row = []
            for j in i:
                if hexes[hex_index] == Resource.DESERT:
                    hex_row.append(Hex(hexes[hex_index]))
                    hex_index += 1
                    continue
                hex_row.append(Hex(hexes[hex_index], numbers[number_index]))
                hex_index += 1
                number_index += 1
            random_board.append(hex_row)
        print(random_board)
        return random_board

    def __get_shuffled_resources(self):
        hexes = []
        for resource in self.resource_counts:
            hexes.extend([resource] * self.resource_counts[resource])
        random.shuffle(hexes)
        return hexes

    def __get_shuffled_numbers(self):
        numbers = []
        for number in self.token_numbers:
            numbers.extend([number] * self.token_numbers[number])
        random.shuffle(numbers)
        return numbers


CatanBoard().get_balanced_board()

# first make adjacent hex logic
# check number of times a resource is adjacent to itself, divide that by 2 to actually find adjacencies, it cant be more than 1
# that is it, nothing more for resource spreading
# balanced board - check if 2 poors or 2 reds not adjacent
# balance resources, locations, number repetitions
