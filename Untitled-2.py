
endno = int(input("enter end number: "))
divisibleno = int(input("divided by : "))
finalresult = 0
while 0<=endno:
    if endno%divisibleno==0:
        finalresult=finalresult+endno
    endno=endno - 1
print("total of number upto ",endno ," divided by ",divisibleno," is : ", finalresult)