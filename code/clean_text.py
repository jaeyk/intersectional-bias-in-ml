#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:34:09 2020

@author: jae
"""

# HTML tags and punctuation 
url_re = r'http\S+'
at_re = r'@[\w]*'
rt_re = r'^[rt]{2}'
punct_re = r'[^\w\s]'

def clean_tweet(document):
    document = document.str.lower() # Lower Case
    document = document.str.replace(url_re, '') # Remove Links/URL
    document = document.str.replace(at_re, '') # Remove @
    document = document.str.replace(rt_re, '') # Remove rt
    document = document.str.replace(punct_re, '') # Remove Punctation
    return(document)
