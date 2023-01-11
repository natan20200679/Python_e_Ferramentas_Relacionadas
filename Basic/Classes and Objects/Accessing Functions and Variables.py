class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"
myobjectx.function()

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)