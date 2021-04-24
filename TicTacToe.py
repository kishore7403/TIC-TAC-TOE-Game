print("XO GAME")
ch='1'
while(ch=='1'):
    mat=[[" " for x in range(3)] for y in range(3)]
    m,n,val=0,0,0
    def display(mat):
        for i in range(0,3):
            for j in range(0,3):
                if j<2:
                    print(mat[i][j],end="|")
                else:
                    print(mat[i][j])
            if i<2:
                print("-+-+-")
    display(mat)
    def choice():
        print("press 1.play agian  0.exit")
        ch=input()
        return(ch)
    def enter():
        m2=int(input("row:"))
        n2=int(input("col:"))
        print('\n')
        if(m2<=3 and n2<=3 and m2>0 and n2>0):
            return(m2,n2)
        else:
            print("enter valid index")
            print("give it a try again!!!")
            return(0,0)
    def assign(mat,m,n,val):
        mat[m-1][n-1]=val
        return(mat)
    def rowcheck(mat):
        i=0
        addx=0
        addo=0
        while i<3:
            for j in range(0,3):
                if mat[i][j]=='x':
                    addx=addx+1
                elif mat[i][j]=='o':
                    addo=addo+1
            if addx==3:
                print("x wins by row",i+1)
                exitr=0
                return(exitr)
            elif addo==3:
                print("o wins by row",i+1)
                exitr=0
                return(exitr)
            addo=0    
            addx=0
            i=i+1
    def colcheck(mat):
        j=0
        addx=0
        addo=0
        while j<3:
            for i in range(0,3):
                if mat[i][j]=='x':
                    addx=addx+1
                elif mat[i][j]=='o':
                    addo=addo+1
            if addx==3:
                print("x wins by col:",j+1)
                exitc=0
                return(exitc)
            elif addo==3:
                print("o wins by col:",j+1)
                exitc=0
                return(exitc)
            addo=0    
            addx=0
            j=j+1

    def rdiagnol(mat):    
        addx=0
        addo=0
        i=0
        j=2
        while i<3:
            if j>=0:
                if mat[i][j]=='x':
                    addx=addx+1
                elif mat[i][j]=='o':
                    addo=addo+1
            i=i+1
            j=j-1
        if(addx==3):
            print("x win by right diagnol (/)")
            exitrd=0
            return(exitrd)
        elif(addo==3):
            print("o win by right diagnol (/)")
            exitrd=0
            return(exitrd)
        
    def ldiagnol(mat):    
        addx=0
        addo=0
        i=0
        j=0
        while i<3:
            while j<3:
                if(i==j):
                    if mat[i][j]=='x':
                        addx=addx+1
                    elif mat[i][j]=='o':
                        addo=addo+1
                j=j+1
            i=i+1
            j=0
        if(addx==3):
            print("x win by left diagnol (\)")
            exitld=0
            return(exitld)
        elif(addo==3):
            print("o win by left diagnol (\)")
            exitld=0
            return(exitld)
            
    print("enter index")    
    for i in range(1,10):
        if i%2==0:
            val='o'
        else:
            val='x'
        print(val,"--->turn")
        m=n=0
        while(m==0 and n==0):
                m,n=enter()
        while(mat[m-1][n-1]=='x' or mat[m-1][n-1]=='o'):
            print("CHECK:space already filled with",mat[m-1][n-1])
            print("give it a try again!!!")
            m=n=0
            while(m==0 and n==0):
                m,n=enter()
        mat=assign(mat,m,n,val)
        display(mat)
        resr,resc,resld,resrd=1,1,1,1
        resr=rowcheck(mat)
        resc=colcheck(mat)
        resld=ldiagnol(mat)
        resrd=rdiagnol(mat)
        if(resr==0 or resc==0 or resld==0 or resrd==0):
            break
    if(resr!=0 and resc!=0 and resld!=0 and resrd!=0):
        print("Its a DRAW!!!!")
    print("press 1.play agian  0.exit")
    ch=input()
    while ch!='1' and ch!='0':
        print("invalid choice")
        ch=choice()
while(ch=='0'):
    print("game closed")
    break
