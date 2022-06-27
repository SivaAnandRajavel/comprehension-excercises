# 1st if check if the number beetwen range of 100 is divisible by both 3 and 5 then print fizzbuzz, if no. is divisible by 3 print fizz else if it is divible by 5 print buzz
output = [("fizzbuzz" if(i % 3 == 0 and i % 5 == 0) else "buzz" if i % 5 == 0 else "fizz" if i % 3 == 0  else i) for i in
         range(1, 101)]
print(output)

