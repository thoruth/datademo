# Refactor the code without changing the script's behavior.
# Attach any code you used to solve the task.
# Copyright 2021 Continental AG

# The code filters and separates box labels with x0, y0, x1, y1 coordinates and a class type

PEDESTRIAN = 5
X_DIFF_MAX = 2
Y_DIFF_MAX = 12

class Coordinate():
    def __init__(self,  x0, y0, x1, y1):
        self.x0, self.y0, self.x1, self.y1 =  float(x0), float(y0), float(x1), float(y1)
        
    def __repr__(self) -> str: # for fancy styling output
        return f"Coordinate(x0={self.x0}, y0={self.y0}, x1={self.x1}, y1={self.y1})"
        
class Label():
    def __init__(self,coordinate:Coordinate, value):
        self.coordinate, self.value = coordinate, int(value)

    def __repr__(self) -> str: # for fancy styling output
        return f"Label( Coordinate={self.coordinate}, value={self.value})"

def filter_coordinate(coord:Coordinate):
    return not abs(coord.x0-coord.x1) < X_DIFF_MAX and not abs(coord.y0-coord.y1) < Y_DIFF_MAX

def parse_label(label:str) -> Label:
    obj = label.split(",")
    return Label(coordinate=Coordinate(*obj[:-1]), value=obj[-1])
        
def main(labels):
    # parse
    parsed_labels : list[Label] = [parse_label(label)for label in labels]
        
    # filter small labels
    res2 = [ label for label in parsed_labels if filter_coordinate(label.coordinate)]
    
    # filter pedestrian, label value  equal 5
    res3 = [ label for label in parsed_labels if label.value==PEDESTRIAN]
    
    return res2, res3

res = main(["0,1,2.2,3,5", "0, 0, 21, 42, 5"])
print(res)