
# Strings are immutable
a = "Dipika!!!!! pawar"
print(len(a))

# UpperCase
print(a.upper())
print(a.lower())

# rstrinp to remove symbol(!)
print(a.rstrip("!"))

# Replace method
print(a.replace("Dipika", "vedika"))

#Split method
print(a.split(" ")) #split into list

name = "dipika"
print(name.capitalize()) 

#Centre method
string = "Hello welcome to my code!!"
print(string.center(30))  #align to centre
print(len(string))
print(len(string.center(50)))

#Count method
b = "hello dipika! dipika is an engg student"
print(b.count("dipika"))

#EndsWith() method
b = "hello dipika! dipika is an engg student"
print(b.endswith("student"))  #True/ False
print(b.endswith("dipika", 6, 12))

#Find() Method
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) #-1 - if not found

#isPrintable() - all characters are printable
str1 = "He's name is Dan. He is an honest man."
print(str1.isprintable())
str1 = "He's name is Dan. He is an honest man.\n" 
print(str1.isprintable()) #-- False

#SpaceBar
str1 = "        "
print(str1.isspace())

#isTitle()
str1 = "He's name is Dan. He is an honest man."
print(str1.istitle()) #returns True only if first letter of each word is capitable

#StartsWith()
str1 = "He's name is Dan. He is an honest man."
print(str1.startswith("dipika"))

#Title()method - capitalize each letter of the word
str1 = "He's name is Dan. He is an honest man."
print(str1.title())


 

