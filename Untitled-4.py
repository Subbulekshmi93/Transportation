
endno = int(input("enter end number: "))
startno= int(input("enter start number: "))
finalresult = 0
while startno<=endno:
    if startno%2==0:
        finalresult=finalresult+startno
    startno=startno+1
print("total of number upto ",endno ," is : ", finalresult)