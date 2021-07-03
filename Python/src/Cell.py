#!usr/bin/env python3
#連結リスト

class Cell:
    def __init__(self,x,y):
        self.data = x
        self.next = None
    
    def first(self):
        return self.data
    
    def rest(self):
        return self.next
    
    def set_first(self,x):
        self.data = x

    def set_rest(self,x):
        self.next = x

class LinkedLisat:

    def __init__(self):

        self.top = None

    def insert(self,x,y):

        if n == 0 or not self.top:
            self.top = Cell(x,self.top)
        else:
            cp = self.top
            while cp.rest():
                n -= 1
                if n == 0:
                    break
                cp = cp.rest()
            new_cp = Cell(x,cp.rest())
            cp.set_rest(new_cp)