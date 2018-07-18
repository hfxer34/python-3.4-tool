# -*- coding: utf-8 -*-

import doctest
import requests

def sample(query):
    """ requests sample that use qiita search api
    >>> 'title' in sample('python')
    True
    >>> 'totle' in sample('python')
    False
    """
    q = {'q':  query}
    r = requests.get('https://qiita.com/api/v1/search', params=q)
    return list(r.json()[0].keys())

if __name__ == "__main__":
    doctest.testmod()