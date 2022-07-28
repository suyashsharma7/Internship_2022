def swap_case(s):
    s1 = s
    ans=''
    for i in range(len(s)):
        if s[i].isalnum():
            if s[i].lower()==s1[i]:
                ans+=s1[i].upper()
            else:
                ans +=s1[i].lower()
        else:
            ans+=s[i]
                 
    return ans

if __name__ == '__main__':