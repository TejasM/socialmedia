import requests

__author__ = 'tmehta'

ip_address = ''
port = '5000'
connection = 'https://' + ip_address + ':' + port + '/'


def post_to_server(data):
    return requests.post(connection + 'event/', data)