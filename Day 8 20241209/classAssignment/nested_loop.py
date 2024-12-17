# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*"*i)


for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print("\n")



# password generator "abcd" a,b,c,d,aa,ab,ac,ad,ba,bb,bc,bd,ca,cb,cc,cd,da,db,dc,dd,aaa,aab,aac,aad,aba,abb,abc,abd,aca
superset="abcd"

for i1 in superset:
    print(i1)
for i2 in superset:
    for j2 in superset:
        print(i2,j2)
for i3 in superset:
    for j3 in superset:
        for k3 in superset:
            print(i3,j3,k3)
for i4 in superset:
    for j4 in superset:
        for k4 in superset:
            for l4 in superset:
                print(i4,j4,k4,l4)