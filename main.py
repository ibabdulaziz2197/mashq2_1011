# 8
matn = input('Matn kirit: ')

if matn[0] == 'a' or matn[0] == 'A':
    print('YES')
else:
    print('NO')

# 9
matn = "salom dunyo"

count = 0
for i in range(len(matn)):
    if matn[i] == 'a':
        count += 1

print(f"a lar soni: {count}")


# 10
matn = "salom Aziza"
print(matn)

print(matn[:: -1])


# 11
ism = input('Ism kirit')
familya = input('Familya kirit')
natija = ism + familya
print(natija)
