import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse
from t0mm0.common.addon import Addon
from metahandler import metahandlers
from resources.lib.libraries import cloudflare
# from BeautifulSoup import BeautifulSoup as bs


addon_id = 'plugin.video.italiaserie'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
ADDON2=xbmcaddon.Addon(id='plugin.video.italiaserie')
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
metaset = selfAddon.getSetting('enable_meta')
base = 'http://www.italiaserie.com'
def CATEGORIES():
		addDir2('[COLOR yellow]Search >>>[/COLOR]','http://www.italiaserie.com/?s=',3,icon,'',fanart)
		addDir2('[COLOR gold]ITALIASERIE.co[/COLOR]','http://www.italiaserie.co/genere/serie-tv/',6,icon,'',fanart)
		addDir2('[COLOR lime]ITALIAFILM.co[/COLOR]','http://www.italia-film.co/category/telefilm/page/1/',2,icon,'',fanart)
		addDir2('[COLOR orange]FILMPERTUTTI.click[/COLOR]','http://www.filmpertutti.click/category/serie-tv/page/1/',13,icon,'',fanart)
		addDir2('[COLOR aqua]ITALIASERIE.com[/COLOR]','http://www.italiaserie.com/category/serie-tv/',6,icon,'',fanart)
		addDir2('[COLOR purple]EUROSTREAMING.tv[/COLOR]','http://eurostreaming.tv/category/serie-tv-archive/page/1/',7,icon,'',fanart)
		addDir2('[COLOR pink]Pellicoliamo.tv[/COLOR] Big List','http://pellicoliamo.tv/serie-tv/',15,icon,'',fanart)


def GETTANTIFILM(url,name):
	# try:
			
			# basepage=url.split('/page/')
			# pagenum=basepage[1]
			# pagenum=pagenum.split('/')
			# curpage = int(pagenum[0])
			# nextpage = curpage + 1
			# nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	# except:pass
	try:
			
			link = open_url(url)

	except:
            dialog = xbmcgui.Dialog()
            dialog.ok("[COLOR lime][B]Cloudflare[/B][/COLOR]", "Blocco attivo sul sito, sara usata la versione mobile", "")
            link = cloudflare.request(url, mobile=True)        
	
	# soup=bs(html)
	# tag=soup.find('div',{'class':'home'})
	
	# reg=re.compile('<a href="(.+?)".+?>(.+?) S(\d+)E(\d+)</a>')
	# episodes=re.findall(reg,str(tag))
	
        metaset = selfAddon.getSetting('enable_meta')
      
        match = re.compile('<li><a href="(.+?)"><strong>(.+?)</strong></a></li>').findall(link)
        for url,name in match:
                        
                        name=re.sub('Permalink to','', name)
                        name=re.sub('streaming','', name)
                        name=re.sub('&#8211;', '', name)
                        name=re.sub('&#8217;','', name)
                        addDir2(name,url,16,icon,'',icon)
                
        try:
               
               
                addDir2('[COLOR yellow]Next Page >>[/COLOR]',nextpageurl,15,icon,'',icon)
        except: pass		
