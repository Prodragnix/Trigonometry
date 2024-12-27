import math
print('\nTHIS IS A TRIGONOMETRY CALCULATOR!\n')
ans=input('Please enter what you want to work out:\n sin\n cos\n tan\n all\nEnter you choice: ')
angle=int(input('Please enter the angle:'))
if ans=='sin':
    print('The sin of',angle,'is: ',math.sin(angle))

elif ans=='cos':
    print('The cos of',angle,'is: ',math.cos(angle))

elif ans=='tan':
    print('The tan of',angle,'is: ',math.tan(angle))

else:
    print('The sin of',angle,'is: ',math.sin(angle))
    print('The tan of',angle,'is: ',math.tan(angle))
    print('The cos of',angle,'is: ',math.cos(angle))