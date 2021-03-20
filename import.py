import os
import  time
import requests
from  win10toast import ToastNotifier
from time import strftime

class Instagram_updater(object):
    def __init__(self, username):
        self.username = username
        self.current = "None"
        self.last = "None"
        self.first = "None"

    def followers(self):
        url = 'https://www.instagram.com/' +self.username
        r = requests.get(url).text
        start = '"edgo_followedby":{"count":'
        end = '},"followed_by_viewer"'
        self.last = self.current
        self.current = str(r[r.find(start)+len(start):r.rfind(end)])

    def main(self, notification_note):
        parser = ToastNotifier()
        start_time = strftime("%H:%M:%S",time.localtime())
        self.followers()
        self.first = self.current

        while True:
            try:
                data = str(f"Current Amount:\t{int(self.current):,}\n"
                           f"Last Amount:\t{int(self.last):,}\n"
                           f"Time Started:\t{int(start_time):,}\n"
                           f"Started with:\t{int(self.current):,}")
                           













