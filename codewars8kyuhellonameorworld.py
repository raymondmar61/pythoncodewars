#https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/python
'''
Hello, Name or World! 8kyu

Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given or `name` = "" => return "Hello, World!"
'''
def hello(name=""):
    return f"Hello, {name.title()}!" if name or len(name) > 1 else "Hello, World!"


print(hello("John")) #print Hello, John!
print(hello("aLIce")) #print Hello, Alice!
print(hello("")) #print Hello, World!

name = ""
if name:
    print(f"Hello, {name.title()}!")
else:
    print("Hello, World!") #print Hello, World!
