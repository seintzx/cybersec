def search_agenda(voice):
    fo = 0
    for ele in agenda:
        if voice == ele['name']:
            fo =1
            break
        
    if fo == 1:
        print(ele['name'] + "=" + ele['num'])
    else:
        print("Not found")

n = int(input().strip())
agenda = []

for i in range(n):
    entry = input().split()
    agenda.append(dict( [('name', entry[0]), ('num', entry[1])]))


while True:
    try:
        line = input()
        if line:
            search_agenda(line)
    except EOFError:
        break
