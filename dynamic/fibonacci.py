def fibonacci(p) :
  if (p == 1):
    return 0
  elif (p == 2):
    return 1
  return fibonacci(p - 1) + fibonacci(p -2)

print(fibonacci(5))