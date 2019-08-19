my_var = list()

class A:
    pass


B = type("MyNewClass" , (), {"var_in_class": "yes" })

print(A)
print(B.var_in_class)

print(B.__dict__)

b = B()
print(b.__dict__)