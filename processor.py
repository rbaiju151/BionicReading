import re
import math

def bionic_bold(matchobj):
    text = matchobj.group(0)
    bold_length = math.ceil(len(text) / 2)
    return f'<b>{text[:bold_length]}</b>{text[bold_length:]}'

# debugging lines
# text = "Vendémiaire"
# print(re.sub('[a-zA-ZÀ-ÿ]+', bionic_bold, text))