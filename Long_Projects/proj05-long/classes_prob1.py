class Simplest:
    def __init__(self, p, q, r):
        self.a = p
        self.b = q
        self.c = r


class Rotate:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def get_third(self):
        return self.third

    def rotate(self):
        temp = self.first
        self.first = self.second
        self.second = self.third
        self.third = temp


class Band:
    def __init__(self, singer):
        self.singer = singer
        self.drummer = None
        self.guitar = []

    def get_singer(self):
        return self.singer

    def set_singer(self, new_singer):
        self.singer = new_singer

    def get_drummer(self):
        return self.drummer

    def set_drummer(self, new_drummer):
        self.drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self.guitar.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self.guitar = []

    def get_guitar_players(self):
        out_list = []
        for i in range(len(self.guitar)):
            out_list.append(self.guitar[i])
        return out_list

    def play_music(self):
        if self.singer == "Frank Sinatra":
            print("Do be do be do")
        elif self.singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")
        if self.drummer is not None:
            print("Bang bang bang!")
        if len(self.guitar) >0:
            for i in range(len(self.guitar)):
                print("Strum!")


