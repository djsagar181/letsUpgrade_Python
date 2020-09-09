for num in range(1042000,702648295):
# lower = 1042000     #either use above for loop or use this lower and upper ans will be same
# upper = 702648295
# for num in range(lower,upper-1):
    temp=num
    order = len(str(num))
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print("The First Armstrong Number is: ",sum)
        break