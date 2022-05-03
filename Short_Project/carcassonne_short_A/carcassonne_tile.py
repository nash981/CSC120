class CarcassonneTile:
    def __init__(self, North, East, South, West, Centre = None):
        self._North = North
        self._East = East
        self._South = South
        self._West = West
        self._Centre = Centre
        self._Reference = [self._North, self._East, self._South, self._West]

    def get_edge(self, side):
        if side == 0:
            return self._North
        elif side == 1:
            return self._East
        elif side == 2:
            return self._South
        elif side == 3:
            return self._West

    def edge_has_road(self, side):
        if (side == 0 and self._North == "grass+road") or \
                (side == 1 and self._East == "grass+road") or \
                (side == 2 and self._South == "grass+road") or \
                (side == 3 and self._West == "grass+road"):
            return True
        else:
            return False

    def edge_has_city(self, side):
        if (side == 0 and self._North == "city") or \
                (side == 1 and self._East == "city") or \
                (side == 2 and self._South == "city") or \
                (side == 3 and self._West == "city"):
            return True
        else:
            return False

    def has_crossroads(self):
        if self._Centre == "crossroad":
            return True
        else:
            return False

    def road_get_connection(self, from_side):
        if self._Centre == "crossroad":
            return -1
        elif self._Centre == "grass+road":
            if self._North == "grass+road" and from_side != 0:
                return 0
            elif self._East == "grass+road" and from_side != 1:
                return 1
            elif self._South == "grass+road" and from_side != 2:
                return 2
            elif self._West == "grass+road" and from_side != 3:
                return 3

    def city_connects(self, sideA, sideB):
        if self._Centre == "city" or self._Centre == "grass+road":
            if self._Reference[sideA] == self._Reference[sideB]:
                return True
        elif sideA == sideB:
            return True
        return False


tile01 = CarcassonneTile("city", "grass+road", "grass", "grass+road",
                         "grass+road")
tile02 = CarcassonneTile("city", "city", "grass", "city", "city")
tile03 = CarcassonneTile("grass+road", "grass+road", "grass+road",
                         "grass+road", "crossroad")
tile04 = CarcassonneTile("city", "grass+road", "grass+road", "grass",
                         "grass+road")
