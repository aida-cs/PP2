import time, math

number = int(input("Enter the number: "))
delay = int(input("Enter the delay in milliseconds: "))
time.sleep(delay / 1000)
print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")