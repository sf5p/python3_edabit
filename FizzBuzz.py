def fizzbuzz(num):
  if not num % 5 and not num % 3:
    print("FizzBuzz")
  elif not num % 5:
    print("Buzz")
  elif not num % 3:
    print("Fizz")
  else:
    print(str(num))


while True:
  try:
    user_input = int(input("Some input please: "))
    fizzbuzz(user_input)
  except EOFError:
    print()
    break
