import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.filmx'
plugin = xbmcaddon.Addon(id=addon_id)
net = Net()
addon = Addon('plugin.video.filmx', sys.argv)
selfAddon = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'filmx.db')
BASE_URL = 'http://oneclickwatch.ws'
BASE_URL2 = 'http://www.filmpertutti.co/search/%5BHD%5D'
BASE_URL1 = 'http://www.filmpertutti.co/category/film/'
BASE_URL3 = 'http://www.filmpertutti.co/category/film/animazione/'

BASE_URL4 ='http://www.filmpertutti.co/category/film/animazione/'
BASE_URL5 ='http://www.filmpertutti.co/category/film/avventura/'
BASE_URL6 ='http://www.filmpertutti.co/category/film/azione/'
BASE_URL7 ='http://www.filmpertutti.co/category/film/biografico/'
BASE_URL8 ='http://www.filmpertutti.co/category/film/comico/'
BASE_URL9 ='http://www.filmpertutti.co/category/film/commedia/'
BASE_URL10 ='http://www.filmpertutti.co/category/film/documentario/'
BASE_URL11 ='http://www.filmpertutti.co/category/film/drammatico/'
BASE_URL12 ='http://www.filmpertutti.co/category/film/fantascienza/'
BASE_URL13 ='http://www.filmpertutti.co/category/film/fantasy/'
BASE_URL14 ='http://www.filmpertutti.co/category/film/gangster/'
BASE_URL15 ='http://www.filmpertutti.co/category/film/guerra/'
BASE_URL16 ='http://www.filmpertutti.co/category/film/horror/'
BASE_URL17 ='http://www.filmpertutti.co/category/film/musicale/'
BASE_URL18 ='http://www.filmpertutti.co/category/film/poliziesco/'
BASE_URL19 ='http://www.filmpertutti.co/category/film/storico/'
BASE_URL20 ='http://www.filmpertutti.co/category/film/thriller/'
BASE_URL21 ='http://www.filmpertutti.co/category/film/western/'
BASE_URL23 = 'http://www.italia-film.co/category/ultime-uscite-dvd/'
BASE_URL24 = 'http://www.italia-film.co/category/telefilm/'
BASE_URL25 = 'http://www.filmpertutti.co/category/serie-tv/'
BASE_URL26 = 'http://www.italia-film.co/category/film-hd/'
BASE_URL27 = 'http://www.italia-film.co/category/film-avventura/'
BASE_URL28 = 'http://www.italia-film.co/category/film-commedia/'
BASE_URL29 = 'http://www.italia-film.co/category/film-comici/'
BASE_URL30 = 'http://www.italia-film.co/category/film-fantascienza-2/'
BASE_URL31 = 'http://www.italia-film.co/category/film-azione/'
BASE_URL32 = 'http://www.italia-film.co/category/film-drammatici/'
BASE_URL33 = 'http://www.italia-film.co/category/film-animazione/'
BASE_URL34 = 'http://www.italia-film.co/category/film-romantici/'
BASE_URL35 = 'http://www.italia-film.co/category/film-fantasy/'
BASE_URL36 = 'http://www.italia-film.co/category/film-horror/'
BASE_URL37 = 'http://www.italia-film.co/category/film-guerra/'
BASE_URL38 = 'http://www.italia-film.co/category/film-poliziesco/'
BASE_URL39 = 'http://www.italia-film.co/category/genere-thriller/'
BASE_URL40 = 'http://www.italia-film.co/category/film-western/'
BASE_URL41 = 'http://www.italia-film.co/category/now-on-cinema/'
BASE_URL42 = 'http://www.darkstream.tv/elenco-saghe-streaming/'
BASE_URL43 = 'http://www.darkstream.tv/elenco-saghe-streaming/'

BASE_URL44 = 'http://www.darkstream.tv/uscite-bluray-e-dvd-2015-streaming/'
BASE_URL45 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-0-9/'
BASE_URL46 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-a/'
BASE_URL47 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-b/'
BASE_URL48 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-c/'
BASE_URL49 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-d/'
BASE_URL50 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-e/'
BASE_URL51 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-f/'
BASE_URL52 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-g/'
BASE_URL53 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-h/'
BASE_URL54 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-i/'
BASE_URL55 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-l/'
BASE_URL56 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-m/'
BASE_URL57 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-n/'
BASE_URL58 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-o/'
BASE_URL59 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-p/'
BASE_URL60 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-q/'
BASE_URL61 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-r/'
BASE_URL62 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-s/'
BASE_URL63 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-t/'
BASE_URL64 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-u/'
BASE_URL65 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-v/'
BASE_URL66 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-w/'
BASE_URL67 = 'http://www.darkstream.tv/elenco-alfabetico-film-streaming/elenco-film-xyz/'
BASE_URL68 = 'http://www.darkstream.tv/elenco-serie-tv-streaming/'
BASE_URL69 = 'http://www.filmsenzalimiti.co/genere/dvd-rip'
#http://dl1.moviefarsi.org/#
BASE_URL70 = 'http://filmstream.re/film-del-cinema'
BASE_URL71 = 'http://filmstream.re/animazione'
BASE_URL72 = 'http://filmstream.re/azione'
BASE_URL73 = 'http://filmstream.re/comico'
BASE_URL74 = 'http://filmstream.re/commedia'
BASE_URL75 = 'http://filmstream.re/fantasy'
BASE_URL76 = 'http://filmstream.re/gangster'
BASE_URL77 = 'http://filmstream.re/horror'
BASE_URL78 = 'http://filmstream.re/poliziesco'
BASE_URL79 = 'hhttp://filmstream.re/storico'
BASE_URL80 = 'http://filmstream.re/western'
BASE_URL81 = 'http://filmstream.re/film-del-cinema'

