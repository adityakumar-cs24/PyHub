with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

word = "good"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")