if __name__ == '__main__':
    s = input()
    f1=f2=f3=f4=f5=0
    for i in range(len(s)):
        if s[i].isalnum():
            f1=1
    if f1==1:
        print('True')
    else:
        print('False')
    for i in range(len(s)):
        if s[i].isalpha():
            f2=1
    if f2==1:
        print('True')
    else:
        print('False')
    for i in range(len(s)):
        if s[i].isdigit():
            f3=1
    if f3==1:
        print('True')
    else:
        print('False')
    for i in range(len(s)):
        if s[i].islower():
            f4=1
    if f4==1:
        print('True')
    else:
        print('False')
    for i in range(len(s)):
        if s[i].isupper():
            f5=1
    if f5==1:
        print('True')
    else:
        print('False')
            
