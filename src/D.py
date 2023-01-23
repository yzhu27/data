class DATA:
    def __init__(self , src):
        self.rows = {}
        self.cols = None
        def fun(x):
            self.add(x)
        if type(src) == str:
            csv(src , fun)
        else:
            if src:
                map(src , fun)
            else:
                map({} , fun)
    
    def add(self , t):
        if self.cols:
            t = t.cells and t or ROW(t)
            push(self.rows , t)
            self.cols.add(t) #COLS.add()
        else:
            self.cols = COLS(t)
    
    def stats(self , what , cols , nPlaces):
        def fun(k , col):
            if what == 'div':
                return col.rnd(col.div(col) , nPlaces) , col.txt
            else:
                return col.rnd(col.mid(col) , nPlaces) , col.txt
        return kap(cols or self.cols.y , fun)

        

