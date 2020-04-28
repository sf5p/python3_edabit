GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}

def ig(name):
  if name in GUEST_LIST:
    return "Hi! I'm {}, and I'm from {}".format(name, GUEST_LIST[name])
  return "Hi! I'm a guest."

while True:
  try:
    user_input = input("A name: ")
    print(ig(user_input))
  except EOFError:
    print()
    break
  

