# required args
def p1(name):
    print("hello", name)


p1("hey")


# keyword arg
def user_info(name, age):
    print("hello", name, "your age is: ", age)


user_info("python", 20)
user_info(20, "python")
user_info(name="rithik", age=24)
user_info(age=24, name="rithik")


# default arg
def user_info_default(name, age=30):
    print("hello", name, "your age is: ", age)


user_info_default("python", 20)
user_info_default("python")


# variable lenght args
def hello(*name):
    for i in name:
        print("hello", i)


hello("python", "java", "rudy")
