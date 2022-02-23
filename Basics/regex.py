import re 
txt = "the rain in Spain"
print("the sentence is : \'"+txt+"\'")
print('\nusing'+' re.findall(\"ai\",txt)')
x =re.findall("ai",txt)
print(x)

x = re.search("ai",txt)
print(x)

print("\nsplit")
x = re.split("\s",txt)
print(x)

print("\nsubstitute")
x = re.sub("\s","@",txt)
print(x)
