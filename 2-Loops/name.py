import re

s = "helloWorld"
result = re.split(r"(?=[A-Z])", s)
print(result)