BASE_URL82 = 'http://www.cb01.eu/category/hd-alta-definizione/page1/'
BASE_URL83 = 'http://www.cb01.eu/category/hd-alta-definizione/animazione-hd/page1/'
BASE_URL84 = 'http://www.cb01.eu/category/hd-alta-definizione/avventura-hd/page1/'
BASE_URL85 = 'http://www.cb01.eu/category/hd-alta-definizione/azione-hd/page1/'
BASE_URL86 = 'http://www.cb01.eu/category/hd-alta-definizione/comico-hd/page1/'
BASE_URL87 = 'http://www.cb01.eu/category/hd-alta-definizione/commedia-hd/page1/'
BASE_URL88 = 'http://www.cb01.eu/category/hd-alta-definizione/documentario-hd/page1/'
BASE_URL89 = 'http://www.cb01.eu/category/hd-alta-definizione/drammatico-hd/page1/'
BASE_URL90 = 'http://www.cb01.eu/category/hd-alta-definizione/fantascienza-hd/page1/'
BASE_URL91 = 'http://www.cb01.eu/category/hd-alta-definizione/fantasy-fantastico-hd/page1/'
BASE_URL92 = 'http://www.cb01.eu/category/hd-alta-definizione/gangster-hd/page1/'
BASE_URL93 = 'http://www.cb01.eu/category/hd-alta-definizione/guerra-hd/page1/'
BASE_URL94 = 'http://www.cb01.eu/category/hd-alta-definizione/horror-hd/page1/'
BASE_URL95 = 'http://www.cb01.eu/category/hd-alta-definizione/poliziesco-hd/page1/'
BASE_URL96 = 'http://www.cb01.eu/category/hd-alta-definizione/sentimentale-hd/page1/'
BASE_URL97 = 'http://www.cb01.eu/category/hd-alta-definizione/storico-hd/page1/'
BASE_URL98 = 'http://www.cb01.eu/category/hd-alta-definizione/thriller-hd/page1/'
BASE_URL99 = 'http://www.cb01.eu/category/hd-alta-definizione/western-hd/page1/'

#### PATHS ##########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)
text = addon.queries.get('text', None)
urlurl = addon.queries.get('urlurl', None)
img = addon.queries.get('img', None)




def GetTitles13(section, url, startPage= '1', numOfPages= '1'):
    html = net.http_GET(url).content
    match=re.compile('<a href="(.+?)"> <h1>(.+?)</h1></a>').findall(html)
    match_next=re.compile("<link rel='next' href='(.+?)'/>").findall(html)
    for movieUrl, name in match:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('speedvideo.net', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                        
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks13', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
    
    for nextpage in match_next:
                       cm  = []
                       addon.add_directory({'mode': 'GetTitles13', 'section': section, 'url': nextpage}, {'title':  'Next >>>'}, contextmenu_items= cm, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
  	

def GetLinks13a(section, url):
        html = net.http_GET(url).content
       
        content = html
        
        match=re.compile('<a href="(.+?)" class="btn-wrapper link"').findall(content)
        
        for url in match:
                host = GetDomain(url)
                host = host.replace('embed.','')
                addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  'PLAY >>>' }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
def GetLinks13(section, url):
        html = net.http_GET(url).content
       
        content = html
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(content)
        match1=re.compile('<a href="(.+?)" rel="bookmark" title=".+?">').findall(content)
        
        for url,name in match:
                host = GetDomain(url)
                host = host.replace('embed.','')
                if not 'Videowood' in name: addon.add_directory({'mode': 'GetLinks13a', 'url': url.encode('utf-8')}, {'title':  name }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
                else: addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  name }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



##################################### GetTitles ################################ GetTitles ############################################### GetTitles ######################################
#------------------------------------------------------------------------------- FILMSTREAM.re ------------------------------------------------------------------------------#
def GetTitles12(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match=re.compile('<a href="(.+?)">\s*<img class=".+?" src="(.+?)" alt="" />\s*<div class=".+?">\s*<div class=".+?">\s*(.+?)<br><br>').findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        name=re.sub('Streaming','', name)
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks12', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles12', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img='http:' + img , fanart=img)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
		

def GetLinks12(section, url):
        html = net.http_GET(url).content
        
        content = html
        match = re.compile('<a href="(.+?)"><img src=".+?"').findall(content)
        match1 = re.compile('<a target=".+?" href="(.+?)" rel=".+?">').findall(content)
		
        
        
        for url in match + match1:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------- FILM SENZA LIMITI ------------------------------------------------------------------------------#
def GetTitles11(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match=re.compile('<a href="(.+?)">\s*<img src="(.+?)" width=".+?" alt=".+?" title="(.+?)"').findall(html)
                match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        name=re.sub('Streaming','', name)
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks11', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles11', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img='http:' + img , fanart=img)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks11(section, url):
        html = net.http_GET(url).content
        
        content = html
        match = re.compile('<a href="(.+?)" rel="nofollow" target="_blank" class="external">').findall(content)
        match1 = re.compile('SRC="(.+?)"').findall(content)
        
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))




