def square_footage():
        length = int(input('\nPlease enter the length of the house in feet -----> \n'))
        width = int(input('Please enter the width of the house in feet -----> \n'))
        total_area = length * width
        return total_area   

def circumference_circle():
        import math
        r = float(input('Please enter the raadius of the circle you would like to calculate the circumference for : --- >  '))
        circ = float(((2 * math.pi) * r))
        return circ
    
