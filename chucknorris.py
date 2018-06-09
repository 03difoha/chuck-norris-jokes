"""
@author 03difoha

@date 2018

Generates Chuck Norris jokes
"""

import json
import urllib2
from time import sleep

baseUrl = 'http://api.icndb.com/'

def greeting():
    initiateJoke = raw_input('Psst...Would you like to hear a joke?\n')
    if str(initiateJoke) == 'yes' or str(initiateJoke) == 'ok':
        firstName = raw_input('Awesome!, Whats your first name?\n')
        lastName = raw_input('Got it, and your last name?\n')
        chooseCategory(firstName, lastName)
    else:
        print('No worries bro...')


def getCategories():
    categories = json.load(urllib2.urlopen(baseUrl + 'categories'))
    for i in categories['value']:
        print('- ' + i + '\n')


def chooseCategory(firstName, lastName):
    print('Sweet, What kind of joke do you want to hear {}\n'.format(firstName))
    getCategories()
    print('- Whatever, I dont care (Just press enter)')
    category = str(raw_input("(Choose one from the list)\n".format(firstName)))
    print('Ok, here goes...')
    getJoke(firstName, lastName, category)


def getJoke(firstName, lastName, category):
    if category:
        url = '{}jokes/random?firstName={}&lastName={}&limitTo=[{}]'.format(baseUrl, firstName, lastName, category)
    else:
        url = '{}jokes/random?firstName={}&lastName={}'.format(baseUrl, firstName, lastName)
    data = json.load(urllib2.urlopen(url))
    print(data['value']['joke'])
    sleep(4)
    another = raw_input('lulz, pretty funny, want to hear another?\n')
    if str(another) == 'yes' or str(another) == 'ok':
        chooseCategory(firstName, lastName)
    else:
        print('fair play. Bye then!')


if __name__=='__main__':
    greeting()
