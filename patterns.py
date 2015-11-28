import re

"""
This file contains all the patterns used in regex
"""

class regex:
    html_tag = re.compile(r'<.*?>')
    empty_space = re.compile(r'[ \t\n]+')
    name = re.compile(r'\b[A-Z][a-z]*? [A-Z][a-z]*?\b')
