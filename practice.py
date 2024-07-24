
endno = int(input("enter end number: "))
divisibleno = int(input("divided by : "))
startno = 0
finalresult = 0
while 0<=endno:
    if endno%divisibleno==0:
        finalresult=finalresult+endno
        divisibleno=divisibleno+1
    else:
        print(finalresult)