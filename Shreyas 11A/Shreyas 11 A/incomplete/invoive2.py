
x=1
while( x ==1 ):
    titlename="Item.name"
    titleprice="Price"
    titlegst="GST"
    titlequantity="Quantity"
    titletotal="Total"
    A=str(input("enter the item name"))
    B=int(input("enter the  price"))
    C=(B*9)/100
    D=int(input("enter the quantity"))
    E=C+B
    x=int(input("enter 1 to continue and 2 to finish"))
    print("%-15s %-15s %-15s %-15s %-s" %(titlename, titleprice, titlegst, titlequantity, titletotal))
    print("%-15s %-15s %-15s %-15s %-s" % (A, B, C, D, E))

