class Process:
    def __init__(self, id, time, shift, parent=None):
        self.id = id
        self.time = time
        self.shift = shift
        self.end = shift + time 
        self.parent = parent

    def shift(self, new_shift):
        self.shift = new_shift
    
    def start_end(self):
        return self.end - self.time + 1, self.end

file = open(r"D:\Study\egeinfo\22\10592\1.txt")

for i in file:
    print(list(map(int, i.split("\t"))))