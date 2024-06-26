import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
#BASE_URL = "https://ssfjuod8z4.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODO')
        #List
        url = BASE_URL+"/todos"
        response = requests.get(url)
        print('Response List Todo:' + str(response.json()))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertFalse(response.json())
        
        print('End - integration test List TODO')
   
    def test_api_gettodo(self):
         print('---------------------------------------')
         print('Starting - integration test Get TODO')
         jsonbody = {'id': 123}
         ID_TODO = str(jsonbody['id'])
         #Test GET TODO
         url = BASE_URL+"/todos/"+ID_TODO
         response = requests.get(url)
         print('Response Get Todo '+ url+': '+ str(response))
         self.assertEqual(
         response.status_code, 404, "Error en la petición API a {url}"
         )

    