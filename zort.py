for i in range(int(input())):
    x, y = map(int, input().split())
    if((x+y)%3==0):
        if(min(x,y)*2<max(x,y)): print("Yes")
        else: print("NO")
    else: print("NO")
