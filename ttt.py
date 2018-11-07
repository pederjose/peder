print("""

  _____________________
  ##   TIC TAC TOE   ##
  ##      OYUNU      ##
  ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ
    ________________
    |   a   b   c  |
    |1  X   O   _  |  >> X: a1 / O: b1
    |2  _   X   _  |  >> X: b2
    |3  _   _   O  |  >> O: c3
    ˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
""")

tablo=[
['| ','a','b','c','|'],
['|1','_','_','_','|'],
['|2','_','_','_','|'],
['|3','_','_','_','|']
]
secimler = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

def yazdirma():
    print(' '*3,'______________')
    for i in tablo:
        print(' '*2, *i, sep='  ')
    print(' '*3,'˜˜˜˜˜˜˜˜˜˜˜˜˜˜')

def fonksiyon_X():
    a = 1
    while a==1:
        X_icin = input('X koymak istediginiz yeri secin: ')
        if X_icin in secimler:
            secimler.remove(X_icin)
            if X_icin=='a1':
                tablo[1][1]='X'
            if X_icin=='a2':
                tablo[2][1]='X'
            if X_icin=='a3':
                tablo[3][1]='X'
            if X_icin=='b1':
                tablo[1][2]='X'
            if X_icin=='b2':
                tablo[2][2]='X'
            if X_icin=='b3':
                tablo[3][2]='X'
            if X_icin=='c1':
                tablo[1][3]='X'
            if X_icin=='c2':
                tablo[2][3]='X'
            if X_icin=='c3':
                tablo[3][3]='X'
            a+=1
        else:
            print('Orasi dolu! Baska bir yer secin')
    print(secimler)
    yazdirma()

def fonksiyon_O():
    a = 1
    while a==1:
        O_icin = input('O isaretini koymak istediginiz yeri secin: ')
        if O_icin in secimler:
            secimler.remove(O_icin)
            if O_icin=='a1':
                tablo[1][1]='O'
            if O_icin=='a2':
                tablo[2][1]='O'
            if O_icin=='a3':
                tablo[3][1]='O'
            if O_icin=='b1':
                tablo[1][2]='O'
            if O_icin=='b2':
                tablo[2][2]='O'
            if O_icin=='b3':
                tablo[3][2]='O'
            if O_icin=='c1':
                tablo[1][3]='O'
            if O_icin=='c2':
                tablo[2][3]='O'
            if O_icin=='c3':
                tablo[3][3]='O'
            a+=1
        else:
            print('Orasi dolu! Baska bir yer secin')
    print(secimler)
    yazdirma()

fonksiyon_X()
fonksiyon_O()
fonksiyon_X()
fonksiyon_O()
fonksiyon_X()
fonksiyon_O()
fonksiyon_X()
fonksiyon_O()
fonksiyon_X()

a = [tablo[1][1],tablo[1][2],tablo[1][3]]
b = [tablo[2][1],tablo[2][2],tablo[2][3]]
c = [tablo[3][1],tablo[3][2],tablo[3][3]]
d = [tablo[1][1],tablo[2][1],tablo[3][1]]
e = [tablo[1][2],tablo[2][2],tablo[3][2]]
f = [tablo[1][3],tablo[2][3],tablo[3][3]]
g = [tablo[1][1],tablo[2][2],tablo[3][3]]
h = [tablo[1][3],tablo[2][2],tablo[3][1]]
sayi_X=['X','X','X']
sayi_O=['O','O','O']
kazanma = [a,b,c,d,e,f,g,h]

if kazanma.count(sayi_X)> kazanma.count(sayi_O):
    print('"X" KAZANDI !!')
elif kazanma.count(sayi_O)> kazanma.count(sayi_X):
    print('"O" KAZANDI !!')
else:
    print('KAZANAN YOK TEKRAR OYNAYIN !!')
