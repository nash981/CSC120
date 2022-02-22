def set_val(val):
    if val < 0:
        return 0
    elif val > 255:
        return 255
    else:
        return val


class Color:
    def __init__(self, r, g, b):
        self.r = set_val(r)
        self.g = set_val(g)
        self.b = set_val(b)

    def __str__(self):
        string = f"rgb({self.r},{self.g},{self.b})"
        return string

    def html_hex_color(self):
        hex_r = hex(self.r)
        hex_g = hex(self.g)
        hex_b = hex(self.b)
        if len(hex_r) != 4:
            hex_red = "0"
            hex_red += hex_r[-1]
        else:
            hex_red = hex_r[-2:]
        if len(hex_g) != 4:
            hex_green = "0"
            hex_green += hex_g[-1]
        else:
            hex_green = hex_g[-2:]
        if len(hex_b) != 4:
            hex_blue = "0"
            hex_blue += hex_b[-1]
        else:
            hex_blue = hex_b[-2:]

        string = f"#{hex_red}{hex_green}{hex_blue}".upper()
        return string

    def get_rgb(self):
        x = (self.r, self.g, self.b)
        return x

    def set_standard_color(self, name):
        name = name.lower()
        if name == "white":
            self.r = 255
            self.g = 255
            self.b = 255
        elif name == "red":
            self.r = 255
            self.g = 0
            self.b = 0
        elif name == "yellow":
            self.r = 255
            self.g = 255
            self.b = 0
        elif name == "black":
            self.r = 0
            self.g = 0
            self.b = 0

    def remove_red(self):
        self.r = 0
