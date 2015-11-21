import google
import requests
import beautifulsoup
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
        TODO
    """
