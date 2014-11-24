__author__ = 'tmehta'
from twython import TwythonStreamer


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code
        # self.disconnect()


stream = MyStreamer('UR7PSstYAPjRpHGJV3DfTKHjX', 'cIJjcRHjrga5umsPp6iGWi0RFhgDUIybieg8XyvmEj0CkAn1PZ',
                    '1363462640-l9AXw6jpKv3d3MzddqHVY3BV16l3dz2596mg0dZ',
                    'qRqns6173zX9jNDJOwqTDCe6BNSSr2ybB4pzrdr3Tbpzh')
stream.statuses.filter(track='wethenorth')