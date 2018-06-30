def logcheck(function):
    def printError():
        print("error")
    
    pw = int(input("pw:"))
    if pw != 2468:
        return printError
    else:
        return function

@logcheck
def foo():
    print("HI")
foo()
