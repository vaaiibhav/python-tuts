yesethogaya = {"dominor400","CBR350", "Apache310", "KTM390", "NINJA 410"};
print(yesethogaya);
print (len(yesethogaya));
# adding one item
yesethogaya.add("Suzuki Hayabausa");
print(yesethogaya);
print (len(yesethogaya));

# adding a lot of items

yesethogaya.update(["KTM DUKE","Enticer","R15","Avenger","Gixer"])
print(yesethogaya);
print (len(yesethogaya));


#remove from a set

yesethogaya.remove("Enticer");
print (yesethogaya);  

#Discard from a set
yesethogaya.discard("Avenger");
print (yesethogaya);


yesethogaya = {"dominor400","CBR350", "Apache310", "KTM390", "NINJA 410"};
yebhisethogaya={"KTM DUKE","Enticer","R15","Avenger","Gixer","dominor400","CBR350", "Apache310",};
mai_chodke_sab_set_hogaya = yesethogaya.union(yebhisethogaya);
print(mai_chodke_sab_set_hogaya);
