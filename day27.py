s = input()
clean = ""

for c in s:
    if c.isalnum():         
        clean += c.lower()

if clean == clean[::-1]:
    print("Yes")
else:
    print("No")