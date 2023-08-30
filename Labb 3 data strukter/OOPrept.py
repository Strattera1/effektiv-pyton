class Mouse :

    wireless = False
    def __init__(self):
        self._x_coordinate = 0
        self._y_cordinate = 0

    def __repr__(self) -> str:
        return f"x_coo"
        
    def move_right(self,amount_of_pixles = 10):
        self._x_coordinate = amount_of_pixles

    def move_left (self, amount_of_pixles = 10):
        self._x_coordinate = amount_of_pixles
        self._x_coordinate = min(0,self._x_coordinate)

    def move_up (self, amount_of_pixles = 10):
        self._y_cordinate= amount_of_pixles

    def move_down(self, amount_of_pixles = 10):
        self._y_cordinate = amount_of_pixles
        self._y_cordinate = min(0,self._y_cordinate)

        if __name__ == "__main__":

            mouse_1 = Mouse()

            print (mouse_1._x_coordinate)