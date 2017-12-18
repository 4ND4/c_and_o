import time
import urllib2
import lxml


def ping():
    global lst1
    status = True
    while(status):
        if network_connection() is True:
            links = lxml.html.parse("http://google.com").xpath("//a/@href")
            status = False
            for url in links:
                lst1.append(url)
        else:
            time.sleep(0.1) #use 100 milliseconds sleep to throttke down CPU usage


def network_connection():
    network = False
    try:
        response = urllib2.urlopen("http://google.com", None, 2.5)
        network = True

    except urllib2.URLError, e:
        pass
    return network


ping()

