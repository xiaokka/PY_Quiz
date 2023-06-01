#正则匹配中文
import re

string = "中文！English"
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(string)

print(result)
