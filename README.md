pythonbitly
===========

Gets a short URL from bit.ly using Python and outputs it to the command line and clipboard.


----------

Usage: pythonbitly < longURL >

----------
**Please note:** At the moment pythonbitly is dependend on [requests][1], [pyperclip][2] and [docopt][5]. If you have [pip][3] installed on your system you can simply install these dependencies using

`sudo pip install requests`

`sudo pip install pyperclip`

`sudo pip install docopt`

If you know how to achieve the same funcionality without those dependencies feel free to commit!


----------
**Also note:** To actually use pythonbitly you'll have to get your bit.ly API Token which you can get [here][4]. You'll then have to insert it in place of `YOUR_TOKEN_HERE` in the code.


  [1]: https://github.com/kennethreitz/requests
  [2]: http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/
  [3]: https://github.com/pypa/pip
  [4]: http://dev.bitly.com/
  [5]: https://github.com/docopt/docopt