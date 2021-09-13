#challenge from the looping program
#shortcut for star=star+1 is sta+=1
stars = int(input("how many stars"))
line = stars
space = 0
for i in range(line):
    for counter in range(stars):
        print("* ", end=" ")
    for j in range(space):
        print("  ", end=" ")
    space+=2
    for counter in range(stars):
        print("* ", end=" ")
        #print(counter+1, end=" ")
    print()
    stars-=1
