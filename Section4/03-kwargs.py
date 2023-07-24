def  get_product(**data):
    print(data)
    print(data["id"],data["name"]) #We can print one by one the arguments

get_product(id = "23",
            name =" iPhone",
            desc = "This is an iPhone")