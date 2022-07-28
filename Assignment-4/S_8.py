def merge_the_tools(string, k):
    # your code goes here
    l=[]
    x=0
    s = ''
    if k==1:
        for i in string:
            print(i)
    else:
        for i in range(k):
            s = string[x:k+x]
            s = list(set(s))
            l.append(''.join(s))
            x+=k
        for i in l:
            print(i)
        
        
if __name__ == '__main__':