#------------------------------------------------------------------------------- DARKSTREAM TV -----------------------------------------------------------------------------------------#

def GetTitles10(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + ''
                        html = net.http_GET(pageUrl).content                      
                match=re.compile('<a href="(.+?)">(.+?)</a>').findall(html)
                
                for movieUrl, name in match:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('speedvideo.net', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                        
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks10', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles66', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')      
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
def GetTitles10a(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + ''
                        html = net.http_GET(pageUrl).content                      
                match=re.compile('<a href="(.+?)">(.+?)</a>').findall(html)
                
                for movieUrl, name in match:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('speedvideo.net', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                        
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks10a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles66', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')      
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
				
def GetLinks10(section, url):
        html = net.http_GET(url).content
       
        content = html
        match=re.compile('<a href="(.+?)" target="_blank">.+?</a>').findall(content)
        match1=re.compile('<a href="(.+?)" rel="bookmark" title=".+?">').findall(content)
        
        for url in match + match1:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks10a(section, url):
        html = net.http_GET(url).content
       
        content = html
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(content)
        match1=re.compile('<a href="(.+?)" rel="bookmark" title="(.?)">').findall(content)
        
        for url,name in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------- FILM PER TUTTI SERIES. ------------------------------------------------------------------------------#

def GetTitles66(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/?paged=' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/?paged=' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
                match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
                for movieUrl, name, img in match + match1:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('speedvideo.net', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                        
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetTitles66b', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles66', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')      
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetTitles66b(section, url, startPage= '1', numOfPages= '1'):
        html = net.http_GET(url).content
        
        content = html
        match = re.compile('<a href="(.+?)" target="_blank" rel="nofollow">').findall(content)
        match1 = re.compile('SRC="(.+?)"').findall(content)
        
        for url in match + match1 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------- ITALIA FILM SERIES. ------------------------------------------------------------------------------#

def GetTitles65(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
		# reset
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img src="(.+?)"').findall(html)[:12]
                match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)[:12]
                for movieUrl,name,img in match + match1:
                        cm  = []
                        name=re.sub('Streaming','', name)
                        name=re.sub('-','', name)
                        name=re.sub('[!@#$-]', '', name)
                        
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        
                        addon.add_directory({'mode': 'GetTitles65b', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip() }, contextmenu_items= cm, img='http:' + img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles65', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img='', fanart=FanartPath + 'fanart.png')
                xbmcplugin.endOfDirectory(int(sys.argv[1]))
                
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles65b(section, url, startPage, numOfPages):
        html = net.http_GET(url).content
        
        content = html
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(content)
        match1=re.compile('>(.+?)<a href="(.+?)" target="_blank">Openload</a>').findall(content)
        
        
        for url,name in match :
                
                name=re.sub('Videomega', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title': '[COLOR yellow]' + name.strip() +'[/COLOR]' + ' -  url:' + url.strip()}, img=IconPath + 'rls66.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
#------------------------------------------------------------------------------- tvlog ------------------------------------------------------------------------------#

#------------------------------------------------------------------------------- ITALIA FILM SERIES. ------------------------------------------------------------------------------#

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;-", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def GetTitles(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#.replace('//', 'http://')#\s*?#
#------------------------------------------------------------------------------- FILM PER TUTTI -----------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'):
    
    
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/?paged=' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/?paged=' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
                match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
                for movieUrl, name, img in match + match1:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('Serie Tv','', name)
                        name=re.sub('Serie TV','', name)
                        
                        name=re.sub('-','', name)
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip()}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')      
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#------------------------------------------------------------------------------- FILMSTREAM -----------------------------------------------------------------------------------------#

def GetTitles67(section, url, startPage= '1', numOfPages= '1'):
    
    
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<a href="(.+?)">(.+?)</a><br />').findall(html)
                match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
                for movieUrl, name in match:
                        
                        
                        
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks67', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title': name.strip()}, contextmenu_items= cm, img='', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles67', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img= '', fanart=FanartPath + 'fanart.png')      
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
def GetLinks67(section, url):
        html = net.http_GET(url).content
        
        content = html
        match = re.compile('<a href="(.+?)" class=".+?">').findall(html)
                
                
        match1 = re.compile('SRC="(.+?)"').findall(content)
        
        for url in match :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
#------------------------------------------------------------------------------- ITALIA FILM.co ------------------------------------------------------------------------------#
def GetTitles3(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img src="(.+?)"').findall(html)[:12]
                match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)[:12]
                for movieUrl, name, img in match + match1:
                        cm  = []
                        name=re.sub('Streaming','', name)
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks1a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img='http:' + img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles3', 'url': url.encode('utf-8'), 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img='http:' + img , fanart=img)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
#----------------------------------------------------------------------- links --------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------ FILM PER TUTTI LINKS ---------------------------------------------------------------------------------#

def GetLinks1(section, url):
        html = net.http_GET(url).content
        
        content = html
        match = re.compile('<a href="(.+?)" target="_blank" rel="nofollow">').findall(content)
        match1 = re.compile('SRC="(.+?)"').findall(content)
        
        for url in match + match1 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- FIND MOVIES --------------------------------------------------------------------------------------------#
def GetLinks1a(section, url): 
        html = net.http_GET(url).content
        
        content = html
        match = re.compile('<script src="(.+?)"></script><br/>').findall(content)
        match1 = re.compile('<iframe src="(.+?)" width=".+?" height=".+?" frameborder=".+?" scrolling=".+?" allowfullscreen=".+?">').findall(content)
        match2 = re.compile('<a href="(.+?)" target="_blank">.+?</a><br/>').findall(content)
        
        for url in match + match1 + match2 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url.encode('utf-8')}, {'title':  host.encode('utf-8') }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))



############################### PlayVideo ######################################## PlayVideo ############################################# PlayVideo ###########################

def PlayVideo(url, listitem):
    try:
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------livestreams------------#

def PlayVideo2(url, listitem):
    try:
	xbmc.Player().play(url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Stream may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------myvideolinks------------#

def PlayVideo1(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='https://lh5.googleusercontent.com/-p2h0tx7Trgs/Uzu-3kxzKuI/AAAAAAAAOsU/sVJKqxSMY-4/s319/watch2.jpg', thumbnailImage= 'http://s29.postimg.org/8z8jd5x5j/logo1.png')
        li.setProperty('fanart_image', 'http://littletechboy.com/downloads/sins/modding/LoadingSplash.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

#-------m3u playlists------------#

def PlayVideo5(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]LOAD STREAM PLAYLIST[/B][/COLOR]  >> ', iconImage='http://www.creation-spip.fr/IMG/arton37.png?1357155686', thumbnailImage= 'http://www.creation-spip.fr/IMG/arton37.png?1357155686')
        li.setProperty('fanart_image', 'http://littletechboy.com/downloads/sins/modding/LoadingSplash.jpg') 
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

#--------------------------------------------------------------------------------------------------#

def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain

#--------------------------------------------------------------------------------------------------#

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################
############################# menus ################################## menus ########################################################### menus ################################


def MainMenu():    #homescreen
        addon.add_directory({'mode': 'CB01'}, {'title':  '(HD Movies) [COLOR red][B]CB01.eu >[/B][/COLOR] >'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MovieMenu'}, {'title':  '(Movies) [COLOR lime][B]Film per Tutti >[/B][/COLOR] >'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SportMenu'}, {'title':  '(Movies) [COLOR lime][B]ItaliaFilm >[/B][/COLOR] >'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'DARKSTREAM'}, {'title':  '(Movies) [COLOR lime][B]DarkstreamTV >[/B][/COLOR] >'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'FILMSTREAMRE'}, {'title':  '(Movies) [COLOR lime][B]Filmstream.re >[/B][/COLOR] >'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL69 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '(Movies) [COLOR lime][B]Film Senza Limiti[/B][/COLOR] >>'}, img=IconPath + 'filmsenzalimiti.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'GetTitles65', 'section': 'ALL', 'url': BASE_URL24 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '(TV Shows) [COLOR white][B]ItaliaFilm[/B][/COLOR] >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'GetTitles66', 'section': 'ALL', 'url': BASE_URL25 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '(TV Shows) [COLOR white][B]Film Per Tutti[/B][/COLOR] >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10a', 'section': 'ALL', 'url': BASE_URL68 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '(TV Shows) [COLOR white][B]DarkstreamTV[/B][/COLOR] >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
							 
        addon.add_directory({'mode': 'SearchMenu'}, {'title':  '[COLOR red][B]Search >[/B][/COLOR] >'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def CB01():   #sport
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL82 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR yellow][B]Ultime Uscite[/B][/COLOR] >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL83 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animazione >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
 
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL84 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Avventura >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL85 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Azione >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL86 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comico >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL87 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Commedia >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL88 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentario >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL89 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drammatico >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL90 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'SciFi >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL91 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL92 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Gangster >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL93 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Guerra >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL94 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL95 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Poliziesco >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL96 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sentimentale >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL97 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Storico >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL98 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles13', 'section': 'ALL', 'url': BASE_URL99 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')
							 
def FILMSTREAMRE():   #sport
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL70 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR yellow][B]Ultime Uscite[/B][/COLOR] >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL71 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animazione >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
 
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL72 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Azione >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL73 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comico >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL74 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Commedia >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL75 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL76 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Gangster >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL77 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL78 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Poliziesco >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL79 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Storico >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL80 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'filmstream.png', fanart=FanartPath + 'fanart.png')
        
def DARKSTREAM():   #sport
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL43 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR yellow][B]Saghe Complete[/B][/COLOR] >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL44 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR yellow][B]BLU RAY & DVD[/B][/COLOR] >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL45 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '0-9 >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
 
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL46 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'A >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL47 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'B >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL48 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'C >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL49 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'D >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL50 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'E >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL51 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'F >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL52 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'G >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL53 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'H >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL54 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'I >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL55 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'L >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL56 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'M >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL57 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'N >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL58 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'O >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL59 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'P >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL60 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Q >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL61 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'R >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL62 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'S >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL63 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'T >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL64 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'U >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL65 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'V >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL66 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'W >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL67 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'XYZ >>'}, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')
def SportMenu():   #sport
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL23 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]Ultime Uscite DVD[/B][/COLOR] >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL26 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]HD Films[/B][/COLOR] >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL41 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Al Cinema >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
 
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL27 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Avventura >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL28 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Commedia >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL29 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comici >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL30 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'SciFi >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL31 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Azione >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL32 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drammatici >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL33 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animazione >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL34 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romantici >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL35 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL36 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL37 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Guerra >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL38 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Poliziesco >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL39 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL40 + '',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'italiafilm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#
#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#
#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#
#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#
#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#
#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#


