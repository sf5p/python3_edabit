def greeting(name):
    GUEST_LIST = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    tag = GUEST_LIST.get(name)
    if tag:
        print(f"Hi, I'm {name}, and I'm from {tag}.")
    else:
        print("Hi!, I'm a guest.")
