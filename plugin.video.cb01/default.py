import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,random
from t0mm0.common.addon import Addon
from metahandler import metahandlers
from resources.lib.libraries import cache
from resources.lib.libraries import client
from resources.lib.resolvers import googleplus
from resources.lib.libraries import cloudflare

addon_id = 'plugin.video.cb01'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

metaset = selfAddon.getSetting('enable_meta')
addon = Addon(addon_id, sys.argv)

def CATEGORIES():
        
        addDir2('[COLOR gold]Ultime Uscite[/COLOR]','http://www.cb01.co/category/hd-alta-definizione/page/1/',1,icon,fanart)
        addDir2('[COLOR lime]TV Shows[/COLOR]','http://www.cb01.co/serietv/page/1/',4,icon,fanart)
        addDir2('[COLOR white]Generi[/COLOR]','http://www.cb01.co/category/hd-alta-definizione/',5,icon,fanart)

	addDir2('Search Movies','http://www.cb01.co/',3,icon,fanart)
	addDir2('Search TV Shows','http://www.cb01.co/',7,icon,fanart)
def GENRES():
        
        addDir2('Animazione','http://www.cb01.co/category/hd-alta-definizione/animazione-hd/page/1/',1,icon,fanart)
        addDir2('Avventura','http://www.cb01.co/category/hd-alta-definizione/avventura-hd/page/1/',1,icon,fanart)
        addDir2('Azione','http://www.cb01.co/category/hd-alta-definizione/azione-hd/page/1/',1,icon,fanart)
        addDir2('Comico','http://www.cb01.co/category/hd-alta-definizione/comico-hd/page/1/',1,icon,fanart)
        addDir2('Commedia','http://www.cb01.co/category/hd-alta-definizione/commedia-hd/page/1/',1,icon,fanart)
        addDir2('Drammatico','http://www.cb01.co/category/hd-alta-definizione/drammatico-hd/page/1/',1,icon,fanart)
        addDir2('Fantascienza','http://www.cb01.co/category/hd-alta-definizione/fantascienza-hd/page/1/',1,icon,fanart)
        addDir2('Fantasy','http://www.cb01.co/category/hd-alta-definizione/fantasy-fantastico-hd/page/1/',1,icon,fanart)
        addDir2('Gangster','http://www.cb01.co/category/hd-alta-definizione/gangster-hd/page/1/',1,icon,fanart)
        addDir2('Guerra','http://www.cb01.co/category/hd-alta-definizione/guerra-hd/page/1/',1,icon,fanart)
        addDir2('Horror','http://www.cb01.co/category/hd-alta-definizione/horror-hd/page/1/',1,icon,fanart)
        addDir2('Poliziesco','http://www.cb01.co/category/hd-alta-definizione/poliziesco-hd/page/1/',1,icon,fanart)
        addDir2('Romantico','http://www.cb01.co/category/hd-alta-definizione/sentimentale-hd/page/1/',1,icon,fanart)
        addDir2('Storico','http://www.cb01.co/category/hd-alta-definizione/storico-hd/page/1/',1,icon,fanart)
        addDir2('Thriller','http://www.cb01.co/category/hd-alta-definizione/thriller-hd/page/1/',1,icon,fanart)
        addDir2('Western','http://www.cb01.co/category/hd-alta-definizione/western-hd/page/1/',1,icon,fanart)


def GETLINKSNEW(url,name,iconimage):
        originalname = name
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(link)
		
        for url, name in match:
			
     		addDir2(name,url,101,icon,fanart)
 
 
				
                       
                        # addLink(originalname + "   ",url,100,icon,fanart)		

def GETSHOWS(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)

	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			pagenum=pagenum[0]
			curpage = int(pagenum)
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
        
        metaset = selfAddon.getSetting('enable_meta')
		
        match=re.compile('<a href="(.+?)"> <h1>(.+?)</h1></a>').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
				
                name=re.sub('3D','',name)
                name=re.sub('Sub-ITA','',name)
                name=re.sub('HD 720p','',name)
                name=re.sub('HD','',name)
                name=re.sub(r'\[',r'', name)
                name=re.sub(r'\]',r'', name)
                name=re.sub(r'\/',r'', name)
                if metaset=='false':
                        try:
                                addDir3(name,url,6,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir3(name,url,6,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,4,icon,'')
					
	except: pass	

def GETEPISODES(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)

	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			pagenum=pagenum[0]
			curpage = int(pagenum)
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
        
        metaset = selfAddon.getSetting('enable_meta')
		
        match=re.compile('>(.+?)<a href="(.+?)" target="_blank">(.+?)</a').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for ep,url,name in match:
                # name=cleanHex(name)
				
                ep=re.sub('&#8211;','',ep)
                ep=re.sub('&#8217;','',ep)
                ep=re.sub('1&#215;','',ep)
                ep=re.sub('<strong>','',ep)
                name=re.sub('Sub-ITA','',name)
                name=re.sub('HD 720p','',name)
                name=re.sub('HD','',name)
                name=re.sub(r'\[',r'', name)
                name=re.sub(r'\]',r'', name)
                name=re.sub(r'\/',r'', name)
                if metaset=='false':
                        try:
                                addLink(ep + '  ' + name,url,101,icon,'')
                        except:pass
                else:
                        try:
                                addLink(ep + '  ' + name,url,101,icon,'')
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,4,icon,'')
					
	except: pass	

	
def GETMOVIES(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)

	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			pagenum=pagenum[0]
			curpage = int(pagenum)
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
        
        metaset = selfAddon.getSetting('enable_meta')
		
        match=re.compile('<a href="(.+?)"> <h1>(.+?)</h1></a>').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
				
                name=re.sub('3D','',name)
                name=re.sub('Sub-ITA','',name)
                name=re.sub('HD 720p','',name)
                name=re.sub('HD','',name)
                name=re.sub(r'\[',r'', name)
                name=re.sub(r'\]',r'', name)
                name=re.sub(r'\/',r'', name)
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
    keyboard = xbmc.Keyboard(search_entered, 'Search CB01')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://www.cb01.co/?s=' + search_entered
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
    	url = 'http://www.cb01.co/?s=' + search_entered
        GETSHOWS(url,name)
     except: pass
		
def PLAYMOVIE(name,url):
        if "http" not in url:
		  url = "http:" + url
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=True)	
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
            liz.addContextMenuItems(contextMenuItems, replaceItems=True)
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
            liz.addContextMenuItems(contextMenuItems, replaceItems=True)
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
elif mode==4: GETSHOWS(url,name)
elif mode==3: SEARCH()
elif mode==7: SEARCHTV()
elif mode==1: GETMOVIES(url,name)
elif mode==2: GETLINKSNEW(url,name,iconimage)
elif mode==5: GENRES()
elif mode==6: GETEPISODES(url,name)
elif mode==101: PLAYMOVIE(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