def MovieMenu():   #movies
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' ALL MOVIES >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL2 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' HD MOVIES >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')

        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL3 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' Animazione >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL4 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' Avventura >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL5 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' Azione >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL6 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' Biografico >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL7 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' Comico >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL8 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  ' Commedia >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL9 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentario >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL10 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drammatico >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL11 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'SciFi >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL12 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL13 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Gangster >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL14 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Guerra >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL15 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL16 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL17 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Poliziesco >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL18 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Storico >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL19 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL20 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'filmpertutti.png', fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################searchmenu###############################################################################################

def SearchMenu():
        addon.add_directory({'mode': 'GetSearchQuery11'},  {'title': '[COLOR yellow][B]Search Movies >[/B][/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery12'},  {'title':  '[COLOR yellow][B]Search TV Shows >[/B][/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

########################################################################search#################################################################################################


def GetSearchQuery11():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR yellow]Search Movies[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search11(query)
	else:
                return
def Search11(query):
    try:
     url = 'http://www.cb01.eu/?s=' + query 
     url = url.replace(' ', '+')
     html = net.http_GET(url).content
     match=re.compile('<a href="(.+?)"> <h1>(.+?)</h1></a>').findall(html)
     match_next=re.compile("<link rel='next' href='(.+?)'/>").findall(html)
     for movieUrl, name in match:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('speedvideo.net', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                        
                        						
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.filmx/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks13', 'section': section, 'url': movieUrl}, {'title':  name.strip() + '[COLOR red]...(CB01.eu)[/COLOR]'}, contextmenu_items= cm, img=IconPath + 'cb01.png', fanart=FanartPath + 'fanart.png')

    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Cb01.eu not found [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")



    try:
        url = 'http://www.filmpertutti.co/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
        match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
        for movieUrl, name, img in match + match1:
                cm  = []
                name=re.sub('Link to','', name)
                name=re.sub('Serie Tv','', name)
                name=re.sub('Serie TV','', name)
                       
                
                        						
                
                
                addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip() + '[COLOR lime]...(Filmpertutti)[/COLOR]'}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]FILM PER TUTTI [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.italia-film.co/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img src="(.+?)"').findall(html)
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)
        for movieUrl, name, img in match + match1:
                cm  = []
                name=re.sub('Streaming','', name)
                name=re.sub('Serie Tv','', name)
                name=re.sub('Serie TV','', name)
                name=re.sub('serie tv','', name)
                name=re.sub('streaming','', name)				
                addon.add_directory({'mode': 'GetLinks1a', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip() + '[COLOR orange]...(ItaliaFilm)[/COLOR]'}, contextmenu_items= cm, img='http:' + img, fanart=FanartPath + 'fanart.png')    
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]ITALIA FILM [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.darkstream.tv/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match=re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)">').findall(html)
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)
        for movieUrl, name in match:
                cm  = []
                name=re.sub('Streaming','', name)
                
                
               
                				
                addon.add_directory({'mode': 'GetLinks10', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip() + '[COLOR green]...(Darkstreamtv)[/COLOR]'}, contextmenu_items= cm, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')    
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]DARKSTREAM [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.filmsenzalimiti.co/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match=re.compile('<a href="(.+?)">\s*<img src="(.+?)" alt=".+?" title="(.+?)"').findall(html)
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)
        for movieUrl,img, name in match:
                cm  = []
                name=re.sub('Streaming','', name)
                
                
               
                				
                addon.add_directory({'mode': 'GetLinks11', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip() + '[COLOR cyan]...(FilmsenzaLimiti)[/COLOR]'}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')    
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]DARKSTREAM [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

		


##------------------------------------------------------------- mega tv search-------------------------------------------------------------------------------------------##


def GetSearchQuery12():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR yellow]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search12(query)
	else:
                return
