keys=[1,2,3,4,5,6,7]
p=[None,0.04,0.06,0.08,0.02,0.10,0.12,0.14]
q=[0.06,0.06,0.06,0.06,0.05,0.05,0.05,0.05]


def opt_bst_cost(keys,p,q):
    n=len(keys)

    e = []
    w=[]
    root=[]
    for i in range(0,n+2):
        temp=[]
        for j in range(n+1):
            temp.append(None)
        e.append(temp)
        temp2=temp[:]
        w.append(temp2)
    for i in range(0,n+1):
        temp=[]
        for j in range(n+1):
            temp.append(None)
        root.append(temp)
      


    for i in range(1,n+2):                                                                                       
        e[i][i-1]=q[i-1]
        w[i][i-1]=q[i-1]

    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j=l+i-1
            e[i][j]=float('inf')
            w[i][j]=w[i][j-1]+p[j]+q[j]
            for r in range(i,j+1):
                t = e[i][r-1]+e[r+1][j]+w[i][j]
                if t<e[i][j]:
                    e[i][j]=t
                    root[i][j]=r
    return e,root

def print_bst_left(r,i,j):
    if j==i-1:
        print("d"+str(i-1)+" is left child of k"+str(r[i][j+1])) 
        
     
        
def print_bst(r,i,j,n,parent):
    


    if j==i-1:
        if j==parent-1:
            print("d"+str(j)+" is left child of k"+str(parent))
        else:
            print("d"+str(j)+" is right child of k"+str(parent))
        return
    root=r[i][j]

    if not parent:
        root=r[i][j]
        print("k"+str(root)+" is the root")
        print_bst(r,i,root-1,n,root)
        print_bst(r,root+1,j,n,root)
        return
    if j == parent-1:
        print("k"+str(r[i][j])+" is left child of k"+str(parent))
    else:
        print("k"+str(r[i][j])+" is right child of k"+str(parent))


    print_bst(r,i,root-1,n,r[i][j])
   
    print_bst(r,root+1,j,n,r[i][j])


    
e,r  = opt_bst_cost(keys,p,q)
print(e[1][7])
print_bst(r,1,7,7,None)



