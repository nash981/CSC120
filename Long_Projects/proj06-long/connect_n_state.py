class Connect_N_State:
    def __init__(self, wid, hei, target, players):
        self._width = wid
        self._height = hei
        self._target = target
        self._playah = players

    def get_size(self):
        x = (self._width, self._height)
        return x

    def get_target(self):
        return self._target

    def get_player_list(self):
        return self._playah