def GETLINKTANTIFILM(url,name):
	metaset = selfAddon.getSetting('enable_meta')
	try:link = open_url(url)
	except:	link = cloudflare.request(url, mobile=True)        

        # match=re.compile('<p>(.+?) <a href="(.+?)" target="_blank" rel="nofollow">').findall(link)
        # match2=re.compile('.+?>(.+?)\s*<a href="(.+?)" target="_blank" rel="nofollow">').findall(link)      
	match=re.compile('<.+?>(.+?)<a href="(.+?)" target=".+?">').findall(link) 
	match2=re.compile('</.+?>(.+?)<a href="(.+?)" target="_blank">').findall(link)
	match3=re.compile('<.+?>(.+?) <a href="(.+?)" rel="nofollow" target="_blank">').findall(link)	
	
        for name,url in  match + match2:
                        
                
                        name=re.sub('<p>','', name)
                        name=re.sub('&#215;','x', name)
                        name=re.sub('</a>','', name)
                        name=re.sub('&#8211;','', name)
                        name=re.sub('&#8217;','', name)
                        name=re.sub('<strong>','', name)
                        name=re.sub('</strong>','', name)
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name + '  (' +  host  + ')   ...  Play  >>>',url,11,icon,'',fanart)	
def GETFILMPERTUTTI(url,name):
	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			curpage = int(pagenum[0])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
	try:
			
			link = open_url(url)

	except:
            dialog = xbmcgui.Dialog()
            dialog.ok("[COLOR lime][B]Cloudflare[/B][/COLOR]", "Blocco attivo sul sito, sara usata la versione mobile", "")
            link = cloudflare.request(url, mobile=True)        

        
        
        metaset = selfAddon.getSetting('enable_meta')
      
        match = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(link)
        match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(link)
        for url,name,img in match + match1:
                        
                        name=re.sub('Streaming','', name)
                        name=re.sub('Link to','', name)
                        name=re.sub('&#8211;', '', name)
                        name=re.sub('&#8217;','', name)
                        addDir2(name,url,14,img,'',img)
                
        try:
               
               
                addDir2('[COLOR yellow]Next Page >>[/COLOR]',nextpageurl,13,img,'',img)
        except: pass
def GETLINKFILMPERTUTTI(url,name):
	metaset = selfAddon.getSetting('enable_meta')
	try:link = open_url(url)
	except:	link = cloudflare.request(url, mobile=True)        

        # match=re.compile('<p>(.+?) <a href="(.+?)" target="_blank" rel="nofollow">').findall(link)
        # match2=re.compile('.+?>(.+?)\s*<a href="(.+?)" target="_blank" rel="nofollow">').findall(link)      
	match=re.compile('.+?>(.+?)<a href="(.+?)" target="_blank" rel="nofollow">').findall(link) 
	match2=re.compile('<.+?>(.+?)<a href="(.+?)" target="_blank" rel="nofollow">').findall(link)
	match3=re.compile('<.+?>\s*(.+?)<a href="(.+?)" target="_blank" rel="nofollow">').findall(link)	
	
        for name,url in  match3:
                        
                
                        name=re.sub('<p>','', name)
                        name=re.sub('&#215;','x', name)
                        name=re.sub('</a>','', name)
                        name=re.sub('&#8211;','', name)
                        name=re.sub('&#8217;','', name)
                       
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name + '  (' +  host  + ')   ...  Play  >>>',url,11,icon,'',fanart)		
def GETITALIAFILMCO(url,name):
	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			curpage = int(pagenum[0])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
	try:
			
			link = open_url(url)

	except:
            dialog = xbmcgui.Dialog()
            dialog.ok("[COLOR lime][B]Cloudflare[/B][/COLOR]", "Blocco attivo sul sito, sara usata la versione mobile", "")
            link = cloudflare.request(url, mobile=True)        

        
        
        metaset = selfAddon.getSetting('enable_meta')
      
        match=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img src="(.+?)"').findall(link)[:12]
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(link)[:12]
        for url,name,img in match + match1:
                        img = "http:" + img
                        name=re.sub('Streaming','', name)
                        name=re.sub('-','', name)
                        name=re.sub('[!@#$-]', '', name)
                        name=re.sub('&#8217;','', name)
						
                        addDir2(name,url,4,img,'',img)
                
        try:
               
               
                addDir2('[COLOR yellow]Next Page >>[/COLOR]',nextpageurl,2,img,'',img)
        except: pass
		
