print("Armstrong Numbers between 1 to 1000 are:")
numbers=1000

for no in range(1,1001):
       org=no
       temp=0
       while no > 0 :
             rem=no % 10
             temp += rem ** 3
             no //= 10        
            
       if org==temp :
              print(org)            

'''
nilesh@ishan:~/Desktop/Python/Basics$ python3 arm1_to_n.py
Armstrong Numbers between 1 to 1000 are:
1
153
370
371
407

'''
