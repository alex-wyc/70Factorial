import google
import requests
import bs4
import re
from patterns import regex

MONTH_TABLE = {
    'jan' : 1,
    'january' : 1,
    'feb' : 2,
    'febuary' : 2,
    'mar' : 3,
    'march' : 3,
    'apr' : 4,
    'april' : 4,
    'may' : 5,
    'jun' : 6,
    'june' : 6,
    'jul' : 7,
    'july' : 7,
    'aug' : 8,
    'august' : 8,
    'sep' : 9,
    'sept' : 9,
    'september' : 9,
    'oct' : 10,
    'october' : 10,
    'nov' : 11,
    'november' : 11,
    'dec' : 12,
    'december' : 12
}

def get_list_of_urls(to_google, num_results):
    """
    get_list_of_urls: returns a list of urls 

    Args:
        to_google (string): a string 
        num_results (int): the number of results
    
    Returns:
        a list of urls that the google api returns
    """

    to_return = []
    search_results = google.search(to_google, num = num_results, start = 0, stop = num_results);
    for i in search_results:
        to_return.append(i)

    return to_return

def get_text_from_url(url):
    """
    get_text_from_url: returns the text of a website from a given url

    Args:
        url (string): the url to explore
    
    Returns:
        a large unicode string that is the website.
    """

    r = requests.get(url)
    raw = r.text
    text = regex.html_tag.sub("", raw) # nuke html tags
    text = regex.empty_space.sub(" ", text) # remove spaces
    return text

def find_name(haystack, current_results = {}):
    """
    find_name: find everything that looks like a name in the haystack

    Args:
        haystack (string): the haystack to search in
        current_results (dictionary, optional): if we have already had
            some answers, default value is the empty dictionary
    
    Returns:
        a dictionary whose keys are the possible names and whose values
        are the number of occurances of the name
    
    Example:
        find_name("Superman is Clark Kent!") --> {"Clark Kent" : 1}
    """
    name = regex.name
    a = re.findall(name, haystack)
    for i in a:
        if i in current_results:
            current_results[i] += 1
        else:
            current_results[i] = 1
    return current_results

def find_date(haystack, result={}):
    """
    find_date: finds everything in haystack that looks like a date-time
        and updates the frequency in result

    Args:
        haystack (string): the haystack to look for time
	result (dictionary): the frequency table that will be updated, default
        	value is an empty dictionary
    
    Returns:
        a dictionary that is an updated version of result
    
    Example:
        find_date("This even happened on October 11, 2015") --> {'2015-10-11' : 1}
    """
    res1 = re.findall(regex.time1, haystack)
    for (year, month, day) in res1:
        if year != '':
            date = "%s-%s-%s" % (year, month, day)
            if date in current_results:
                current_results[date] += 1
            else:
                current_results[date] = 1

        date = "%s-%s" % (month, day)
        if date in current_results:
            current_results[date] += 1
        else:
            current_results[date] = 1

    res2 = re.findall(regex.time2, haystack)
    for (month, day, year) in res2:
        month = MONTH_TABLE[month.lower()]

        if year == '':
            date = "%d-%s" % (month, day)
        else:
            date = "%s-%d-%s" % (year, month, day)

        if date in current_results:
            current_results[date] += 1
        else:
            current_results[date] = 1

    return current_results

def sort_dict_by_value(dict, num_results):
    """
    sort_dict_by_value: return a list of the top num_results keys sorted
        by the value of the dictionary

    Args:
        dict (dictionary): the dictionary that needs to be sorted
	num_results (int): the number of desired results
    
    Returns:
        a list of length num_results of the keys of the dictionary sorted by
        value
    
    Example:
        sort_dict_by_value({'a': 10, 'b':1, 'c': 3, 'd':5}, 2) --> ['a', 'd']
    """

    sorted_res = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_res[0:num_results]

if __name__ == '__main__':
    input = raw_input("What would you like to know? ")

    if input.split()[0].lower() == 'who':
        mode = 'who'
    else:
        mode = 'when'

    list1 = get_list_of_urls(input, 10);
    current_results = {}
    for i in list1:
        text = get_text_from_url(i)
        if mode == 'who':
            current_results = find_name(text, current_results)
        else:
            current_results = find_date(text, current_results)

    print sort_dict_by_value(current_results, 10)
