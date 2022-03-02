''' 
A minimalistic {Bit,Lite,...}coin RPC client using only few modules
from the Python standard library.

PRESET_PORTS : dict of strings
PRESET_COOCKIES : string
'''

import os
import sys
import json
import http.client
from base64 import b64encode


PRESET_PORTS = {
        'bitcoin': '18332',
        'litecoin': '9332',
        }


# {}coind datadir varies by OS
if os.name == 'nt':
    PRESET_COOKIE = os.path.join(os.getenv('APPDATA'), '{}./cookie')
elif os.name == 'posix':
    if sys.platform == 'darwin':
        PRESET_COOKIE = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', '{}/.cookie')
    else:
        PRESET_COOKIE = os.path.join(os.path.expanduser('~'), '.{}/.cookie')
else:
    raise NotImplementedError



def call(url, command, user_colon_pass=None):
    '''Send a command to the {}coind RPC server and retrieve its response.

    Parameters
    ----------
    command : string
        A valid {}coind RPC command. Try "help" if unsure.
        Arguments have to be space separated, try "help {command_name}" for
        more information.
    user_colon_pass: string
        Username:password (separated by a semicolon). Alternatively, a loaded
        cookie file (__cookie__:blablabla...). This parameter is identical to
        the strRPCUserColonPass variable in bitcoin_cli.cpp

    Returns
    -------
    result : string
        The response of the RPC server
    
    Raises
    ------
    hhtp.client.HTTP
        If the server's response status code is other than 200 (success).
    '''
    
    command = command.split(' ')[0]
    arguments = command.split(' ')[1:]

    message = {"method": command , "id": 1}
    if arguments:
        message['params'] = arguments
    message = json.dumps(message)

    headers = {}
    headers['Authorization'] = b'Basic '+ b64encode( user_colon_pass.encode() )
    headers['Connection'] = 'close'
    headers['Content-Length'] = len(message)

    c = http.client.HTTPConnection(url)
    c.request('POST', '', message, headers)
    
    response = c.getresponse()

    if response.status != 200:
        message = json.loads(response.read().decode('ISO-8859-1'))['error']['message']
        raise http.client.HTTPException(
                ('RPC server responded with HTTP status code {}. Message: {}'
                    ).format(response.status, message))
    
    return json.loads(response.read().decode('ISO-8859-1'))['result']



def load_cookie(cookie_fn):
    '''Load an active coind cookie file.

    Parameters
    ----------
    cookie_fn : string
        Filename of the cookie file.
    '''
    with open(cookie_fn, 'r') as fp:
        return fp.readline()



class TinyCoinTalk:
    '''Object oriented interface to TinyCoinTalk.
    
    Attributes
    ----------
    self.url : string
    self.user_colon_pass : string
    '''
    def __init__(self, url, user_colon_pass=None, cookie_fn=None):
        '''
        Parameters
        ----------
        url : string
            hostname:port or a special value to get a port from PRESET_PORTS.
        user_colon_pass : string or None
            Username separated by a colon. For example "tux:password".
        cookie_fn : string or None
            If specified, attempts to load the user_color_pass from this file.
        '''
        if url in PRESET_PORTS:
            self.url = 'localhost:'+PRESET_PORTS[url]
            if not user_colon_pass and not cookie_fn:
                cookie_fn = PRESET_COOKIE.format(url)
        else:
            self.url = url

        if user_colon_pass and cookie_fn:
            raise ValueError('Use ONLY user_colon_pass OR cookie_fn, not both')
        elif not user_colon_pass and not cookie_fn:
            raise ValueError(
                    ('The given URL "{}" does not belong to the known preset '
                        'values of {}.'
                        'You have to give user_colon_pass or cookie_fn for the '
                        'constructor.').format(url, list(PRESET_PORTS.keys()))
                    )
        
        if user_colon_pass:
            self.user_colon_pass = user_colon_pass
        elif cookie_fn:
            self.user_colon_pass = load_cookie(cookie_fn)


    def call(self, command):
        return call(self.url, command, self.user_colon_pass)

