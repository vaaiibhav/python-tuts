# 1. it should iterate untill the user presses N
# 2.  it should total all the products
# 3. it should calculate GST as 9% on the overall bill
listitems =[];
listprices = [];

while (input("Add more Items   ") =='y'):
   
    pn=input("Add Product Name  ");
    pp=input("Add Product Price     ");
    listitems.append(pn);
    listprices.append(pp);


for lp in listitems:
    print ("item = " , listitems ,"price = " ,listprices);
    

totalprice=0;

for tlp in range(0, len(listprices)):
    totalprice =  totalprice + int(listprices[tlp]);
    
    # print ("item = " , listitems ,"price = " ,listprices);

print("totalprice" ,totalprice);    

def letsgst(tp):
    gstprice = tp*18/100;
    return gstprice;

# def totalbill():

final_bill = totalprice + letsgst(totalprice);

print("Final Price ",final_bill);



    