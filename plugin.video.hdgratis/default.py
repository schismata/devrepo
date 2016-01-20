import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,random
from t0mm0.common.addon import Addon
from metahandler import metahandlers
from resources.lib.libraries import cache
from resources.lib.libraries import client
from resources.lib.resolvers import googleplus
from resources.lib.libraries import cloudflare

addon_id = 'plugin.video.hdgratis'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
icon2 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'genere.png'))
icon3 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'cerca.png'))
icon4 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'play.png'))
metaset = selfAddon.getSetting('enable_meta')
addon = Addon(addon_id, sys.argv)

def CATEGORIES():

	addDir2('[COLOR white]Ultime Uscite[/COLOR]','http://hdgratis.net/nuove-uscite/page/1/',1,icon,fanart)
	addDir2('[COLOR white]Al Cinema[/COLOR]','http://hdgratis.net/in-sala/page/1/',1,icon,fanart)
        
        addDir2('[COLOR white]Generi[/COLOR]','http://hdgratis.net/in-sala/',5,icon2,fanart)

	addDir2('Cerca Film','http://hdgratis.net/film/',3,icon3,fanart)
	
def GENRES():
        
        addDir2('Animazione','http://hdgratis.net/film/animazione/page/1/',1,icon2,fanart)
        addDir2('Avventura','http://hdgratis.net/film/avventura/page/1/',1,icon2,fanart)
        addDir2('Azione','http://hdgratis.net/film/azione/page/1/',1,icon2,fanart)
        addDir2('Comico','http://hdgratis.net/film/comico/page/1/',1,icon2,fanart)
        addDir2('Commedia','http://hdgratis.net/film/commedia/page/1/',1,icon2,fanart)
        addDir2('Drammatico','http://hdgratis.net/film/drammatico/page/1/',1,icon2,fanart)
        addDir2('Fantascienza','http://hdgratis.net/film/fantascienza/page/1/',1,icon2,fanart)
        addDir2('Fantasy','http://hdgratis.net/film/fantasy/page/1/',1,icon2,fanart)
       
        addDir2('Guerra','http://hdgratis.net/film/guerra/page/1/',1,icon2,fanart)
        addDir2('Horror','http://hdgratis.net/film/horror/page/1/',1,icon2,fanart)
        
        addDir2('Romantico','http://hdgratis.net/film/romantico/page/1/',1,icon2,fanart)
        addDir2('Storico','http://hdgratis.net/film/storico/page/1/',1,icon2,fanart)
        addDir2('Thriller','http://hdgratis.net/film/thriller/page/1/',1,icon2,fanart)
        addDir2('Giallo','http://hdgratis.net/film/giallo/page/1/',1,icon2,fanart)


def GETLINKSNEW(url,name,iconimage):
        originalname = name
        try:link = open_url(url)
        except:link = cloudflare.request(url, mobile=False)
		
        match=re.compile('<iframe .+? src="http://hdpass.link/(.+?)"').findall(link)
		
        for url in match:
			if "download" not in url:
				url = "http://hdpass.link/" + url
				try:link = open_url(url)
				except:link = cloudflare.request(url)
				matchnew=re.compile('src="(.+?)"\s*type=".+?"\s*label="(.+?)"').findall(link)
				for url,name in matchnew:
				
					addDir2("Quality: "+name,url,101,icon4,fanart)
                       
                        # # addLink(originalname + "   ",url,100,icon,fanart)		
		# match2=re.compile('<input type="hidden" name="play_chosen" value="(.+?)"/>\s*<input type="hidden" name="idFilm" value="(.+?)"/>\s*<input type="submit" .+? name="mir_pl" value="(.+?)"/>').findall(link)  
		# for name,id,value in match2:
			# url = "http://hdpass.link/film.php?play_chosen=" + name + "&idFilm=" + id + "&mir_pl=" + value
			# addDir2("Other links: "+name,url,101,icon4,fanart)

	
def GETMOVIES(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url,mobile=False)

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
		
        match=re.compile('<a href="(.+?)" title="(.+?)">').findall(link)
		
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
def GETSEARCH(url,name):
        try:link = open_url(url)
        except:link = cloudflare.request(url,mobile=False)


        
        metaset = selfAddon.getSetting('enable_meta')
		
        match=re.compile('<a href="(.+?)" title=".+?">\s*<h2 class="title-list">(.+?)</h2>').findall(link)
		
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
				
                # name=re.sub('3D','',name)
                # name=re.sub('Sub-ITA','',name)
                # name=re.sub('HD 720p','',name)
                # name=re.sub('HD','',name)
                # name=re.sub(r'\[',r'', name)
                # name=re.sub(r'\]',r'', name)
                # name=re.sub(r'\/',r'', name)
                if metaset=='false':
                        try:
                                addDir2(name,url,2,icon,len(match),isFolder=True)
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
    keyboard = xbmc.Keyboard(search_entered, 'Search Movie')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://hdgratis.net/?s=' + search_entered
        GETSEARCH(url,name)
     except: pass


def PLAYMOVIE(name,url):
	try:
		xbmc.Player ().play(url)
		addLink("Press Back to exit",url,'',icon,fanart)
  	
	except:
		resp = urllib2.urlopen(url)
		url2 = resp.geturl()
		stream_url = urlresolver.HostedMediaFile(url2).resolve()
		xbmc.Player ().play(stream_url)
		addLink("Press Back to exit",url,'',icon,fanart)		

  
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

elif mode==3: SEARCH()

elif mode==1: GETMOVIES(url,name)
elif mode==10: GETSEARCH(url,name)
elif mode==2: GETLINKSNEW(url,name,iconimage)
elif mode==5: GENRES()

elif mode==101: PLAYMOVIE(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

