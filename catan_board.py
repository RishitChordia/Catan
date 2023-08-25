import random
from resource_type import Resource
from hex import Hex


class HexNode:
    def __init__(self, hex, coordinates = None):
        self.hex: Hex = hex
        self.coordinates: tuple[int] = coordinates
        self.neighbors: list[HexNode] = []

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

    def get_balanced_board(self):
        resource_board = []
        hex_node_map: dict[tuple[int], HexNode] = dict()
        while True:
            resource_board = []
            hexes = self.__get_shuffled_resources()
            hex_index = 0
            for index_i, i in enumerate(self.board):
                hex_row = []
                for index_j, j in i:
                    hex_row.append(HexNode(Hex(hexes[hex_index]), (index_i,index_j)))
                    hex_node_map[(index_i, index_j)] = hex_row[-1]
                    hex_index += 1
                resource_board.append(hex_row)
                
            print(hex_node_map, sep="\n")
            # hex_node_graph = self.get_hex_nodes(resource_board)
            
            if self.resource_balance_score(hex_node_graph) < float('inf'):
                break
        
        print(resource_board)
        while True:
            numbers = self.__get_shuffled_numbers()
            number_index = 0
            for i in resource_board:
                for j in i:
                    if hexes[hex_index] == Resource.DESERT:
                        hex_row.append(Hex(hexes[hex_index]))
                        hex_index += 1
                        continue
                    hex_row.append(Hex(hexes[hex_index], numbers[number_index]))
                    hex_index += 1
                    number_index += 1
                resource_board.append(hex_row)
                
            hex_node_graph = self.get_hex_nodes(resource_board)
            
            if self.resource_balance_score(hex_node_graph) < float('inf'):
                break
    
    # def get_hex_nodes(self):
    #     for i in 

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


CatanBoard().get_random_board()

# first make adjacent hex logic
# check number of times a resource is adjacent to itself, divide that by 2 to actually find adjacencies, it cant be more than 1 
# that is it, nothing more for resource spreading
# balanced board - check if 2 poors or 2 reds not adjacent
# balance resources, locations, number repetitions