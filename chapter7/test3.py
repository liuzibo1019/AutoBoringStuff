import re

regex = re.compile(r"name: (.*)")
reg = regex.search("name: 456")
print(reg.group())
