import string

upperLetter = string.ascii_uppercase
print("輸入要加密的密鑰")
s = input().upper() #第一個輸入，作為加密的密鑰使用
code = list(set(upperLetter) - set(s))
code.sort()
ls = list(set(s))
ls.sort(key = s.index)
keys = ''.join(ls + code)
print("輸入想要加密的字串")
decode = input().upper() #第二個輸入，作為想要加密的字串使用
table = ''.maketrans(upperLetter, keys)
print("加密過後為:" + decode.translate(table))

