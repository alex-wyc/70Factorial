import google
import requests
import bs4
import re

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
    soup = bs4.BeautifulSoup(r.text)
    raw = soup.get_text(r.text)
    text = re.sub("[\t\n ]+",' ',raw)
    text2 = re.sub("\<[^\>]\>", " ", text);
    return text2

if __name__ == '__main__':
    list_of_urls = get_list_of_urls(raw_input("What would you like to know? "), 10)
    for i in list_of_urls:
        print i
    print
    print get_text_from_url(list_of_urls[4])

