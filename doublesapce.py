sen="my name is shruti"
sen2="hello  world  "
print(sen2)
print(sen.find("  "))#returns -1(no doublespace found)
print(sen2.find("  "))#returns 5 (doublespace found at 5th index)
sen2=sen2.replace("  "," ")
print(sen2)

