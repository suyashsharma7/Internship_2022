if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
                
        l.append([score,name])
    ans=[]
    x=min(l)[0]
    res = []
    for i in l:
    
        if i[0] !=x:
            res.append(i)

    mn = 10e5
    for i in res:
        
        if i[0]<mn:
            ans = [i[1]]
            mn = i[0]
        elif i[0]==mn:
            ans.append(i[1])
        
        ans.sort()
   
    for i in ans:
        print(i)

                
                
            
                
                
