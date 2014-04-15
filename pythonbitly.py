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

"""
Usage: pythonbitly <longURL>
"""

import requests, json, pyperclip
from docopt import docopt


if __name__ == "__main__":
    # Docopt will check all arguments, and exit with the Usage string if they
    # don't pass.
    # If you simply want to pass your own modules documentation then use __doc__,
    # otherwise, you would pass another docopt-friendly usage string here.
    # You could also pass your own arguments instead of sys.argv with: docopt(__doc__, argv=[your, args])
    args = docopt(__doc__)

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
    'access_token': '70fe81c157645c2e608431797a5f6ec448de2750',
    'longUrl': args["<longURL>"]
    }
    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params=query_params, verify=False)
    data = json.loads(response.content)
    shortURL = data['data']['url']
    pyperclip.copy(shortURL)
    return shortURL

#In the following line get_short(args) will be called
print "Your shortened Link:", bcolors.HEADER, bcolors.BOLD, get_short(args), bcolors.ENDC
print "It has also been copied to the clipboard."