'''
Created on Oct 20, 2020

@author: lgu
'''

import urllib.request, urllib.parse
import rdflib

import logging as log
log.basicConfig(level=log.DEBUG)

class FREDError(Exception):

    def __init__(self, message):
        self.message = message

class FREDDialer:

    def __init__(self, fred_endpoint, requestMimeType):
        self.__fred_endpoint = fred_endpoint + "?%s"
        self.__requestMimeType = requestMimeType
    
    def dial(self, text, namespace, wsd=None):
        params = {'text': text,
             'namespace': namespace,
             'wsd': wsd}
        
        if wsd is not None:
            params["wfd"] = True
            params["wfd_profile"] = wsd
            
        params = urllib.parse.urlencode(params)
                
        log.info(self.__fred_endpoint % params)
        graph = rdflib.Graph()
        request = urllib.request.Request(self.__fred_endpoint % params, headers={"Accept": self.__requestMimeType})
        try:
            response = urllib.request.urlopen(request)
            output = response.read()
            
            graph.parse(data=output, format=self.__requestMimeType)
        except:
            raise FREDError("The graph produced is empty due to an exception occurred with FRED.")
        
        return graph