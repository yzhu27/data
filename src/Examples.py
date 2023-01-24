## Examples

egs = {}
def eg(key, str, fun):  #--> nil; register an example.
    global help
    egs[key] = fun
    help = help + f'  -g  {key}\t{str}\n'



if __name__=='__main__':
    
    # eg("crash","show crashing behavior", function()
    #   return the.some.missing.nested.field end)
    def thefun():
        global the
        return oo(the)
    eg("the","show settings", thefun)

    def symfun():
        sym = SYM()
        for x in ["a","a","a","a","b","b","c"]:
            sym.add(x)
        return "a" == sym.mid() and 1.379 == rnd(sym.div())
    eg("sym","check syms", symfun)

    def numfun():
        num = NUM()
        for x in [1,1,1,1,2,2,3]:
            num.add(x)
        return 11/7 == num.mid() and 0.787 == rnd(num.div())
    eg("num", "check nums", numfun)

    def csvfun():
        n = 0
        def tmp(t):
            n += len(t)
        Csv(the["file"], tmp(n))
        return n==8*399
    eg("csv","read from csv", csvfun)

    def datafun():
        data = Data(the["file"])
        return len(data.rows) == 398 &\
               data.cols.y[1].w == -1 &\
               data.cols.x[1].at == 1 &\
               len(data.cols.x == 4)
    eg("data","read DATA csv", datafun)

    def statsfun():
        data = Data(the["file"])
        for k, cols in enumerate((data.cols.y, data.cols.x)):
            print(k, "mid", o(data.stats("mid", cols, 2)))
            print("", "div". o(data.stats("div", cols, 2)))
        return True
    eg("stats","stats from DATA", statsfun)



    main(the, help, egs)