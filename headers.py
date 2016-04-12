from urllib.request import Request, urlopen
import re


def main():

    
    
    url = 'http://www.twitter.com'
    getHeader(url)

   
    url = 'http://www.google.com'
    getHeader(url)
    
    url = 'http://www.facebook.com'
    getHeader(url)

    url = 'http://www.yahoo.com'
    getHeader(url)



def getHeader(url):

    a = urlopen(url).info()
    str(a)

    for x in a: 
        if re.match("(S|s)et-(C|c)ookie.*$", x):
            print(x)

    return a



if __name__ == '__main__':
    main()
