import pandas as pd
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# fizzbuzz.py  
for i in range(1, 16):
    print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)

df = pd.DataFrame(columns=['Fizz', 'Buzz'])
for i in range(1, 16):
    df.loc[i] = ['Fizz'*(i%3==0), 'Buzz'*(i%5==0)]
    print(df.loc[i])
    