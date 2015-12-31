import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse
from t0mm0.common.addon import Addon
from metahandler import metahandlers

addon_id = 'plugin.video.portalehd'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
ADDON2=xbmcaddon.Addon(id='plugin.video.portalehd')
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
metaset = selfAddon.getSetting('enable_meta')
base = 'http://www.portalehd.net'
def CATEGORIES():
		addDir2('[COLOR lime]Search[/COLOR]','http://www.portalehd.net/?s=',3,icon,'',fanart)

		addDir2('[COLOR yellow]BDRip[/COLOR]','http://www.portalehd.net/category/bdrip/',6,icon,'',fanart)
		addDir2('[COLOR gold]1080p/720p[/COLOR]','http://www.portalehd.net/category/film-hd',6,icon,'',fanart)
		addDir2('[COLOR gold]DVDRip[/COLOR]','http://www.portalehd.net/category/dvdrip',6,icon,'',fanart)

		addDir2('Al Cinema','http://www.portalehd.net/category/al-cinema',6,icon,'',fanart)
		addDir2('Azione','http://www.portalehd.net/category/azione',6,icon,'',fanart)
		addDir2('Animazione','http://www.portalehd.net/category/animazione',6,icon,'',fanart)
		addDir2('Avventura','http://www.portalehd.net/category/avventura',6,icon,'',fanart)
		addDir2('Commedia','http://www.portalehd.net/category/commedia',6,icon,'',fanart)
		addDir2('Comico','http://www.portalehd.net/category/comico',6,icon,'',fanart)
		addDir2('Drammatico','http://www.portalehd.net/category/drammatico',6,icon,'',fanart)
		addDir2('Documentario','http://www.portalehd.net/category/documentario',6,icon,'',fanart)
		addDir2('Fantascienza','http://www.portalehd.net/category/fantascienza',6,icon,'',fanart)
		addDir2('Fantasy','http://www.portalehd.net/category/fantasy',6,icon,'',fanart)
		addDir2('Gangster','http://www.portalehd.net/category/gangster',6,icon,'',fanart)
		addDir2('Guerra','http://www.portalehd.net/category/guerra',6,icon,'',fanart)
		addDir2('Horror','http://www.portalehd.net/category/horror',6,icon,'',fanart)
		addDir2('Noir','http://www.portalehd.net/category/noir',6,icon,'',fanart)
		addDir2('Poliziesco','http://www.portalehd.net/category/poliziesco',6,icon,'',fanart)
		addDir2('Sentimentale','http://www.portalehd.net/category/sentimentale',6,icon,'',fanart)
		addDir2('Thriller','http://www.portalehd.net/category/thriller',6,icon,'',fanart)
		addDir2('Western','http://www.portalehd.net/category/western',6,icon,'',fanart)

	

		
def GETITALIAFIM(url,name):
        
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<a href="(.+?)" title="(.+?)">\s*<figure><img src="(.+?)"').findall(link)[:15]
		
        for url,name,img in match:
                        # name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('SubITA','', name)
                       
                        addDir2(name,url,10,img,'',img)
                
        try:
               
                match=re.compile('<a class="nextpostslink" rel="next" href="(.+?)">').findall(link)
                
                url= match[0]
                addDir2('[COLOR yellow]Next Page >>[/COLOR]',url,6,icon,'',fanart)
        except: pass
def GETLINK(url,name):
        
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<script type="text/javascript" src="(.+?)">').findall(link)
        match2=re.compile('src="(.+?)" frameborder=".+?" allowfullscreen>').findall(link)                
        for url in match + match2:
                        name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('SubITA','', name)
                        name=re.sub('-','', name)
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host + '  Play >>>',url,11,icon,'',fanart)
                
	
def PLAYLINKMOVIEWATCHER(name,url,iconimage):
        name=selfAddon.getSetting('namestore')
        stream_url=urlresolver.resolve(url)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url)

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))


def SEARCHMOVIES():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Cerca Film')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
        url = 'http://www.portalehd.net/?s='+ search_entered
        link = open_url(url)
        GETITALIAFIM(url,name)


		
def PLAYITALIAHDFILM(name,url,iconimage):
        link = open_url(url)
        try: url=re.compile('src="http://videomega.tv/(.+?)"').findall(link)[0]
        except: url=re.compile("src='(.+?)' allowFullScreen></iframe>").findall(link)[0]
        ua='|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
        #### THANKS TO LAMBDA ####
        import client
        import jsunpack
        url = urlparse.urlparse(url).query
        url = urlparse.parse_qsl(url)[0][1]
        url = 'http://videomega.tv/cdn.php?ref=%s' % url
        result = client.request(url)
        unpacked = ''
        packed = result.split('\n')
        for i in packed: 
            try: unpacked += jsunpack.unpack(i)
            except: unpacked += i
        result = unpacked
        result = re.sub('\s\s+', ' ', result)
        url = re.compile('"video".+?"src"\s*\,\s*"(.+?)"').findall(result)
        url += client.parseDOM(result, 'source', ret='src', attrs = {'type': 'video.+?'})
        url = url[0]+ua
        #### THANKS TO LAMBDA ####

        ok=True
        liz=xbmcgui.ListItem(name, iconImage=icon,thumbnailImage=icon); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(url, liz, False)




def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def addLink(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

		




		
def addDir2(name,url,mode,iconimage,description,fanart):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=iconImage, thumbnailImage=img)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok
        
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON2.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON2.getSetting(viewType) )

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
print params

if mode==None or url==None or len(url)<1: CATEGORIES()

elif mode==6: GETITALIAFIM(url,name)
elif mode==3: SEARCHMOVIES()
elif mode==10: GETLINK(url,name)
elif mode==11: PLAYLINKMOVIEWATCHER(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

