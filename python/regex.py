# Find ===========

# import re

# text = "The quick brown fox with brown legs"
# pattern = r"brown"

# # search = re.search(pattern, text) # finds in middle of the string as well
# # search = re.match(pattern, text) # only finds at start of string
# search = re.findall(pattern, text)
# if search:
#     # print("Pattern found:", search.group())
#     print("Pattern found:", search) # with findall
# else:
#     print("Pattern not found")

# Replace ============

# import re

# text = "The quick brown fox jumps over the lazy brown dog"
# pattern = r"brown"

# replacement = "red"

# new_text = re.sub(pattern, replacement, text)
# print("Modified text:", new_text)

# Split =========
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)