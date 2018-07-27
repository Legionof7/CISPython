##########################
# CIS 117 Python Programming:  Lab #5   
#
# The Web and Search
#
##########################
from urllib.request import urlopen

def TopicCount():
    TopicList = ["research", "climate", "evolution", \
    "cultural", "leadership", "science"] 
    SiteOpen = urlopen('http://www.nasonline.org/')
    SiteContent = SiteOpen.read()
    html = SiteContent.decode().lower()
    for topic in TopicList:
        count = html.count(topic)
        print('{} appears {} times.' \
        .format(topic,count))

TopicCount()

##########################
#Run
#
#research appears 9 times.
#climate appears 4 times.
#evolution appears 6 times.
#cultural appears 11 times. 
#leadership appears 4 times. 
#science appears 54 times.
##########################  