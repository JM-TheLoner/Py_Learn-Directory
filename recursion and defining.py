def spell(txt):
   return show(-1)
    
def show(m):
    print(txt[m])
    if txt.find(txt[m]) != 0:
        return next(m - 1)

def next(m):
    print(txt[m])
    if txt.find(txt[m]) != 0:
        return show(m - 1)



txt = input()
spell(txt)



#can use above or below.


def spell(txt):
    x = len(txt)
    for a in range(0,x):
        print(txt[x-1])
        x-=1
txt = input()
spell(txt)