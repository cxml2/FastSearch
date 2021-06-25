import re as reg
import time
import urllib.request as url
import winsound
from pyyoutube import Api
import wikihowunofficialapi as wha
import wikipedia
import wikipedia.exceptions as we
import requests

wordstolookfor = ["why", "how", "who", "?", "what"]
pagetit = ""
print('"gs:" to only search Google \n'
      '"bn:" to only search Bing\n'
      '"pip:" to search pypi.org\n'
      '"yt:" to search videos on YouTube (Work In Progress)\n'
      '"rickroll" to generate a rickroll link so that you can troll your friends ;)\n'
      '"random" to find a random Wikipedia article')
searchforwhat = input("searching for?: ")

getaritcles = wha.search_wikihow(searchforwhat)
firstarticle = getaritcles[0]
firstarticlestr = str(firstarticle)
# print(firstarticlestr)

i = 0
q = 0
title = ""
content = ""
search_results = ""
f = 0
string = ""
string2 = ""
slow = searchforwhat.lower()
slist = slow.split()

if slist[0] == "random":
    searchforwhat = f"How to {wha.random_article()}"

splitstringlist = firstarticlestr.split()
l = 1
while i < (len(splitstringlist)):
    string += f"{splitstringlist[i]}-"
    i = i + 1
string8 = ""
while l < (len(slist)):
    string8 += f"{slist[l]}-"
    l = l + 1
j = 1
h = 1
y = 1
string4 = ""
stringy = ""
stringslicedy = ""
if slist[0] == "who" or slist[0] == "gs:":
    while j < (len(slist)):
        string2 += f"{slist[j]}%20"
        j = j + 1
if slist[0] == "bg:":
    while h < (len(slist)):
        string4 += f"{slist[h]}+"
        h = h + 1

if slist[0] == "yt:":
    while y < (len(slist)):
        stringy += f"{slist[y]}%20"
        y = y + 1
if slist[0] == "who" or slist[0] == "gs:":
    stringsliced2 = string2[0:len(string2) - 3]

if slist[0] == "how":
    stringsliced = string[0:len(string) - 1]
if slist[0] == "pip:":
    stringsliced5 = string8[0:len(string8) - 1]
if slist[0] == "bg:":
    stringsliced4 = string4[0:len(string4) - 1]
if slist[0] == "yt:":
    stringslicedy = stringy[0:len(stringy) - 3]
if slist[0] == "how":
    t0 = time.time()

    articleurl = wha.Article(f'https://www.wikihow.com/{stringsliced}')

    print(articleurl.summary)

    t1 = time.time()
    total = t1 - t0
    print(f"Took approximately {total.__round__()} seconds to load results from WikiHow")
    print(f"For more information on {firstarticlestr.title()}, visit {articleurl.url} ")
    print("Keep in Mind :")
    while f < len(articleurl.tips):
        print(f"> {articleurl.tips[f]}")
        f = f + 1
    winsound.MessageBeep()
elif slist[0] == "rickroll":

    print(f"dis.gd/threads")
    winsound.MessageBeep()
elif slist[0] == "who" or slist[0] == "gs:":
    print(f"visit: https://www.google.com/search?q={stringsliced2}")
elif slist[0] == "yt:":
    request = requests.get(
        f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={stringslicedy}&type=video&key=[Your API Key]")
    response = request.json()
    print(response)
    #print(response.items.stringify())
    html = url.urlopen(f"https://www.youtube.com/results?search_query={stringslicedy}")
    print(f"https://www.youtube.com/results?search_query={stringslicedy}")
    Vid_ID = reg.findall(r"watch\?v=(\S{11})", html.read().decode())
    #Vid_Title = reg.findall(r"'title': '()'", response)
    #print (Vid_Title)
    print("List of Videos found on Youtube:")
    while q < len(Vid_ID):
        vidurl = Vid_ID[q]
        video_by_id = api.get_video_by_id(video_id=vidurl)

         #video_by_id
        #VideoListResponse(kind='youtube#videoListResponse')

         #video_by_id.items
        #[Video(kind='youtube#video', id='CvTApw9X8aA')]
        url = f"{q+1} https://www.youtube.com/watch?v={vidurl}"
        # urltest="https://www.youtube.com/watch?v=Xm7gtOi2pnc"
        # v= Video(urltest)
        print(url)
        q = q + 1
    print (f"Found {q} URLs")

elif slist[0] == "pip:":
    print(f"visit: https://pypi.org/search/?q={stringsliced5}/")
elif slist[0] == "bg:":
    print(f"visit: https://www.bing.com/search?q={stringsliced4}")

else:

    try:
        pagetit = wikipedia.page(slow.strip()).title
        if pagetit in slow:
            t0 = time.time()
            print(wikipedia.summary(searchforwhat.lower()))

            t1 = time.time()
            total = t1 - t0
            print(f"Took approximately {total.__round__()}({total}) seconds to load results from Wikipedia")
            print(f"For more information on {searchforwhat.title()}, visit {wikipedia.page(searchforwhat).url} ")
            winsound.MessageBeep()
        else:
            if slist[0] != "random":

                print(f"searched for {searchforwhat.lower()} but found {pagetit.lower()}")
                t0 = time.time()
                print(wikipedia.summary(searchforwhat.lower()))

                t1 = time.time()
                total = t1 - t0
                print(f"Took approximately {total.__round__()}({total}) seconds to load results from Wikipedia")
                print(f"For more information on {pagetit.title()}, visit {wikipedia.page(searchforwhat).url} ")
                winsound.MessageBeep()
            else:

                t0 = time.time()
                print(wikipedia.summary(searchforwhat.lower()))
                t1 = time.time()
                total = t1 - t0
                print(f"Took approximately {total.__round__()}({total}) seconds to load results from Wikipedia")

                winsound.MessageBeep()

    except we.PageError as e:

        print("""\033[1;33;40m Uh Oh an error has occurred!:(
        Try rephrasing the question, or try again! \033[0;37;40m""")
        # print(f"searched for {searchforwhat.lower()} but found {pagetit.lower()}")
    except we.DisambiguationError as e:
        print(
            "\033[1;33;40m Uh Oh, Looks like what you searched was too strong! Even for Wikipedia! Try rephrasing the question")
    except NameError as e:
        print("\033[1;33;40m Wait, did you just find a glitch in the Matrix?")
# if close.lower()=="true":
print("Press ENTER to close ...")
input()
