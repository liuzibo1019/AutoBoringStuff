import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d")
mo = phoneNumRegex.search("my number = 123-456")
print(mo.group())
