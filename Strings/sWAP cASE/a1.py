def swap_case(s):
    a = ''
    for i in s:
        if(i.islower() == True):
            i = i.upper()
        else:
            i = i.lower()
        a=a+i
    return a
