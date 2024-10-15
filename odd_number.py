'''
Author:Divya Kuriakose
Date:15-10-2024
program for generating n odd numbers
'''

limit=int(input("Enter the limit:"))
odd_number=1
count=0
while count<limit:
    print("\n",odd_number,"\n",end=" ")
    count+=1
    odd_number+=2