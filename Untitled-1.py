
endno = int(input("enter end number: "))
divisibleno = int(input("divided by : "))
startno=0
finalresult = 0
while startno<=endno:
    if startno%divisibleno==0:
        finalresult=finalresult+startno    
    startno=startno+1
    
print("total of number upto ",endno ," divided by ",divisibleno," is : ", finalresult)