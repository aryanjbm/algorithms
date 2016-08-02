
def find_lcs(x,y):
    i=len(x)
    j=len(y)
    cost=[]
    s=[]
    for k in range(i+1):
        temp=[]
        for l in range(j+1):
            temp.append(None)

        cost.append(temp)

    for k in range(i+1):
        temp=[]
        for l in range(j+1):
            temp.append(None)

        s.append(temp)

    for k in range(i+1):
        cost[k][0]=0


    for l in range(j+1):
        cost[0][l]=0

##
##    for k in range(i):
##        print(cost[k])



    for k in range(1,i+1):
        for l in range(1,j+1):
            if x[k-1]==y[l-1]:
                cost[k][l]=cost[k-1][l-1]+1
                s[k][l]="d"
            elif cost[k-1][l]>=cost[k][l-1]:
                cost[k][l]=cost[k-1][l]
                s[k][l]="u"
            else:
                cost[k][l]=cost[k][l-1]
                s[k][l]="l"



    return cost,s


    
def print_lcs(x,s,i,j):
    
    if i==0 or j==0:
     
        return

    elif s[i][j]=="d":
        print_lcs(x,s,i-1,j-1)
     
        print(x[i-1],end=" ")
    elif s[i][j]=="u":
      
        print_lcs(x,s,i-1,j)
    else:
        print_lcs(x,s,i,j-1)

def print_lcs_without_memo(x,y,c,i,j):
    if i==0 or j==0:
        return
    elif x[i-1]==y[j-1]:
        print_lcs_without_memo(x,y,c,i-1,j-1)
        print(x[i-1],end=" ")
    elif c[i-1][j]>=c[i][j-1]:
        print_lcs_without_memo(x,y,c,i-1,j)

    else:
        print_lcs_without_memo(x,y,c,i,j-1)

    



x = "character"
y = "retcarahc"

c,s=find_lcs(x,y)

print_lcs_without_memo(x,y,c,len(x),len(y))


