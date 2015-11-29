import re

"""
This file contains all the patterns used in regex
"""

class regex:
    html_tag = re.compile(r'<.*?>')
    empty_space = re.compile(r'[ \t\n]+')
    name = re.compile(r'\b[A-Z][a-z]*? [A-Z][a-z]*?\b')
    time1 = re.compile(r'([0-9]{4}){0,1}[/-]{0,1}([1-9]|0[1-9]|1[0-2])[/-]([0-2][0-9]|3[01]|[0-9])');
    time2 = re.compile('(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec'
                        '|january|febuary|march|april|june|july|august|september|'
                        'october|november|december)'
                        '[. ]+?([0-2][0-9]|3[01]|[0-9]).*? '
                        '([0-9]{4})?', re.IGNORECASE)

if __name__ == '__main__':
    #input = raw_input("Enter a Time: ")
    #res = re.findall(regex.time1, input)
    #print res
    #res = re.findall(regex.time2, input)
    #print res

    input = raw_input("Enter a sentence with a name: ")
    res = re.findall(regex.name, input)
    print res
