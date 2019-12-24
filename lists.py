hamariList =["Vaibhav",  "CSE", 14, 5.10, 54];
print(hamariList);

if 14 in hamariList:
    print(14);


print(hamariList[3]);

print(len(hamariList))


print(hamariList[:4])
hamariList.append("Yamaha")
print(hamariList);

hamariList.append(" honda")
print(hamariList);

hamariList.insert(2,"Gym")
print(hamariList);

hamariList.remove("CSE");
print(hamariList)

hamariList.pop(2)
print(hamariList);

hamariList.reverse();
print("hamarilist ",hamariList);

newlist = hamariList.copy();
print("newlist: ",newlist);


# Join 2 list
sabkiList = hamariList + newlist;
print("sabkilist: ",sabkiList);



newlist.clear();
print(newlist);
