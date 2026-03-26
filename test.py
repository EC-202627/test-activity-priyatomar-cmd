#X ml of water today. Determine if the client followed the doctor's advice or not.
#Input Format

#The first line contains a single integer 
#T — the number of test cases. Then the test cases follow.
#The first and only line of each test case contains one integer 
#X — the amount of water client drank today.
T=int(input())
for i in range(T):
    x=int(input())
    if x>=2000:
        print("Yes")
    else:
        print("No")