def Search12(query):
    try:
        url = 'http://www.italia-film.co/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img src="(.+?)"').findall(html)
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)
        for movieUrl, name, img in match + match1:
                cm  = []
                name=re.sub('Streaming','', name)
                name=re.sub('Serie Tv','', name)
                name=re.sub('Serie TV','', name)
                name=re.sub('serie tv','', name)
                name=re.sub('streaming','', name)				
                addon.add_directory({'mode': 'GetTitles65b', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name + '[COLOR orange]...(ItaliaFilm)[/COLOR]'}, contextmenu_items= cm, img='http:' + img, fanart=FanartPath + 'fanart.png')    
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]ITALIA FILM [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.filmpertutti.co/search/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
        match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(html)
        for movieUrl, name, img in match + match1:
                        cm  = []
                        name=re.sub('Link to','', name)
                        name=re.sub('Serie Tv','', name)
                        name=re.sub('Serie TV','', name)
                        name=re.sub('speedvideo.net', '[COLOR lime]--- EPISODES ---[/COLOR]' , name)
                        
                        						
                        addon.add_directory({'mode': 'GetTitles66b', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name.strip() + '[COLOR lime]...(Filmpertutti)[/COLOR]'}, contextmenu_items= cm, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]FILM PER TUTTI [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.darkstream.tv/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match=re.compile('<a href="(.+?)" rel="bookmark" title="(.+?)">').findall(html)
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(html)
        for movieUrl, name in match + match1:
                cm  = []
                name=re.sub('Streaming','', name)
                name=re.sub('Serie Tv','', name)
                name=re.sub('Serie TV','', name)
                name=re.sub('serie tv','', name)
                name=re.sub('streaming','', name)				
                addon.add_directory({'mode': 'GetLinks10a', 'section': section, 'url': movieUrl.encode('utf-8')}, {'title':  name + '[COLOR green]...(Darkstreamtv)[/COLOR]'}, contextmenu_items= cm, img=IconPath + 'darkstream.png', fanart=FanartPath + 'fanart.png')    
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]DARKSTREAM [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

                        # addon.add_directory({'mode': 'GetTitles65b', 'section': section, 'url': movieUrl}, {'title':  name.strip() }, contextmenu_items= cm, img='http:' + img, fanart=FanartPath + 'fanart.png')    
                # addon.add_directory({'mode': 'GetTitles65', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img='', fanart=FanartPath + 'fanart.png')
                # addon.add_directory({'mode': 'backtomain'}, {'title':  '[COLOR yellow][B]Home Menu >>[/B][/COLOR] '}, img=IconPath + 'fimpertutti.png', fanart=FanartPath + 'fanart.png')


##.replace('/', ' ')## \s*? ##
###################################################################################### setViews ##########################################################################

def setView(content, viewType):

	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

##############################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles11': 
	GetTitles11(section, url, startPage, numOfPages)
elif mode == 'GetTitles13': 
	GetTitles13(section, url, startPage, numOfPages)
elif mode == 'GetLinks12':
	GetLinks12(section, url)
elif mode == 'GetTitles12': 
	GetTitles12(section, url, startPage, numOfPages)
elif mode == 'GetTitles66':
	GetTitles66(section, url, startPage, numOfPages)
elif mode == 'GetTitles66b':
	GetTitles66b(section, url, startPage, numOfPages)
elif mode == 'GetLinks60':
	GetLinks60(section, url)
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles2a': 
	GetTitles2a(query)
elif mode == 'GetTitles2b': 
	GetTitles2b(query)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles10': 
	GetTitles10(section, url, startPage, numOfPages)
elif mode == 'GetTitles10a': 
	GetTitles10a(section, url, startPage, numOfPages)
elif mode == 'GetTitles14': 
	GetTitles14(section, url, startPage, numOfPages)
elif mode == 'GetTitles15': 
	GetTitles15(section, url, startPage, numOfPages)
elif mode == 'GetTitles15a': 
	GetTitles15a(section, url, startPage, numOfPages)
elif mode == 'GetTitles15b': 
	GetTitles15b(section, url, startPage, numOfPages)
elif mode == 'GetTitles16': 
	GetTitles16(section, url, startPage, numOfPages)
elif mode == 'GetTitles20': 
	GetTitles20(section, url, startPage, numOfPages)
elif mode == 'GetTitles21': 
	GetTitles21(section, url, startPage, numOfPages)
elif mode == 'GetTitles23': 
	GetTitles23(section, url, startPage, numOfPages)
elif mode == 'GetTitles25': 
	GetTitles25(section, url, startPage, numOfPages)
elif mode == 'GetTitles27': 
	GetTitles27(section, url, startPage, numOfPages)
elif mode == 'GetTitles27a': 
	GetTitles27a(section, url, startPage, numOfPages)
elif mode == 'GetTitles28': 
	GetTitles28(section, url, startPage, numOfPages)
elif mode == 'GetTitles28a': 
	GetTitles28a(section, url, startPage, numOfPages)
elif mode == 'GetTitles31': 
	GetTitles31(section, url, startPage, numOfPages)
elif mode == 'GetTitles31a': 
	GetTitles31a(section, url, startPage, numOfPages)
elif mode == 'GetTitles32': 
	GetTitles32(section, url, startPage, numOfPages)
elif mode == 'GetTitles32a': 
	GetTitles32a(section, url, startPage, numOfPages)
elif mode == 'GetTitles32b': 
	GetTitles32b(section, url, startPage, numOfPages)
elif mode == 'GetTitles34': 
	GetTitles34(section, url, startPage, numOfPages)
elif mode == 'GetTitles35': 
	GetTitles35(url)
elif mode == 'GetTitles35a': 
	GetTitles35a(url)
elif mode == 'GetTitles37': 
	GetTitles37(url)
elif mode == 'GetTitles38': 
	GetTitles38(section, url, startPage, numOfPages)
elif mode == 'GetTitles38a': 
	GetTitles38a(url)
elif mode == 'GetTitles38b': 
	GetTitles38b(url)
elif mode == 'GetTitles38c': 
	GetTitles38c(section, url, startPage, numOfPages)
elif mode == 'GetTitles39': 
	GetTitles39(section, url, startPage, numOfPages)
elif mode == 'GetTitles40': 
	GetTitles40(section, url, startPage, numOfPages)
elif mode == 'GetTitles41': 
	GetTitles41(section, url, startPage, numOfPages)
elif mode == 'GetTitles41a': 
	GetTitles41a(query, startPage, numOfPages)
elif mode == 'GetTitles42': 
	GetTitles42(section, url, startPage, numOfPages)
elif mode == 'GetTitles43': 
	GetTitles43(section, url, startPage, numOfPages)
elif mode == 'GetTitles44': 
	GetTitles44(section, url, startPage, numOfPages)
elif mode == 'GetTitles45': 
	GetTitles45(section, url, startPage, numOfPages)
elif mode == 'GetTitles46': 
	GetTitles46(section, url, startPage, numOfPages)
elif mode == 'GetTitles46a': 
	GetTitles46a(url)
elif mode == 'GetTitles48': 
	GetTitles48(section, url, startPage, numOfPages)
elif mode == 'GetTitles48a': 
	GetTitles48a(url)
elif mode == 'GetTitles49': 
	GetTitles49(query)
elif mode == 'GetTitles50': 
	GetTitles50(section, url, startPage, numOfPages)
elif mode == 'GetTitles51': 
	GetTitles51(section, url, startPage, numOfPages)
elif mode == 'GetTitles52': 
	GetTitles52(section, url, startPage, numOfPages)
elif mode == 'GetTitles53': 
	GetTitles53(section, url, startPage, numOfPages)
elif mode == 'GetTitles53a': 
	GetTitles53a(section, url, startPage, numOfPages)
elif mode == 'GetTitles54': 
	GetTitles54(section, url, startPage, numOfPages)
elif mode == 'GetTitles55': 
	GetTitles55(section, url, startPage, numOfPages)
elif mode == 'GetTitles56': 
	GetTitles56(section, url, startPage, numOfPages)
elif mode == 'GetTitles57': 
	GetTitles57(section, url, startPage, numOfPages)
elif mode == 'GetTitles58': 
	GetTitles58(section, url, startPage, numOfPages)
elif mode == 'GetTitles58a': 
	GetTitles58a(section, url, startPage, numOfPages)
elif mode == 'GetTitles59': 
	GetTitles59(section, url, startPage, numOfPages)
elif mode == 'GetTitles60': 
	GetTitles60(section, url, startPage, numOfPages)
elif mode == 'GetTitles61': 
	GetTitles61(section, url, startPage, numOfPages)
elif mode == 'GetTitles61a': 
	GetTitles61a(section, url, startPage, numOfPages)
elif mode == 'GetTitles62': 
	GetTitles62(query)
elif mode == 'GetTitles62a': 
	GetTitles62a(query)
elif mode == 'GetTitles64': 
	GetTitles64(section, url, startPage, numOfPages)
elif mode == 'GetTitles64a': 
	GetTitles64a(section, url, startPage, numOfPages)
elif mode == 'GetTitles64b': 
	GetTitles64b(section, url, startPage, numOfPages)
elif mode == 'GetTitles65': 
	GetTitles65(section, url, startPage, numOfPages)
elif mode == 'GetTitles66': 
	GetTitles66(section, url, startPage, numOfPages)
elif mode == 'GetTitles67': 
	GetTitles66(section, url, startPage, numOfPages)
elif mode == 'GetTitles65b': 
	GetTitles65b(section, url, startPage, numOfPages)

elif mode == 'GetTitles67a': 
	GetTitles67a(url, text)
elif mode == 'GetTitles67b': 
	GetTitles67b(url, text)
elif mode == 'GetTitles67c': 
	GetTitles67c(url, text)
elif mode == 'GetTitles67d': 
	GetTitles67d(url, text, urlurl)
elif mode == 'GetTitles67e': 
	GetTitles67e(url, text, urlurl)
elif mode == 'GetTitles68': 
	GetTitles68(section, url)
elif mode == 'GetTitles68a': 
	GetTitles68a(section, url)
elif mode == 'GetTitles69': 
	GetTitles69(section, url, startPage, numOfPages)
elif mode == 'GetTitles70': 
	GetTitles70(section, url, startPage, numOfPages)
elif mode == 'GetTitles71': 
	GetTitles71(section, url, startPage, numOfPages)
elif mode == 'GetTitles72': 
	GetTitles72(section, url, startPage, numOfPages)
elif mode == 'GetTitles75': 
	GetTitles75(section, url, startPage, numOfPages)
elif mode == 'GetTitles75a': 
	GetTitles75a(img, section, url)
elif mode == 'GetTitles76': 
	GetTitles76(section, url, startPage, numOfPages)
elif mode == 'GetTitles81': 
	GetTitles81(section, url, startPage, numOfPages)
elif mode == 'GetTitles143': 
	GetTitles143(section, url)
elif mode == 'GetTitles143a': 
	GetTitles143a(query, section)
elif mode == 'GetTitles144': 
	GetTitles144(query, section)
elif mode == 'GetTitles145': 
	GetTitles145(url, text)
elif mode == 'GetTitles145a': 
	GetTitles145a(url, text)
elif mode == 'GetTitles145b': 
	GetTitles145b(url, text)
elif mode == 'Categorieswco':
        Categorieswco(url)
elif mode == 'Categorieswoc':
        Categorieswoc(url)
elif mode == 'Categories':
        Categories(url)
elif mode == 'Categories1':
        Categories1(url)
elif mode == 'Categories2':
        Categories2(url)
elif mode == 'Categoriesuwf':
        Categoriesuwf(url)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks1a':
	GetLinks1a(section, url)
elif mode == 'GetLinks1b':
	GetLinks1b(section, url)
elif mode == 'GetLinks1c':
	GetLinks1c(section, url)
elif mode == 'GetLinks1d':
	GetLinks1d(section, url)
elif mode == 'GetLinks1e':
	GetLinks1e(section, url)
elif mode == 'GetLinks5':
	GetLinks5(section, url)
elif mode == 'GetLinks7':
	GetLinks7(section, url)
elif mode == 'GetLinks8':
	GetLinks8(section, url)
elif mode == 'GetLinks9':
	GetLinks9(url)
elif mode == 'GetLinks9a':
	GetLinks9a(url)
elif mode == 'GetLinks10':
	GetLinks10(section, url)
elif mode == 'GetLinks10a':
	GetLinks10a(section, url)
elif mode == 'GetLinks11':
	GetLinks11(section, url)
elif mode == 'GetLinks67':
	GetLinks67(section, url)
elif mode == 'GetLinks12a':
	GetLinks12a(section, url)
elif mode == 'GetLinks13':
	GetLinks13(section, url)
elif mode == 'GetLinks13a':
	GetLinks13a(section, url)
elif mode == 'GetLinks14':
	GetLinks14(section, url)
elif mode == 'GetLinks16':
	GetLinks16(section, url)
elif mode == 'GetLinks17':
	GetLinks17(section, url)
elif mode == 'GetLinks18':
	GetLinks18(section, url)
elif mode == 'GetLinks18a':
	GetLinks18a(section, url)
elif mode == 'GetLinks19':
	GetLinks19(section, url)
elif mode == 'GetLinks20':
	GetLinks20(section, url)
elif mode == 'GetLinks21':
	GetLinks21(section, url)
elif mode == 'GetLinks21a':
	GetLinks21a(section, url)
elif mode == 'GetLinks22':
	GetLinks22(section, url)
elif mode == 'GetLinks23':
	GetLinks23(section, url)
elif mode == 'GetLinks24':
	GetLinks24(section, url)
elif mode == 'GetLinks99':
	GetLinks99(section, url)
elif mode == 'GetLinks99a':
	GetLinks99a(section, url)
elif mode == 'GetLinks55':
	GetLinks55(section, url)
elif mode == 'GetLinks55a':
	GetLinks55a(section, url)
elif mode == 'GetLinks81':
	GetLinks81(section, url)
elif mode == 'GetLinks129':
        GetLinks129(section, url)
elif mode == 'GetLinks130':
        GetLinks130(section, url)
elif mode == 'GetLinks130a':
        GetLinks130a(section, url)
elif mode == 'GetLinks131':
        GetLinks131(section, url)
elif mode == 'GetLinks132':
        GetLinks132(section, url)
elif mode == 'GetLinks133':
        GetLinks133(section, url)
elif mode == 'GetLinks99b':
	GetLinks99b(section, url)
elif mode == 'GetLinks60':
	GetLinks60(section, url)
elif mode == 'GetLinks75':
	GetLinks75(section, url)
elif mode == 'GetLinks145':
	GetLinks145(section, url, text)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'GetSearchQuery5':
	GetSearchQuery5()
elif mode == 'Search5':
	Search5(query)
elif mode == 'GetSearchQuery11':
	GetSearchQuery11()
elif mode == 'Search11':
	Search11(query)
elif mode == 'GetSearchQuery12':
	GetSearchQuery12()
elif mode == 'Search12':
	Search12(query)
elif mode == 'GetSearchQuery14':
	GetSearchQuery14()
elif mode == 'Search14':
	Search14(query)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery3':
	GetSearchQuery3()
elif mode == 'Search3':
	Search3(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
elif mode == 'PlayVideo2':
	PlayVideo2(url, listitem)
elif mode == 'PlayVideo4':
	PlayVideo4(url, listitem)	
elif mode == 'PlayVideo5':
	PlayVideo5(url, listitem)
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'SearchMenu':
        SearchMenu()
elif mode == 'ShowMenu':
        ShowMenu(urlurl)
elif mode == 'MovieMenu':
        MovieMenu()
elif mode == 'DocMenu':
        DocMenu()
elif mode == 'KidsMenu':
        KidsMenu()
elif mode == 'TvMenu':
        TvMenu()
elif mode == 'MusicMenu':
        MusicMenu()
elif mode == 'WtMenu':
        WtMenu()
elif mode == 'RgMenu':
        RgMenu()
elif mode == 'OmpMenu':
        OmpMenu()
elif mode == 'SportMenu':
        SportMenu()
elif mode == 'OmpazMenu':
        OmpazMenu()
elif mode == 'PutMenu':
        PutMenu()
elif mode == 'PuttvMenu':
        PuttvMenu()
elif mode == 'Put1Menu':
        Put1Menu()
elif mode == 'Put2Menu':
        Put2Menu()
elif mode == 'Put3Menu':
        Put3Menu()
elif mode == 'RadioMenu':
        RadioMenu()
elif mode == 'TvsMenu':
        TvsMenu()
elif mode == 'Tvs1Menu':
        Tvs1Menu()
elif mode == 'TsuMenu':
        TsuMenu()
elif mode == 'Tsu1Menu':
        Tsu1Menu()
elif mode == 'Tsu2Menu':
        Tsu2Menu()
elif mode == 'Tsu3Menu':
        Tsu3Menu()
elif mode == 'HqMenu':
        HqMenu()
elif mode == 'Hq4Menu':
        Hq4Menu()
elif mode == 'Hq5Menu':
        Hq5Menu()
elif mode == 'Hq6Menu':
        Hq6Menu()
elif mode == 'Hq7Menu':
        Hq7Menu()
elif mode == 'LiveMenu':
        LiveMenu()
elif mode == 'backtomain':
        MainMenu()

elif mode == 'DARKSTREAM':
        DARKSTREAM()
elif mode == 'FILMSTREAMRE':
        FILMSTREAMRE()
elif mode == 'CB01':
        CB01()
xbmcplugin.endOfDirectory(int(sys.argv[1]))