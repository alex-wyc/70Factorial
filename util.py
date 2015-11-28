import google
import requests
import bs4
import re
from patterns import regex

def get_list_of_urls(to_google, num_results):
    """
    get_list_of_urls: returns a list of urls 

    Args:
        to_google (string): a string 
        num_results (int): the number of results
    
    Returns:
        a list of urls that the google api returns
    
    Example:
        TODO
    
    Raises:
        None
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
    
    Example:
        TODO
    
    Raises:
        TODO
    """

    r = requests.get(url)
    raw = r.text
    text = regex.html_tag.sub("", raw) # nuke html tags
    text = regex.empty_space.sub(" ", text) # remove spaces
    return text

def who_frequency(haystack):
    """
    who: finds the NAME that appears the most within a given haystack

    Args:
        haystack (string): the haystack to search in
    
    Returns:
        A name that corrolates the most
    
    Example:
        TODO
    
    Raises:
        TODO
    """


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
        TODO
    
    Raises:
        TODO
    """
    name = regex.name
    a = re.findall(name, haystack)
    for i in a:
        if i in current_results:
            current_results[i] += 1
        else:
            current_results[i] = 1
    return current_results

if __name__ == '__main__':
    list1 = get_list_of_urls(raw_input("What would you like to know? "), 10);
    current_results = {}
    for i in list1:
        text = get_text_from_url(i)
        current_results = find_name(text, current_results)

    sorted_res = sorted(current_results.items(), key=lambda x: x[1], reverse=True)
    print sorted_res[0:10]
