def d():
    animal = "elephant"
    def e():
        #It changes the animal to "giraffe" fot the whole thing
        nonlocal animal
        animal = "giraffe"
        print ("Inside the nested functions of: " + animal)
    print ("Before calling the nested functions: " + animal)
    e()
    print ("After calling the nested functions: " + animal)

animal = "camel"
d()
print("Global animal: " + animal)