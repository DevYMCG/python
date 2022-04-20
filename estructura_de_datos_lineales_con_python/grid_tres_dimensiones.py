class Grid(object):

    def __init__(self, rows, columns, z, fill_value=None):
        self.data = [[['*' for k in range(z)] for j in range(columns)] for i in range(rows)]  
    
    def get_height(self):
        "Returns the number of rows."
        return len(self.data)
    
    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])
    
    def get_depth(self):
        """Returns the number of items."""
        return len(self.data[0][0])
    
    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result+= str(self.data[row][col][depth])+ " "
                result += "\n"
            result += "\n"
        
        return str(result)

if __name__ == "__main__":

    """
        6 ancho
        3 largo
        4 alto
    """
    matrix = Grid(6, 3, 4)

    print(matrix.__str__())
    print(matrix.get_height())
    print(matrix.get_width())
    print(matrix.get_depth())