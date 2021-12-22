def swap_case(s):
    result=''
    for later in s:
        if later==later.upper():
            result+=later.lower()
        else:
            result+=later.upper()
    return result
        
str=input()
print(swap_case(str))