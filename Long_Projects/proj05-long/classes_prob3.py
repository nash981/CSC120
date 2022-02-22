class ListNode:
    def __init__(self):
        self.na = None
        self.n = None
        self.s = None
        self.e = None
        self.w = None

    def setter(self, north, south, east, west):
        self.n = north
        self.s = south
        self.e = east
        self.w = west

    def set_name(self, name):
        self.na = name

    def get_name(self):
        return str(self.na)

    def collapse_room(self):
        if self.n is not None:
            self.n.s = None
            self.n = None
        if self.s is not None:
            self.s.n = None
            self.s = None
        if self.e is not None:
            self.e.w = None
            self.e = None
        if self.w is not None:
            self.w.e = None
            self.w = None


def populate_grid(wid, hei, obj_grid):
    north, south, east, west = None, None, None, None
    for i in range(hei):
        for j in range(wid):
            if i is 0:
                if j is 0:
                    north, south, east, west = None, obj_grid[i+1][j], \
                                               obj_grid[i][j+1], None
                elif 0 < j < wid-1:
                    north, south, east, west = None, obj_grid[i+1][j], \
                        obj_grid[i][j+1], obj_grid[i][j-1]
                elif j is wid-1:
                    north, south, east, west = None, obj_grid[i+1][j], \
                                               None, obj_grid[i][j-1]
            elif 0 < i < hei-1:
                if j is 0:
                    north, south, east, west = obj_grid[i-1][j], \
                        obj_grid[i+1][j], obj_grid[i][j+1], None
                elif 0 < j < wid-1:
                    north, south, east, west = obj_grid[i-1][j], \
                        obj_grid[i+1][j], obj_grid[i][j+1], obj_grid[i][j-1]
                elif j is wid-1:
                    north, south, east, west = obj_grid[i-1][j], \
                        obj_grid[i+1][j], None, obj_grid[i][j-1]
            elif i is hei-1:
                if j is 0:
                    north, south, east, west = obj_grid[i-1][j], None, \
                                               obj_grid[i][j+1], None
                elif 0 < j < wid-1:
                    north, south, east, west = obj_grid[i-1][j], None, \
                        obj_grid[i][j+1], obj_grid[i][j-1]
                elif j is wid-1:
                    north, south, east, west = obj_grid[i-1][j], None, \
                                               None, obj_grid[i][j-1]
            obj_grid[i][j].set_name(str(f"{i}{i}{j}"))
            obj_grid[i][j].setter(north, south, east, west)

    return obj_grid[hei-1][0]


def build_grid(wid, hei):
    obj_grid = []
    floor_list = []
    for i in range(hei):
        for j in range(wid):
            floor_list.append(ListNode())
        obj_grid.append(floor_list)
        floor_list = []
    sw_corner = populate_grid(wid, hei, obj_grid)
    return sw_corner

