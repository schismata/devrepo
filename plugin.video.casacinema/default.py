import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,random
from t0mm0.common.addon import Addon
from metahandler import metahandlers
from resources.lib.libraries import cache
from resources.lib.libraries import client
from resources.lib.resolvers import googleplus
from resources.lib.libraries import cloudflare

addon_id = 'plugin.video.casacinema'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

metaset = selfAddon.getSetting('enable_meta')
addon = Addon(addon_id, sys.argv)

def CATEGORIES():
        

        addDir2('Ultimi Film','http://www.casa-cinema.org/genere/film/page/1',1,icon,fanart)
        addDir2('Serie TV','http://www.casa-cinema.org/genere/serie-tv/page/1',3,icon,fanart)
	addDir2('Search TV Shows','http://www.casa-cinema.org/',7,icon,fanart)
	addDir2('Search Movies','http://www.casa-cinema.org/',4,icon,fanart)


def GETLINKSNEW(url,name,iconimage):
		numTries = 7
		host = 0
		urlorig = url
		originalname = name
		try:link = open_url(url)
		except:link = cloudflare.request(url, mobile=True)
		matchlink=re.compile('<iframe class="embed-responsive-item" SRC="(.+?)"').findall(link)
		matchlink2=re.compile("<a style='.+?' href='(.+?)' target='_blank'").findall(link)
		
		for url in matchlink + matchlink2:
						host=url.split('/')[2].replace('www.','').capitalize()
						addLink(host,url,101,icon,'')
					
			
	

def GETEPISODES(url,name):
       try:link = open_url(url)
       except:link = cloudflare.request(url, mobile=True)

        
       metaset = selfAddon.getSetting('enable_meta')
		
       match=re.compile('>\s*(.+?)a\s*href="(.+?)" target="_blank" .+?</a').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
       for name,url in match:
				name = re.sub('<p>','',name)
				name = re.sub('&#215;','x',name)
				name = re.sub('&#8211;','x',name)
				name = re.sub('<','',name)
				# name = re.sub(r"[^\w\s]", '', name)
				host=url.split('/')[2].replace('www.','').capitalize()
				addLink(name + "  " + host,url,101,icon,fanart)
            # except:pass


	
def GETSHOWS(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)

	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			
			curpage = int(pagenum)
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)
	except:pass
        
        metaset = selfAddon.getSetting('enable_meta')
		
        match=re.compile('<div class="box-single-movies">\s*<a href="(.+?)" title="(.+?)" >').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for url,name in match:
                
                
                name=re.sub('3D','',name)
                name=re.sub('Sub-ITA','',name)
                name=re.sub('Serie TV','',name)
                name=re.sub('Serie Tv','',name)
                name=re.sub(r'\[',r'', name)
                name=re.sub(r'\]',r'', name)
                name=re.sub(r'\/',r'', name)
                name= re.sub(r"[^\w\s]", '', name)
                try:
                    addDir3(name,url,6,icon,len(match),isFolder=True)
                except:pass

	try:
                    
					
					addLink('NEXT>>',nextpageurl,3,icon,'')
					
	except: pass		


	
def GETMOVIES(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)

	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			
			curpage = int(pagenum)
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)
	except:pass
        
        metaset = selfAddon.getSetting('enable_meta')
		
        match=re.compile('<div class="box-single-movies">\s*<a href="(.+?)" title="(.+?)" >').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for url,name in match:
                # name=cleanHex(name)
				
                name=re.sub('3D','',name)
                name=re.sub('Sub-ITA','',name)
                name=re.sub('HD 720p','',name)
                name=re.sub('HD','',name)
                name=re.sub(r'\[',r'', name)
                name=re.sub(r'\]',r'', name)
                name=re.sub(r'\/',r'', name)
                name = re.sub(r"[^\w\s]", '', name)
                if metaset=='false':
                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,1,icon,'')
					
	except: pass		
	
	# ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH -------------------------------------------------------- 
def SEARCH():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search Show')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://www.casa-cinema.org/?s=' + search_entered
        GETMOVIES(url,name)
     except: pass

def SEARCHTV():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search CB01')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://www.casa-cinema.org/?s=' + search_entered
        GETSHOWS(url,name)
     except: pass
		
def PLAYMOVIE(name,url):
		if "http" not in url:
		  url = "http:" + url
		try:link = open_url(url)
		except:link = cloudflare.request(url, mobile=True)	
		try:
				stream_url = urlresolver.HostedMediaFile(url).resolve()
				ok=True
				liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
				ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
				xbmc.Player ().play(stream_url,liz)
		except:
				match=re.compile('<a href="(.+?)" class="btn-wrapper link"').findall(link)
				for url in match:
		
					stream_url = urlresolver.HostedMediaFile(url).resolve()
					ok=True
					liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
					ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
					xbmc.Player ().play(stream_url,liz)
			
 
		addLink('Press back to exit','',1,icon,fanart)
        
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

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

def addDir2(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        liz.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir3(name,url,mode,iconimage,itemcount,isFolder=False):
        try:
          if not 'COLOR' in name:
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
          
            meta = mg.get_meta('tvshow', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
            liz.setInfo( type="Video", infoLabels= meta )
            liz.setProperty("IsPlayable","true")
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=False)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
            return ok


		   
        except:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok
def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
        try:
          if not 'COLOR' in name:
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
          
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
            liz.setInfo( type="Video", infoLabels= meta )
            liz.setProperty("IsPlayable","true")
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=False)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
            return ok


		   
        except:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            liz.setProperty("IsPlayable","true")
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
    if selfAddon.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )

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
elif mode==3: GETSHOWS(url,name)
elif mode==4: SEARCH()
elif mode==7: SEARCHTV()
elif mode==1: GETMOVIES(url,name)
elif mode==2: GETLINKSNEW(url,name,iconimage)
elif mode==5: GENRES()
elif mode==6: GETEPISODES(url,name)
elif mode==101: PLAYMOVIE(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

