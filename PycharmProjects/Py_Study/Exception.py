
#FileNotFoundError
#NameError
#BaseException
#raise
name = "Jack"
try:
    print(name)
except NameError as msg:
    print(msg)
else:
    print("the end")
finally:
    print("name is defind")
