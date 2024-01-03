vowel = ["a","e","i","o","u"]
word = input()+' '
count = 0
found = 0
for cha in word:
    if cha in vowel:
        found = 1
    if cha not in vowel:
        if found == 1:
            count += 1
            found = 0
    

print(count)