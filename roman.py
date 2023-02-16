def roman_to_int(current_roman:str)->int:
    res=0
    roman_dict ={'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for roman_symvol in roman_dict:
        res += roman_dict[roman_symvol] * current_roman.count(roman_symvol)
        # print(roman_dict[roman_symvol], current_roman.count(roman_symvol), res)
        current_roman = current_roman.replace(roman_symvol, '')
    return res

def int_to_roman(num:int)->str:
    info=['I', 'X', 'C', 'M']
    #      0    1    2    3   
    weird_number=''# 58 LVIII XXXXXIIIIIIII
    i=0
    while num != 0:
        n=num%10
        weird_number=info[i]*n+weird_number
        num//=10
        i+=1
    res=weird_number
    res=res.replace('IIIIIIIII','IX')
    res=res.replace('IIIII', 'V')
    res=res.replace('IIII', 'IV')
    res=res.replace('XXXXXXXXX','XC')
    res=res.replace('XXXXX','L')
    res=res.replace('XXXX','XL')
    res=res.replace('CCCCCCCCC','CM')
    res=res.replace('CCCCC','D')
    res=res.replace('CCCC','CD')
    return res


