#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get_bitly.py
#  
#  Copyright 2014 tom <tom@ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.
#  
#  

import requests, json, pyperclip


class bcolors:
    #This class defines the different colors that may be used in the code
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
        self.BOLD = ''

def get_short(longURL):
    #The main function of this script
    #It takes a long URL, requests the short URL from bit.ly, returns it and copies it into the clipboard.
    query_params = {
    'access_token': 'YOUR_TOKEN_HERE',
    'longUrl': longURL
    }
    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params=query_params, verify=False)
    data = json.loads(response.content)
    shortURL = data['data']['url']
    pyperclip.copy(shortURL)
    return shortURL

longURL = raw_input("Dein langer Link: ")

print "Dein gekürzter Link: ", bcolors.HEADER, bcolors.BOLD, get_short(longURL), bcolors.ENDC
print "Er befindet sich auch in der Zwischenablage."