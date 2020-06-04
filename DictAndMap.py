n = int(input())
dict ={}
for i in range(n):
    k,v = map(str,input().split())
    dict[k] = v
while True:
    try:
        name = input()
        if name in dict:
            print(name+"="+dict[name])
        else:
            print('Not found')
    except:
        break
