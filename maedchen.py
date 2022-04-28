file = open(r"C:\Users\yazan\Desktop\GPT_Aufgaben\mädchen.txt", "r")
f1, f2, f3, f4, f5, f6 = file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline()
names = f1.split() + f2.split() + f3.split() + f4.split() + f5.split() + f6.split()
print(names)

for i in names:
    if i[::1] == i[::-1]:
        names.remove(i)
for j in names:
    print(j, "-->", j[::-1])
# Die Aufgabe 4 "Jungennamen" wird auch so gelöst (Klausur gpt 20-1b.pdf)