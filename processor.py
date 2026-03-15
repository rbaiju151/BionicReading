import re
import math

def bionic_bold(matchobj):
    text = matchobj.group(0)
    bold_length = math.ceil(len(text) / 2)
    return f'<b>{text[:bold_length]}</b>{text[bold_length:]}'