def GETLINKITALIAFILMCO(url,name):
	metaset = selfAddon.getSetting('enable_meta')
	try:link = open_url(url)
	except:	link = cloudflare.request(url, mobile=True)        

        # match=re.compile('<p>(.+?) <a href="(.+?)" target="_blank" rel="nofollow">').findall(link)
        # match2=re.compile('.+?>(.+?)\s*<a href="(.+?)" target="_blank" rel="nofollow">').findall(link)      
	match=re.compile('<.+?>\s*(.+?)<a href="(.+?)" target="_blank">').findall(link) 
	match2=re.compile('<.+?>(.+?)<a href="(.+?)" target="_blank">').findall(link)	
        for name,url in match:
                        
                
                        name=re.sub('<p>','', name)
                        name=re.sub('&#215;','x', name)
                        name=re.sub('</a>','', name)
                        name=re.sub('&#8211;','', name)
                        name=re.sub('&#8217;','', name)
                        name = urllib2.unquote(name)
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name + '  (' +  host  + ')   ...  Play  >>>',url,11,icon,'',fanart)
                
	
def GETEUROSTR(url,name):
	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			curpage = int(pagenum[0])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
	try:
			
			link = open_url(url)

	except:
            dialog = xbmcgui.Dialog()
            dialog.ok("[COLOR lime][B]Cloudflare[/B][/COLOR]", "Blocco attivo sul sito, sara usata la versione mobile", "")
            link = cloudflare.request(url, mobile=True)        

        
        metaset = selfAddon.getSetting('enable_meta')

        
        match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(link)[:18]
		
        for url,name,img in match:
                        # name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('SubITA','', name)
                        name=re.sub('Just another WordPress site','', name)
                        addDir2(name,url,12,img,'',img)
                
        try:
               

                addDir2('[COLOR yellow]Next Page >>[/COLOR]',nextpageurl,6,icon,'',fanart)
        except: pass		
def GETITALIAFIM(url,name):
	try:
			
			basepage=url.split('/page/')
			pagenum=basepage[1]
			pagenum=pagenum.split('/')
			curpage = int(pagenum[0])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'/page/'+str(nextpage)+'/'
	except:pass
	try:
			
			link = open_url(url)

	except:
            dialog = xbmcgui.Dialog()
            dialog.ok("[COLOR lime][B]Cloudflare[/B][/COLOR]", "Blocco attivo sul sito, sara usata la versione mobile", "")
            link = cloudflare.request(url, mobile=True)        

        
        
        metaset = selfAddon.getSetting('enable_meta')
      
        match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(link)
		
        for url,name,img in match:
                        # name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('SubITA','', name)
                        name=re.sub('Just another WordPress site','', name)
                        addDir2(name,url,10,img,'',img)
                
        try:
               
                match=re.compile('<a class="next page-numbers" href="(.+?)">').findall(link)
                
                url= match[0]
                addDir2('[COLOR yellow]Next Page >>[/COLOR]',url,6,icon,'',fanart)
        except: pass

def GETLINKEUROSTR(url,name):
        
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        if 'category/serials/' in url: metaset='false'
        match=re.compile('>\s*(.+?)<a href="(.+?)" target="_blank">.+?</a>').findall(link)
		
        for name,url in match:
             if "eurostreaming.tv" not in url:           
                
                        name=re.sub('<p>','', name)
                        name=re.sub('&#215;','x', name)
                        name=re.sub('</a>','', name)
                        name=re.sub('&#8211;','', name)
                        name=re.sub('</strong>',' ', name)
                        name=re.sub('<strong>',' ', name)
                        name=re.sub('-',' ', name)
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name + host + '   ...',url,11,icon,'',fanart)
						
def GETLINK(url,name):
	metaset = selfAddon.getSetting('enable_meta')
	try:link = open_url(url)
	except:	link = cloudflare.request(url, mobile=True)        

        # match=re.compile('<p>(.+?) <a href="(.+?)" target="_blank" rel="nofollow">').findall(link)
        # match2=re.compile('.+?>(.+?)\s*<a href="(.+?)" target="_blank" rel="nofollow">').findall(link)      
	match3=re.compile('\s*(.+?)\s*<a href="(.+?)" target="_blank" rel="nofollow">').findall(link) 
		
        for name,url in match3:
                        
                
                        name=re.sub('<p>','', name)
                        name=re.sub('&#215;','x', name)
                        name=re.sub('</a>','', name)
                        name=re.sub('&#8211;','', name)
                        name = urllib2.unquote(name)
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name + '  (' +  host  + ')   ...  Play  >>>',url,11,icon,'',fanart)
                
	
def PLAYLINKMOVIEWATCHER(name,url,iconimage):
    try:
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        # stream_url=urlresolver.resolve(url)
        # ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url, liz)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Playback non riuscito ![/B][/COLOR],[COLOR lime][B] Prova un altro link !![/B][/COLOR],7000,"")")


def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))


