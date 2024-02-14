def openfile(name):
    f = open(name, 'r', encoding='utf-8')
    characters = []
    for i in range(1, 501):
        characters.append(f.readline().strip().split('$'))
        for c in range(4):
            characters[i][c] = str(characters[i][c])
    return characters


def hash(ngnc):
    h = 0
    p = 65
    m = 10 ** 9 + 9
    st = 0
    alph = ['1234567890:-QWERTYUIOPASDFGHJKLZXCVBNNMqwertyuiopasdfghjklzxcvbnm']
    for x in ngnc:
        h += (alph.index(x) * p ** st) % m
        st += 1
    return h



def writefile(name):
    f = open(name,'w', encoding='utf-8')
    f.write(str(characters[i][0]) + '$' + str(characters[i][1] +'\n'))
    for i in range(1,501):
        f.write(str(characters[i][0])+'$'+str(characters[i][1]+'\n'))
    f.close()



characters = openfile('C:\Users\student\PycharmProjects\predprof_14.02.2024\game.txt')
print(characters)
writefile('C:\Users\student\Downloads\game_with_hash.csv')
