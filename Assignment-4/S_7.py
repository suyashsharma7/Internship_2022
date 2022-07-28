def minion_game(string):
    # your code goes here
    s = string
    kev = 0 
    stu = 0
    for i in range(len(s)):
        
        if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
            kev += len(s)-i
        else:
            stu += len(s)-i
    if kev>stu:
        print('Kevin',kev)
    elif kev<stu:
        print('Stuart',stu)
    else:
        print('Draw')

if __name__ == '__main__':