
import random
from resource_type import Resource
from hex import Hex


# class HexNode(Hex):
#     def __init__(self):
#         super().__init__()

#     def __repr__(self) -> str:
#         return super().__repr__()


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
        pass
    
    
    def get_random_board(self):
        hexes = self.__get_shuffled_resources()
        numbers = self.__get_shuffled_numbers()
        print(hexes, numbers)
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
        
                
        
        
    def __get_shuffled_resources(self):
        hexes = []
        for resource in self.resource_counts:
            hexes.extend([resource]*self.resource_counts[resource])
        random.shuffle(hexes)       
        return hexes
    
    def __get_shuffled_numbers(self):
        numbers = []
        for number in self.token_numbers:
            numbers.extend([number]*self.token_numbers[number])
        random.shuffle(numbers)
        return numbers
    

CatanBoard().get_random_board()