def SEARCHMOVIES():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Cerca Serie TV')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
      try:
			url = 'http://www.italiaserie.co/?s='+ search_entered
			try:link = open_url(url)
			except:	link = cloudflare.request(url, mobile=True)     
			match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(link)
		
			for url,name,img in match:
							# name=cleanHex(name)
					
							name=re.sub('Streaming','', name)
							name=re.sub('SubITA','', name)
							name=re.sub('Just another WordPress site','', name)
							addDir2(name + "  ... Italiaserie.co",url,10,img,'',img)
      except:pass

      try:
        url = 'http://www.italia-film.co/?s='+ search_entered
        try:link = open_url(url)
        except:	link = cloudflare.request(url, mobile=True)   
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img src="(.+?)"').findall(link)[:12]
        match1=re.compile('<a href="(.+?)" title="(.+?)" class=".+?"><img pagespeed_lazy_src="(.+?)"').findall(link)[:12]
        for url,name,img in match + match1:
                        img = "http:" + img
                        name=re.sub('Streaming','', name)
                        name=re.sub('-','', name)
                        name=re.sub('[!@#$-]', '', name)
                        name=re.sub('&#8217;','', name)
						
                        addDir2(name + "   ...   Italia-film.co   ",url,4,img,'',img)
      except:pass	  
      try:
        url = 'http://www.filmpertutti.click/?s='+ search_entered
        link = open_url(url)
        if 'category/serials/' in url: metaset='false'
        match = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(link)
        match1 = re.compile('<a href="(.+?)" rel=".+?" title="(.+?)" target="">\s*?<span class="hdbox">HD</span>\s*?<img width=".+?" height=".+?" src="(.+?)"').findall(link)
        for url,name,img in match + match1:
                        
                        name=re.sub('Streaming','', name)
                        name=re.sub('Link to','', name)
                        name=re.sub('&#8211;', '', name)
                        name=re.sub('&#8217;','', name)
                        addDir2(name + "  ... Filmpertutti.click",url,14,img,'',img)
      except:pass
      try:
        url = 'http://eurostreaming.tv/?s='+ search_entered
        link = open_url(url)
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(link)[:18]
		
        for url,name,img in match:
                        # name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('SubITA','', name)
                        name=re.sub('Just another WordPress site','', name)
                        addDir2(name + "  ... Eurostreaming.tv",url,12,img,'',img)
      except:pass
      try:
        url = 'http://www.italiaserie.com/?s='+ search_entered
        try:link = open_url(url)
        except:	link = cloudflare.request(url, mobile=True)   
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(link)
		
        for url,name,img in match:
                        # name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('SubITA','', name)
                       
                        addDir2(name + "  ... Italiaserie.com",url,10,img,'',img)
      except:pass
      try:
        url = 'http://www.pellicoliamo.tv/?s='+ search_entered
        try:link = open_url(url)
        except:	link = cloudflare.request(url, mobile=True)   
        if 'category/serials/' in url: metaset='false'
        match=re.compile('<div class="post-thumb">\s*<a href="(.+?)" title="(.+?)">').findall(link)[:5]
		
        for url,name in match:
                        
                        name=re.sub('Permalink to','', name)
                        name=re.sub('streaming','', name)
                        name=re.sub('&#8211;', '', name)
                        name=re.sub('&#8217;','', name)
                        addDir2(name + "   ...   Pellicoliamo.tv",url,16,icon,'',icon)
      except:pass	  	  
	  

	  

		
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
def open_url2(url):
    req = urllib2.Request(url)
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
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
elif mode==4: GETLINKITALIAFILMCO(url,name)
elif mode==2: GETITALIAFILMCO(url,name)
elif mode==6: GETITALIAFIM(url,name)
elif mode==7: GETEUROSTR(url,name)
elif mode==3: SEARCHMOVIES()
elif mode==10: GETLINK(url,name)
elif mode==11: PLAYLINKMOVIEWATCHER(name,url,iconimage)
elif mode==12: GETLINKEUROSTR(url,name)
elif mode==13: GETFILMPERTUTTI(url,name)
elif mode==14: GETLINKFILMPERTUTTI(url,name)
elif mode==15: GETTANTIFILM(url,name)
elif mode==16: GETLINKTANTIFILM(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

