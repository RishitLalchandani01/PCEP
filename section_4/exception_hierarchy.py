#### PYTHON EXCEPTIONS HIERARCHY ####
# https://profound.academy/python-mid/exception-hierarchy-phonbKOpXJ362GhumAsG
# https://github.com/lavnishl/python_basics/tree/main/Python_Code_PCEP/module5/pcep-30-02

# Ques : in order to do SystemExit .. what module should you import ?
# Ques : KyeyboardInterrupt is a subclass of which exception ?
# Ques : What is base class for mathmatical errors ?
# Ques : what is root of all exceptions ?
# Ques : if you want to make your own exception , which class should you inherit from ?

# Ques : what is difference between type error and value error
# >> TypeError << refers to a situation where something like a function is expecting to get one type as an argument, but it's given something else instead. For instance, it could be expecting a list, but given an integer.
age = input('What is your age? ')  # input always returns a string
print('You entered this', age)  # not type error , context is right
print(
    'In 10 years, you will be', age + 10
)  # you cannot add a string and a number , hence type IN-CONTEXT is wrong hence TypeError

# >> ValueError << refers to a situation where the type of the aforementioned argument is okay, but the actual content doesn't match some agreed-upon rule.
# python always tries to throw the most specific exception like for example zero division error is type of arithmetic error which is type of exception
# VALUE ERROR. : Example
age = int(input('What is your age? '))
# What is your age? a # ValueError: invalid literal for int() with base 10: 'a'

# NOTE : whenever pythoon throws an exception. it tries to throw the most specific exception

# TODO : Ques : What is difference between IndexError and KeyError ?
