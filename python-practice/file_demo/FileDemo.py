import os

with open("sample.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("fjhjh hff jhfjdhf jhjhfs jhgf")

with open("sample.txt", encoding="utf-8") as MyFile:
    print(MyFile.read())

print(myfile.closed)
print(myfile.name)
print(myfile.mode)
os.rename("sample.txt", "sample1.txt")
#os.remove("sample1.txt")