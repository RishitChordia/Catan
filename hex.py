from resource_type import Resource


class Hex:
    def __init__(self, resource_type=Resource.DESERT, number_token=None):
        self.resource_type = resource_type
        self.number_token = number_token

    def __repr__(self) -> str:
        return str(self.resource_type) + " -> " + str(self.number_token)
