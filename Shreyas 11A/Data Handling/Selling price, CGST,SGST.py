#finding sgst and cgst
n=input("Enter item name : ")
sp,R=float(input("Enter the selling price : ")), float(input("Enter % :"))
print("-------------")
print("Item:",n)
print("CGST=",(sp*(R/100)))
print("SGST=",(sp*(R/100)))
print("Total =",(2*(sp*(R/100)))+sp)
                                
