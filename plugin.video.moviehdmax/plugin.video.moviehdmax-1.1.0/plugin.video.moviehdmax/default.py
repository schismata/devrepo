import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,random
from t0mm0.common.addon import Addon
from metahandler import metahandlers

from resources.lib.libraries import client
from resources.lib.resolvers import googleplus

addon_id = 'plugin.video.moviehdmax'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
icon2 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/freefullmovies.png'))
icon3 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/moviesmaze.png'))
icon4 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/moviewatcher.png'))
icon5 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/movieshdmax.png'))
icon6 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/onlinemovies.png'))
icon7 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/xmovies8.png'))
icon8 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/imdb.png'))
icon9 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/movies2k.png'))
metaset = selfAddon.getSetting('enable_meta')
addon = Addon(addon_id, sys.argv)

def CATEGORIES():
        addDir2('[COLOR red]>>> Search Movies <<<[/COLOR]','http://moviehdmax.com/',3,icon,fanart)
        addDir2('[COLOR red]>>> Search TV <<<[/COLOR]','http://moviehdmax.com/',30,icon,fanart)
        addDir2('[COLOR lime]>>> Movies <<<[/COLOR]','http://moviesmaze.org/',40,icon,fanart) 


        addDir2('[COLOR gold]Latest TV Episodes[/COLOR]','http://fulltvepisodes.net/series-index/',11,icon,fanart)
        addDir2('[COLOR gold]Onlinemovies.is Latest Episodes[/COLOR]','http://onlinemovies.is/watch/category/tv-episodes/page/1/',21,icon6,'',fanart)
        addDir2('[COLOR gold]Series Craving[/COLOR]','http://series-cravings.me/tv-show-2',32,icon6,'',fanart)	

def MOVIESINDEX():
        
        addDir2('[COLOR gold](TMDB) Popular Movies[/COLOR]','https://www.themoviedb.org/movie?page=1',35,icon8,fanart)
        addDir2('[COLOR gold](TMDB) Top Rated[/COLOR]','https://www.themoviedb.org/movie/top-rated?page=1',35,icon8,fanart)
        addDir2('[COLOR gold](TMDB) Now Playing[/COLOR]','https://www.themoviedb.org/movie/now-playing?page=1',35,icon8,fanart)
        # addDir2('[COLOR lime]AFDAH-XMOVIES8[/COLOR]','http://moviehdmax.com/',37,icon,fanart)
        addDir2('(HD)[COLOR yellow]MOVIEHDMAX[/COLOR]','http://moviehdmax.com/',5,icon5,fanart)
        addDir2('(HD)[COLOR aqua]XMOVIES8[/COLOR]','http://xmovies8.tv/cinema-movies/page/1',24,icon7,fanart)
        addDir2('(HD)[COLOR orange]FREE FULL MOVIES[/COLOR]','http://www.freefullmovies.net/mp4',6,icon2,fanart)
        addDir2('(HD)[COLOR green]ONLINEMOVIES.IS[/COLOR]','http://onlinemovies.is/',20,icon6,fanart)
        addDir2('[COLOR cyan]HDMOVIE-14[/COLOR]','http://hdmovie-14.com/category/hdmovie14-online-free/',23,icon6,fanart)
        addDir2('[COLOR teal]Movie2k Latest Movies[/COLOR]','http://movies2k.eu//category/hollywood-movies/',39,icon9,fanart)
        addDir2('[COLOR teal]Movie2k Featured[/COLOR]','http://onlinefreemovie.eu/category/featured/',39,icon9,fanart)
		
        addDir2('[COLOR red]MOVIESMAZE[/COLOR]','http://moviesmaze.org/',9,icon3,fanart)
        addDir2('[COLOR teal]MOVIEWATCHER[/COLOR]','http://moviehdmax.com/',19,icon4,fanart)
        addDir2('MOVIESMAZE (year 2015)','http://moviesmaze.org/category/2015-movies/',9,icon3,fanart)
		
def ONLINEMOVIESIS():
        
        addDir2('Latest Cinema Releases','http://onlinemovies.is/watch/category/cinema-movies/page/1/',21,icon6,'',fanart)
        addDir2('2015','http://onlinemovies.is/watch/category/year/2015/page/1/',21,icon6,'',fanart)
        addDir2('HD Movies','http://onlinemovies.is/watch/category/hd-movies/page/1/',21,icon6,'',fanart)
        addDir2('Action','http://onlinemovies.is/watch/category/genre/action/page/1/',21,icon6,'',fanart)
        addDir2('Adventure','http://onlinemovies.is/watch/category/genre/adventure/page/1/',21,icon6,'',fanart)
        addDir2('Animation','http://onlinemovies.is/watch/category/genre/animation/page/1/',21,icon6,'',fanart)
        addDir2('Biography','http://onlinemovies.is/watch/category/genre/biography/page/1/',21,icon6,'',fanart)
        addDir2('Comedy','http://onlinemovies.is/watch/category/genre/comedy/page/1/',21,icon6,'',fanart)
        addDir2('Crime','http://onlinemovies.is/watch/category/genre/crime/page/1/',21,icon6,'',fanart)
        addDir2('History','http://onlinemovies.is/watch/category/genre/history/page/1/',21,icon6,'',fanart)
        addDir2('Horror','http://onlinemovies.is/watch/category/genre/horror/page/1/',21,icon6,'',fanart)
        addDir2('Music','http://onlinemovies.is/watch/category/genre/music/page/1/',21,icon6,'',fanart)
        addDir2('Musical','http://onlinemovies.is/watch/category/genre/musical/page/1/',21,icon6,'',fanart)
        addDir2('Mystery','http://onlinemovies.is/watch/category/genre/mystery/page/1/',21,icon6,'',fanart)
        addDir2('Romance','http://onlinemovies.is/watch/category/genre/romance/page/1/',21,icon6,'',fanart)
        addDir2('SciFi','http://onlinemovies.is/watch/category/genre/science-fiction/page/1/',21,icon6,'',fanart)
        addDir2('Sports','http://onlinemovies.is/watch/category/genre/sports/page/1/',21,icon6,'',fanart)
        addDir2('Thriller','http://onlinemovies.is/watch/category/genre/thriller/page/1/',21,icon6,'',fanart)
        addDir2('War','http://onlinemovies.is/watch/category/genre/war/page/1/',21,icon6,'',fanart)
        addDir2('Western','http://onlinemovies.is/watch/category/genre/western/page/1/',21,icon6,'',fanart)

		
		
def MOVIEWATCHER():
        
        addDir2('Most Popular','http://moviewatcher.to/most-popular-movies.html',17,icon4,fanart)
        addDir2('New Movies','http://moviewatcher.to/new-published-movies.html',17,icon4,fanart)

		
        addDir2('Action','http://moviewatcher.to/genres/action',16,icon4,fanart)
        addDir2('Crime','http://moviewatcher.to/genres/crime',16,icon4,fanart)
        addDir2('Romance','http://moviewatcher.to/genres/romance',16,icon4,fanart)
        addDir2('Biography','http://moviewatcher.to/genres/biography',16,icon4,fanart)
        addDir2('Sci-Fi','http://moviewatcher.to/genres/sci-fi',16,icon4,fanart)
        addDir2('Documentary','http://moviewatcher.to/genres/documentary',16,icon4,fanart)
        addDir2('Drama','http://moviewatcher.to/genres/drama',16,icon4,fanart)
        addDir2('Comedy','http://moviewatcher.to/genres/family',16,icon4,fanart)
        addDir2('Fantasy','http://moviewatcher.to/genres/fantasy',16,icon4,fanart)
        addDir2('History','http://moviewatcher.to/genres/history',16,icon4,fanart)
        addDir2('Horror','http://moviewatcher.to/genres/horror',16,icon4,fanart)
        addDir2('Adventure','http://moviewatcher.to/genres/adventure',16,icon4,fanart)
        addDir2('Mystery','http://moviewatcher.to/genres/mystery',16,icon4,fanart)
        addDir2('Animation','http://moviewatcher.to/genres/animation',16,icon4,fanart)
        addDir2('Family','http://moviewatcher.to/genres/family',16,icon4,fanart)
        addDir2('Sport','http://moviewatcher.to/genres/sport',16,icon4,fanart)
        addDir2('Music','http://moviewatcher.to/genres/music',16,icon4,fanart)
        addDir2('Game-show','http://moviewatcher.to/genres/game-show',16,icon4,fanart)
        addDir2('Thriller','http://moviewatcher.to/genres/thriller',16,icon4,fanart)
        addDir2('War','http://moviewatcher.to/genres/war',16,icon4,fanart)
        addDir2('Western','http://moviewatcher.to/genres/western',16,icon4,fanart)
		
def MOVIEHDMAX():
        addDir2('> Latest Movies','http://moviehdmax.com/',111,icon5,fanart)
        addDir2('Action','http://moviehdmax.com/search/genre/action?page=1#genre',1,icon5,fanart)
        addDir2('Crime','http://moviehdmax.com/search/genre/crime?page=1#genre',1,icon5,fanart)
        addDir2('Romance','http://moviehdmax.com/search/genre/romance?page=1#genre',1,icon5,fanart)
        addDir2('Biography','http://moviehdmax.com/search/genre/biography?page=1#genre',1,icon5,fanart)
        addDir2('Sci-Fi','http://moviehdmax.com/search/genre/sci-fi?page=1#genre',1,icon5,fanart)
        addDir2('Documentary','http://moviehdmax.com/search/genre/documentary?page=1#genre',1,icon5,fanart)
        addDir2('Drama','http://moviehdmax.com/search/genre/drama?page=1#genre',1,icon5,fanart)
        addDir2('Comedy','http://moviehdmax.com/search/genre/comedy?page=1#genre',1,icon5,fanart)
        addDir2('Fantasy','http://moviehdmax.com/search/genre/fantasy?page=1#genre',1,icon5,fanart)
        addDir2('History','http://moviehdmax.com/search/genre/history?page=1#genre',1,icon5,fanart)
        addDir2('Horror','http://moviehdmax.com/search/genre/horror?page=1#genre',1,icon5,fanart)
        addDir2('Adventure','http://moviehdmax.com/search/genre/adventure?page=1#genre',1,icon5,fanart)
        addDir2('Mystery','http://moviehdmax.com/search/genre/mystery?page=1#genre',1,icon5,fanart)
        addDir2('Animation','http://moviehdmax.com/search/genre/animation?page=1#genre',1,icon5,fanart)
        addDir2('Family','http://moviehdmax.com/search/genre/family?page=1#genre',1,icon5,fanart)
        addDir2('Sport','http://moviehdmax.com/search/genre/sport?page=1#genre',1,icon5,fanart)
        addDir2('Music','http://moviehdmax.com/search/genre/music?page=1#genre',1,icon5,fanart)
        addDir2('Game-show','http://moviehdmax.com/search/genre/game-show?page=1#genre',1,icon5,fanart)
        addDir2('Thriller','http://moviehdmax.com/search/genre/thriller?page=1#genre',1,icon5,fanart)
        addDir2('War','http://moviehdmax.com/search/genre/war?page=1#genre',1,icon5,fanart)
        addDir2('Western','http://moviehdmax.com/search/genre/western?page=1#genre',1,icon5,fanart)
        
def AFDAH():
        addDir2('Popular Movies','https://xmovies8.org/popular_movies?page=1',38,icon5,fanart)
        addDir2('Latest Movies','https://xmovies8.org/latest_movies?page=1',38,icon5,fanart)
        addDir2('Most Watched','https://xmovies8.org/most_watched_movies?page=1',38,icon5,fanart)

def FREEFULLMOVIES():
        addDir2('ALL','http://www.freefullmovies.net/mp4',7,icon2,fanart)
        addDir2('Latest Movies','http://www.freefullmovies.net/watchmovies',7,icon2,fanart)
        addDir2('Most Popular','http://www.freefullmovies.net/most-popular.html',7,icon2,fanart)

		
        addDir2('YEAR: 2016','http://www.freefullmovies.net/2016.html',7,icon2,fanart)
        addDir2('YEAR: 2015','http://www.freefullmovies.net/2015.html',7,icon2,fanart)

        addDir2('0-9','http://www.freefullmovies.net/0-9.html',7,icon2,fanart)
        addDir2('A','http://www.freefullmovies.net/a.html',7,icon2,fanart)
        addDir2('B','http://www.freefullmovies.net/b.html',7,icon2,fanart)
        addDir2('C','http://www.freefullmovies.net/c.html',7,icon2,fanart)
        addDir2('D','http://www.freefullmovies.net/d.html',7,icon2,fanart)
        addDir2('E','http://www.freefullmovies.net/e.html',7,icon2,fanart)
        addDir2('F','http://www.freefullmovies.net/f.html',7,icon2,fanart)
        addDir2('G','http://www.freefullmovies.net/g.html',7,icon2,fanart)
        addDir2('H','http://www.freefullmovies.net/h.html',7,icon2,fanart)
        addDir2('I','http://www.freefullmovies.net/i.html',7,icon2,fanart)
        addDir2('J','http://www.freefullmovies.net/j.html',7,icon2,fanart)
        addDir2('K','http://www.freefullmovies.net/k.html',7,icon2,fanart)
        addDir2('L','http://www.freefullmovies.net/l.html',7,icon2,fanart)
        addDir2('M','http://www.freefullmovies.net/m.html',7,icon2,fanart)
        addDir2('N','http://www.freefullmovies.net/n.html',7,icon2,fanart)
        addDir2('O','http://www.freefullmovies.net/o.html',7,icon2,fanart)
        addDir2('P','http://www.freefullmovies.net/p.html',7,icon2,fanart)
        addDir2('Q','http://www.freefullmovies.net/q.html',7,icon2,fanart)
        addDir2('R','http://www.freefullmovies.net/r.html',7,icon2,fanart)
        addDir2('S','http://www.freefullmovies.net/s.html',7,icon2,fanart)
        addDir2('T','http://www.freefullmovies.net/t.html',7,icon2,fanart)
        addDir2('U','http://www.freefullmovies.net/u.html',7,icon2,fanart) 		
        addDir2('V','http://www.freefullmovies.net/v.html',7,icon2,fanart) 		
        addDir2('W','http://www.freefullmovies.net/w.html',7,icon2,fanart) 		
        addDir2('X','http://www.freefullmovies.net/x.html',7,icon2,fanart) 		
        addDir2('Y','http://www.freefullmovies.net/y.html',7,icon2,fanart) 		
        addDir2('Z','http://www.freefullmovies.net/z.html',7,icon2,fanart) 		


def PLAYLINKAFDAH(name,url,iconimage):
        link = open_url(url)
        base_link_1 = 'https://afdah.org'
        base_link_2 = 'https://xmovies8.org'
        search_link = '/results?q=%s'
        info_link = '/video_info'
        base_link = random.choice([base_link_1, base_link_2])
        url = urlparse.urljoin(base_link, url)

        result = client.source(url)

        video_id = re.compile('video_id *= *[\'|\"](.+?)[\'|\"]').findall(result)[0]
        post = urllib.urlencode({'video_id': video_id})

        result = client.source(urlparse.urljoin(base_link, info_link), post=post)

        u = [i for i in result.split('&') if 'google' in i][0]
        u = urllib.unquote_plus(u)
        u = [urllib.unquote_plus(i.split('|')[-1]) for i in u.split(',')]
        u = [googleplus.tag(i)[0] for i in u]
        u = [i for i in u if i['quality'] in ['1080p', 'HD']]
        for i in u:
		addLink(i['quality'],i['url'],101,iconimage,fanart)
def GETMOVIES2K(url,name):
        base_link_2 = 'https://xmovies8.org'
	try:
			
			basepage=url.split('?page=')
			
			curpage = int(basepage[1])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'?page='+str(nextpage)
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match = re.compile('<h1 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h1>.+?src="(.+?)"', re.DOTALL).findall(link)
        for url,name,img in match:
                name=cleanHex(name)
				
                name=re.sub('Watch','',name)
                name=re.sub('DVDRip','',name)
                name=re.sub('Online Free','',name)
                
                if metaset=='false':
                        try:
                                addDir(name,url,31,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,31,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,39,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)') 
def GETMOVIESAFDAH(url,name):
        base_link_2 = 'https://xmovies8.org'
	try:
			
			basepage=url.split('?page=')
			
			curpage = int(basepage[1])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'?page='+str(nextpage)
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for name,url in match:
                name=cleanHex(name)
				
                name=re.sub('Full Movie','',name)
                name=re.sub('HD 1080p','',name)
                name=re.sub('-','',name)
                url= base_link_2 + url
                if metaset=='false':
                        try:
                                addDir(name,url,105,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,105,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,38,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)') 
		
def GETMOVIESDB(url,name):
	try:
			
			basepage=url.split('?page=')
			
			curpage = int(basepage[1])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'?page='+str(nextpage)
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a id=".+?" class=".+?" href="(.+?)" title="(.+?)" alt=".+?">.+?</a>\s*<span class=".+?">').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,36,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,36,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,35,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')
def GETLINKSDB(url,name,iconimage):
     # link = open_url(url)

    search_entered = name
    keyboard = xbmc.Keyboard(search_entered, 'Search Movies')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://moviehdmax.com/search/result?s=' + search_entered + '&selected=false'
        link = open_url(url)
        match=re.compile('<p class=".+?">\s*<a href="../(.+?)">(.+?)</a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
                name=re.sub('Genres','',name)
                name=re.sub('Contacts','',name)
                name=re.sub('Full TV Series','',name)
                name=re.sub('<strong>','',name)
                name=re.sub('</strong>','',name)
                name=re.sub('<span>','',name)
                name=re.sub('</span>','',name)

                url= 'http://moviehdmax.com/' + url
                addLink(name + '... [COLOR yellow]MoviesHDMax[/COLOR]',url,2,iconimage,fanart)
     except: pass
     try:
    	url = 'https://xmovies8.org/results?q=' + search_entered
        link = open_url(url)
        match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        for name,url in match:
                name=cleanHex(name)

                url= 'https://xmovies8.org' + url
                addLink(name + '... [COLOR lime]AFDAH-XMOVIES8[/COLOR]',url,105,iconimage,fanart)
     except: pass

     try:
			url = 'http://xmovies8.tv/?s=' + search_entered
		        link = open_url(url)
			match=re.compile('<a href="(.+?)"><img width=".+?" height=".+?" alt=".+?" title="(.+?)"').findall(link)
			if len(match)>0:
					items = len(match)
					for url,name in match:
							name2 = name.encode('ascii', 'ignore')
							if not 'SEASON' in name2:
								 if not 'Season' in name2:
									if not 'nofollow' in name2:
											 addLink(name2 + '... [COLOR aqua]Xmovies8[/COLOR]',url,104,iconimage,fanart)
               
     except: pass
	 
     try:
       url = 'http://www.warezmovies.info/?s=' + search_entered
       link = open_url(url)
       match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(link)
       for url,name,img in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Warez[/COLOR]',url,28,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Warezmovies  is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
	 
	 
	 
	 
     try:
    	url = 'http://moviesmaze.org/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                if metaset=='false':
                        try:
                                addDir2(name,url,10,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir(name + ' ... Moviesmaze.org',url,10,icon,len(match),isFolder=True)
                        except:pass
     except: pass
     try:
        url = 'http://world4ufree.com/?s=' +search_entered 
        link = open_url(url)
        
        match = re.compile('<div class="cover"><a href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+? class=.+? width=.+? height=.+? /></a></div>', re.DOTALL).findall(link)[:5]
        for url,name,img in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                if metaset=='false':
                        try:
                                addDir(name+' ... World4ufree.com',url,15,img,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+' >>>(World4uFree)',url,15,img,len(match),isFolder=True)
                        except:pass
     except: pass	 
    try:
        url = 'http://300mbmovies4u.com/?s=' +search_entered 
        link = open_url(url)
        
        
        match = re.compile('<li>\s*?<h2><a href="(.+?)" title=".+?">(.+?)</a></h2>\s*?<div class=".+?"><a href=".+?" title=".+?"><img src="(.+?)"', re.DOTALL).findall(link)[:10]
        for url, name, img in match:
                addDir(name+' ... 300mbMovies4u',url,15,img,len(match),isFolder=True)
    except: pass

    try:
    	url = 'http://moviewatcher.to/search?q='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" class="video_inner">\s*<span class=".+?" data-toggle=".+?" title=".+?" data-placement=".+?" data-container="body">\s*.+?\s*</span>\s*<div class="img_holder">\s*<img src="(.+?)" width=".+?" height=".+?" alt="(.+?)">').findall(link)
        for url,img,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                url= 'http://moviewatcher.to' + url
                if metaset=='false':
                        try:
                                addDir(name+'  ... Moviewatcher',url,18,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+'   ... Moviewatcher',url,18,icon,len(match),isFolder=True)
                        except:pass
     
    except: pass
    try:
    	url = 'http://newonlinemovies.pro/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+'   ... NEWOnlineMOvies',url,22,icon,len(match),isFolder=True)
                        except:pass
    except: pass
    try:
    	url = 'http://hdmovie-14.com/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+' ... Hdmovies14.com',url,22,icon,len(match),isFolder=True)
                        except:pass
    except: pass

    try:
    	url = 'http://movie-32.com/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+' ... Movie-32.com',url,22,icon,len(match),isFolder=True)
                        except:pass
    except: pass
    try:
    	url = 'http://rlssource.net/?s=' + search_entered + '&go=Search'
        link = open_url(url)
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(link)
        for url,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Rlssources[/COLOR]',url,29,iconimage,fanart)
    except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSsources is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

def XMOVIES8():

        addDir2('Cinema Movies','http://xmovies8.tv/cinema-movies/page/1',25,icon7,'',fanart)

        addDir2('New Movies','http://xmovies8.tv/new/page/1',25,icon7,'',fanart)

        addDir2('HD Movies','http://xmovies8.tv/movie-quality/hd/page/1',25,icon7,'',fanart)

        addDir2('Movies By Year','http://xmovies8.tv/',26,icon7,'',fanart)

        addDir2('Movies By Genre','http://xmovies8.tv/',27,icon7,'',fanart)




def GETYEARSXMOVIES(url):

        link = open_url(url)

        link=link.replace('\n','').replace('  ','')

        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)

        for url,name in match:
                url=url+'/page/1'

                if 'category' in url:addDir2(name,url,25,icon,'',fanart)

        xbmc.executebuiltin('Container.SetViewMode(50)')



def GETGENRESXMOVIES(url):
        link = open_url(url)
        link=link.replace('\n','').replace('  ','')
        match=re.compile('<a title="(.+?)" href="(.+?)">').findall(link)
        for name,url in match:
                if 'game-show' in name:name = 'Game Show'
                url=url+'/page/1'
                addDir2(name,url,25,icon,'',fanart)
        xbmc.executebuiltin('Container.SetViewMode(50)')
		
def GETXMOVIES8(url,name):
    try:
        pagenum = url.split('page/')
        curpage = int(pagenum[1])
        nextpage = curpage + 1
        nextpageurl = pagenum[0]+'page/'+str(nextpage)
    except:pass
    link = open_url(url)
    match=re.compile('<a href="(.+?)"><img width=".+?" height=".+?" alt=".+?" title="(.+?)"').findall(link)
    if len(match)>0:
            items = len(match)
            for url,name in match:
                    name2 = name.encode('ascii', 'ignore')
                    if not 'SEASON' in name2:
                         if not 'Season' in name2:
                            if not 'nofollow' in name2:
                                    addDir(name2,url,104,'',len(match))
            try:
                    addDir2('Next >> Page '+str(nextpage),nextpageurl,25,icon,'',fanart)
            except:pass
    if metaset=='true':
            setView('movies', 'MAIN')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')


def PLAYLINKXMOVIES(name,url,iconimage):
        link = open_url(url)
        posturl = re.compile('url: "(.+?)",').findall(link)[0]
        postparams = re.compile("data: '(.+?)',").findall(link)[0]
        req = urllib2.Request(posturl,postparams)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        stream_url = re.compile('<a href="(.+?)" target="_blank" rel="nofollow">.+?</a>').findall(link)[-1]
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=icon,thumbnailImage=icon); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url, liz, False)

def GETSERIESCRAVING(url,name):

        
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a>').findall(link)
        for url,name in match:
                
				
                
                if metaset=='false':
                        try:
                                addDir2(name,url,33,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir2(name,url,33,icon,fanart)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,32,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GETSERIESCRAVING_EP(url,name):
	try:
			actualpage = str(url)
			basepage=actualpage.split('page/')
			actualpage2 = re.sub('/','',actualpage)
			pagenum = actualpage2.split('page')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'page/'+str(nextpage)+'/'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match_season=re.compile('<div class=".+?"><div class=".+?">(.+?)</div><div class=".+?" style=".+?"></p>\s*<ul class=".+?">\s*<li>(.+?)<a href="(.+?)">(.+?)</a></li>').findall(link)
        match=re.compile('<li>(.+?)<a href="(.+?)">(.+?)</a></li>').findall(link)
        for ep,url,name in match:
                name=cleanHex(name)
                ep=re.sub('&#8211;','',ep)
                name=re.sub('&#8211;','',name)
                
                
                if metaset=='false':
                        try:
                                
								   addDir(ep + name,url,34,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
						
                                
                               
								addDir(ep + name,url,34,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,32,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')
		
def GETLINKS_SCRAVING(url,name,iconimage):
        link = open_url(url)
        match = re.compile('href="(.+?)"').findall(link)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(link)
        match2 = re.compile('<IFRAME SRC="(.+?)"').findall(link)
        match3 = re.compile('<iframe src="(.+?)"').findall(link)
        match4 = re.compile('<iframe width=".+?" height=".+?" src="(.+?)"').findall(link)

        for url in match2 + match3 + match4:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,103,iconimage,fanart)       
def GETHDMOVIES14(url,name):
	try:
			actualpage = str(url)
			basepage=actualpage.split('page/')
			actualpage2 = re.sub('/','',actualpage)
			pagenum = actualpage2.split('page')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'page/'+str(nextpage)+'/'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:50]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,21,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GETONLINEMOVIESIS(url,name):
	try:
			actualpage = str(url)
			basepage=actualpage.split('page/')
			actualpage2 = re.sub('/','',actualpage)
			pagenum = actualpage2.split('page')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = basepage[0]+'page/'+str(nextpage)+'/'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
	try:
                    
					
					addLink('NEXT>>',nextpageurl,21,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GETONLINEMOVIESLINKS(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<iframe width=".+?" height=".+?" scrolling=".+?" frameborder=".+?" src="(.+?)" allowFullScreen></iframe>').findall(link)
        match2=re.compile('<iframe src="(.+?)" scrolling=".+?" frameborder=".+?" width=".+?" height=".+?" allowfullscreen=".+?"').findall(link) 
        match3=re.compile('<IFRAME SRC="(.+?)" FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO allowfullscreen=".+?"').findall(link) 
		
        for url in match + match2 + match3:
                
                
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)		
# ---------------------------------------------------- MOVIE WATCHER ---------------------------------------------------------		

def GETMOVIEWATCHER2(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)" class="video_inner">\s*<span class=".+?" data-toggle=".+?" title=".+?" data-placement=".+?" data-container="body">.+?</span>\s*<div class="img_holder">\s*<img width=".+?" height=".+?" alt="(.+?)" src="(.+?)">').findall(link)
        for url,name,img in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                url= 'http://moviewatcher.to' + url
                if metaset=='false':
                        try:
                                addDir(name,url,18,img,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,18,img,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')



def PLAYLINKMOVIEWATCHER(name,url,iconimage):
        name=selfAddon.getSetting('namestore')
        stream_url=urlresolver.resolve(url)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url)
        

def GETMOVIEWATCHER(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<h3><a href="(.+?)">(.+?)</a></h3>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                url= 'http://moviewatcher.to' + url
                if metaset=='false':
                        try:
                                addDir(name,url,18,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name,url,18,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GETLINKSMOVIEWATCHER(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<div class=".+?"> <span class=".+?">.+? </span>(.+?)</div>\s*<div class=".+?"> <span class=".+?">.+? </span>\s*<a href="(.+?)" data-id=".+?" data-type=".+?" rel=".+?" target=".+?"').findall(link)
		
        for name,url in match:
                
                
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink( host + ' - ' + name,url,103,iconimage,fanart)
						
						
						
# ---------- VONLINE MOVIES ----------------------------------------------
def GETLINKVONLINE(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<p>.+? <a href="(.+?)" target=".+?">.+?</a></p>').findall(link)
        for url in match:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)		
# --------------------------------- FULLTV EPISODES -----------------------------		
def GETTV(url,name):
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)">(.+?)</a></div>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                if metaset=='false':
                        try:
                                addDir2(name,url,12,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir2(name,url,12,icon,fanart)
                        except:pass
        else: xbmc.executebuiltin('Container.SetViewMode(50)')
def GETTVEPISODES(url,name):
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                if metaset=='false':
                        try:
                                addDir2(name,url,13,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir2(name,url,13,icon,fanart)
                        except:pass
        else: xbmc.executebuiltin('Container.SetViewMode(50)')	
def GETTVLINKS(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<a target=".+?" rel=".+?" href="(.+?)">.+?</a>').findall(link)
        for url in match:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)	
# -------------------------- MOVIES MAZE --------------------------------------------
def GETMOVIESMAZE(url,name):
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                if metaset=='false':
                        try:
                                addDir2(name,url,10,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir(name,url,10,icon,len(match),isFolder=True)
                        except:pass
	try:
					match=re.compile('<link rel="next" href="(.+?)" />').findall(link)
					url= match[0]
                
					addLink('NEXT >>',url,9,icon,'')
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GETLINKSMAZE(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<td><a rel=".+?" target=".+?" href="(.+?)" target=".+?">.+?</a></td>').findall(link)
        for url in match:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)

def PLAYLINKMAZE(name,url,iconimage):
        name=selfAddon.getSetting('namestore')
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url)
        
# -------------------------- MOVIES MAZE --------------------------------------------
def GETFREEFULLMOVIES(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass

        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<div class="image"><a href="(.+?)" title="(.+?)"><img src="(.+?)"').findall(link)
        for url,name,img in match:
                name=cleanHex(name)
                name=re.sub('Watch','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('movie','',name)
				
                
                if metaset=='false':
                        try:
                                addDir2(name,url,8,img,img)
                        except:pass
                else:
                        try:
                                addDir2(name,url,8,img,img)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,8,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')		
def GETMOVIES(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="../..(.+?)"> <img data-original=".+?" alt="(.+?)" class=".+?">').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                url= 'http://moviehdmax.com' + url
                if metaset=='false':
                        try:
                                addDir2(name,url,2,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')
def GETMOVIESNEW(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        originalpage = open_url(url)
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="(.+?)">(.+?)<span class="hblank">').findall(link)[:30]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
				
                url= 'http://moviehdmax.com/' + url
                if metaset=='false':
                        try:
                                addDir2(name,url,2,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')
def GETSEARCH(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass

        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<p class=".+?">\s*<a href="../(.+?)">(.+?)</a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
                name=re.sub('Genres','',name)
                name=re.sub('Contacts','',name)
                name=re.sub('Full TV Series','',name)
                name=re.sub('<strong>','',name)
                name=re.sub('</strong>','',name)
                name=re.sub('<span>','',name)
                name=re.sub('</span>','',name)

                url= 'http://moviehdmax.com/' + url
                if metaset=='false':
                        try:
                                addDir2(name,url,2,icon,fanart)
                        except:pass
                else:
                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
        if metaset=='true':
                setView('movies', 'MAIN')
        else: xbmc.executebuiltin('Container.SetViewMode(50)')


def GETLINKSFREEFULLMOVIES(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<source src="(.+?)" type="(.+?)"></video>').findall(link)
		
        for url, name in match:
                
                
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name,url,101,iconimage,fanart)

def GETLINKS(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('''<source src="(.+?)" type='.+?' data-res="(.+?)"/>''').findall(link)
		
        for url, name in match:
                
                
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name+'p',url,100,iconimage,fanart)
def PLAYLINKFREEFULLMOVIES(name,url,iconimage):
    
    xbmc.Player().play(url)
    
    addDir2('Press Back to exit','',8,'','')


  # WAREZ
def GETLINKS132(url,name,iconimage):
         link = open_url(url)
         match = re.compile('<a href="(.+?)"').findall(link)
         for url in match:

                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addLink(title,url,102,iconimage,fanart)
					  
	# RLSSOURCE
def GETLINKS10(url,name,iconimage):
        link = open_url(url)
        match = re.compile('href=(.+?) target=_blank').findall(link)
        match1 = re.compile('<iframe src="(.+?)"').findall(link)
        
        for url in match + match1:

                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addLink(title,url,102,iconimage,fanart)
 
 


	
	
	
	
	# ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH -------------------------------------------------------- 
def SEARCH():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search Movies')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://moviehdmax.com/search/result?s=' + search_entered + '&selected=false'
        link = open_url(url)
        match=re.compile('<p class=".+?">\s*<a href="../(.+?)">(.+?)</a>').findall(link)
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                name=re.sub('watch','',name)
                name=re.sub('online','',name)
                name=re.sub('free','',name)
                name=re.sub('putlocker','',name)
                name=re.sub('xmovie8','',name)
                name=re.sub('xmovies8','',name)
                name=re.sub('Genres','',name)
                name=re.sub('Contacts','',name)
                name=re.sub('Full TV Series','',name)
                name=re.sub('<strong>','',name)
                name=re.sub('</strong>','',name)
                name=re.sub('<span>','',name)
                name=re.sub('</span>','',name)

                url= 'http://moviehdmax.com/' + url
                addLink(name + '... [COLOR yellow]MoviesHDMax[/COLOR]',url,2,iconimage,fanart)
     except: pass
     # try:
    	# url = 'https://xmovies8.org/results?q=' + search_entered
        # link = open_url(url)
        # match=re.compile('<a title="(.+?)" href="(.+?)">.+?</a>').findall(link)
        # for name,url in match:
                # name=cleanHex(name)

                # url= 'https://xmovies8.org' + url
                # addLink(name + '... [COLOR lime]AFDAH-XMOVIES8[/COLOR]',url,105,iconimage,fanart)
     # except: pass

     try:
			url = 'http://xmovies8.tv/?s=' + search_entered
		        link = open_url(url)
			match=re.compile('<a href="(.+?)"><img width=".+?" height=".+?" alt=".+?" title="(.+?)"').findall(link)
			if len(match)>0:
					items = len(match)
					for url,name in match:
							name2 = name.encode('ascii', 'ignore')
							if not 'SEASON' in name2:
								 if not 'Season' in name2:
									if not 'nofollow' in name2:
											 addLink(name2 + '... [COLOR aqua]Xmovies8[/COLOR]',url,104,iconimage,fanart)
               
     except: pass
	 
     # try:
       # url = 'http://www.warezmovies.info/?s=' + search_entered
       # link = open_url(url)
       # match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(link)
       # for url,name,img in match:
                # name=cleanHex(name)

                # addLink(name + '... [COLOR lime]Warez[/COLOR]',url,28,iconimage,fanart)
     # except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Warezmovies  is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
	 
	 
	 
	 
     # try:
    	# url = 'http://moviesmaze.org/?s='+search_entered
        # link = open_url(url)
        # match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        # for url,name in match:
                # name=cleanHex(name)
                # name=re.sub('Full Movie Watch Online','',name)
                # if metaset=='false':
                        # try:
                                # addDir2(name,url,10,icon,fanart)
                        # except:pass
                # else:
                        # try:
                                # addDir(name + ' ... Moviesmaze.org',url,10,icon,len(match),isFolder=True)
                        # except:pass
     # except: pass
     try:
        url = 'http://world4ufree.com/?s=' +search_entered 
        link = open_url(url)
        
        match = re.compile('<div class="cover"><a href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+? class=.+? width=.+? height=.+? /></a></div>', re.DOTALL).findall(link)[:5]
        for url,name,img in match:
                name=cleanHex(name)
                name=re.sub('Full Movie Watch Online','',name)
                if metaset=='false':
                        try:
                                addDir(name+' ... World4ufree.com',url,15,img,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+' >>>(World4uFree)',url,15,img,len(match),isFolder=True)
                        except:pass
     except: pass	 
    try:
        url = 'http://300mbmovies4u.com/?s=' +search_entered 
        link = open_url(url)
        
        
        match = re.compile('<li>\s*?<h2><a href="(.+?)" title=".+?">(.+?)</a></h2>\s*?<div class=".+?"><a href=".+?" title=".+?"><img src="(.+?)"', re.DOTALL).findall(link)[:10]
        for url, name, img in match:
                addDir(name+' ... 300mbMovies4u',url,15,img,len(match),isFolder=True)
    except: pass

    # try:
    	# url = 'http://moviewatcher.to/search?q='+search_entered
        # link = open_url(url)
        # match=re.compile('<a href="(.+?)" class="video_inner">\s*<span class=".+?" data-toggle=".+?" title=".+?" data-placement=".+?" data-container="body">\s*.+?\s*</span>\s*<div class="img_holder">\s*<img src="(.+?)" width=".+?" height=".+?" alt="(.+?)">').findall(link)
        # for url,img,name in match:
                # name=cleanHex(name)
                # name=re.sub('Full Movie Watch Online','',name)
                # name=re.sub('watch','',name)
                # name=re.sub('online','',name)
                # name=re.sub('free','',name)
                # name=re.sub('putlocker','',name)
                # name=re.sub('xmovie8','',name)
                # name=re.sub('xmovies8','',name)
				
                # url= 'http://moviewatcher.to' + url
                # if metaset=='false':
                        # try:
                                # addDir(name+'  ... Moviewatcher',url,18,icon,len(match),isFolder=True)
                        # except:pass
                # else:
                        # try:
                                # addDir(name+'   ... Moviewatcher',url,18,icon,len(match),isFolder=True)
                        # except:pass
     
    # except: pass
    try:
    	url = 'http://newonlinemovies.pro/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+'   ... NEWOnlineMOvies',url,22,icon,len(match),isFolder=True)
                        except:pass
    except: pass
    try:
    	url = 'http://hdmovie-14.com/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+' ... Hdmovies14.com',url,22,icon,len(match),isFolder=True)
                        except:pass
    except: pass

    try:
    	url = 'http://movie-32.com/?s='+search_entered
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span></a>').findall(link)[:5]
        for url,name in match:
                name=cleanHex(name)
                name=re.sub('HDTV','',name)
				
                
                if metaset=='false':
                        try:
                                addDir(name,url,22,icon,len(match),isFolder=True)
                        except:pass
                else:
                        try:
                                addDir(name+' ... Movie-32.com',url,22,icon,len(match),isFolder=True)
                        except:pass
    except: pass
    try:
    	url = 'http://rlssource.net/?s=' + search_entered + '&go=Search'
        link = open_url(url)
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(link)
        for url,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Rlssources[/COLOR]',url,29,iconimage,fanart)
    except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSsources is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

def GETLINKSMAZE(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<td><a rel=".+?" target=".+?" href="(.+?)" target=".+?">.+?</a></td>').findall(link)
        for url in match:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)
def GetLinks_base(url,name,iconimage):
        link = open_url(url)
        match = re.compile('href="(.+?)"').findall(link)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(link)
        match2 = re.compile('<IFRAME SRC="(.+?)"').findall(link)
        match3 = re.compile('<iframe src="(.+?)"').findall(link)
        for url in match + match2 + match3:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)       

def SEARCHTV():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search TV')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
     try:
    	url = 'http://www.watchonlinefreeseries.com/?s=' + search_entered
        link = open_url(url)
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+?  src="(.+?)"', re.DOTALL).findall(link)
        for url,name,img in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR yellow]Watchonline[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry watchonlinefree [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://300mbmovies4u.com/?s=' + search_entered 
        link = open_url(url)
        match = re.compile('<li>\s*?<h2><a href="(.+?)" title=".+?">(.+?)</a></h2>\s*?<div class=".+?"><a href=".+?" title=".+?"><img src="(.+?)"', re.DOTALL).findall(link)
        for url,name,img in match :
                name=cleanHex(name)

                addLink(name + '... [COLOR red]300mbmovies4u[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 300mbmovies4u is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
       url = 'http://www.warezmovies.info/?s=' + search_entered
       link = open_url(url)
       match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(link)
       for url,name,img in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Warez[/COLOR]',url,28,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Warezmovies  is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

     try:
    	url = 'http://watchitvideos.com/?s=' + search_entered
        link = open_url(url)
        match = re.compile('class="item-list"><h2 class="post-box-title"> <a\s*?href="(.+?)">(.+?)</a></h2><p.+?width="310" height="205" src="(.+?)"', re.DOTALL).findall(link)
        for url,name,img in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR yellow]Watchitvideos[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry watchitvideos is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://rlseries.com/?s=' + search_entered
        link = open_url(url)
        match = re.compile('<div class="img_wrp">\s*?<a href="(.+?)" title="(.+?)" class=".+?">\s*?<img width=".+?" height=".+?" src="(.+?)" class="attachment-poster wp-post-image" alt=".+?" />').findall(link)
        for url,name,img in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Rlseries[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSeries is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://watchseriesus.tv/?s=' + search_entered
        link = open_url(url)
        match = re.compile('<div class="moviefilm">\s*?<a href="(.+?)">\s*?<img src="(.+?)" alt="(.+?)" height=".+?" width=".+?" /></a>', re.DOTALL).findall(link)
        for url,img,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Watchseriesus[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry watchiseriesus is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://free-download.link/?s=' + search_entered
        link = open_url(url)
        match = re.compile('<a href="(.+?)" title="Permalink to .+?" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(link)
        for url,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]free-download.link[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry free-downloadlinks is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://watchseries-onlines.ch/?s=' + search_entered
        link = open_url(url)
        match = re.compile('<figure class="post-thumbnail">\s*?<a href="(.+?)">\s*?<img width="500" height="70" src="(.+?)" class="img-featured img-responsive wp-post-image" alt="(.+?)" />', re.DOTALL).findall(link)
        for url,img,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]watchseries-onlines[/COLOR]',url,31,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry watchseries.ch is down[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://rlssource.net/?s=' + search_entered + '&go=Search'
        link = open_url(url)
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(link)
        for url,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR lime]Rlssources[/COLOR]',url,29,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry RLSsources is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
     try:
    	url = 'http://series-cravings.me/?s=' + search_entered
        link = open_url(url)
        match = re.compile('<h1 class="entry-title">\s*?<a href="(.+?)" rel="bookmark">(.+?)</a>', re.DOTALL).findall(link)
        for url,name in match:
                name=cleanHex(name)

                addLink(name + '... [COLOR yellow]Series-cravings[/COLOR]',url,34,iconimage,fanart)
     except: xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry series-craving down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")


def GETUPTOBOX_BASE(url,name,iconimage):
        link = open_url(url)
        match = re.compile('href="(.+?)"').findall(link)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(link)
        match2 = re.compile('<IFRAME SRC="(.+?)"').findall(link)
        for url in match + match2:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)


		
def PLAYLINK(name,url,iconimage):
        name=selfAddon.getSetting('namestore')
        resp = urllib2.urlopen(url)
        url2 = resp.geturl()
        stream_url = urlresolver.HostedMediaFile(url2).resolve()
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url2,listitem=liz)
        xbmc.Player ().play(stream_url)
       
        
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
            season_list = 1
            season_num = 1
            episode_num = 1
            episode=metaget.get_episode_meta(imdb_id, season_num, episode_num)
            meta = mg.get_meta('movies', name=simplename ,year=simpleyear)
			seasons = metaget.get_seasons(imdb_id, season_list)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['backdrop_url'])
            liz.setInfo( type="Video", infoLabels= meta + episode + seasons )
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
elif mode==40: MOVIESINDEX()
elif mode==1: GETMOVIES(url,name)
elif mode==111: GETMOVIESNEW(url,name)
elif mode==7: GETFREEFULLMOVIES(url,name)
elif mode==16: GETMOVIEWATCHER(url,name)
elif mode==17: GETMOVIEWATCHER2(url,name)
elif mode==4: GETSEARCH(url,name)
elif mode==2: GETLINKS(url,name,iconimage)
elif mode==8: GETLINKSFREEFULLMOVIES(url,name,iconimage)
elif mode==3: SEARCH()
elif mode==5: MOVIEHDMAX()
elif mode==6: FREEFULLMOVIES()
elif mode==19: MOVIEWATCHER()
elif mode==9: GETMOVIESMAZE(url,name)
elif mode==10: GETLINKSMAZE(url,name,iconimage)
elif mode==11: GETTV(url,name)
elif mode==13: GETTVLINKS(url,name,iconimage)
elif mode==14: GETLINKVONLINE(url,name,iconimage)
elif mode==12: GETTVEPISODES(url,name)
elif mode==15: GETUPTOBOX_BASE(url,name,iconimage)
elif mode==18: GETLINKSMOVIEWATCHER(url,name,iconimage)
elif mode==20: ONLINEMOVIESIS()
elif mode==21: GETONLINEMOVIESIS(url,name)
elif mode==23: GETHDMOVIES14(url,name)
elif mode==22: GETONLINEMOVIESLINKS(url,name,iconimage)
elif mode==24: XMOVIES8()
elif mode==25: GETXMOVIES8(url,name)
elif mode==26: GETYEARSXMOVIES(url,name)
elif mode==27: GETGENRESXMOVIES(url,name)
elif mode==28: GETLINKS132(url,name,iconimage)
elif mode==29: GETLINKS10(url,name,iconimage)
elif mode==30: SEARCHTV()
elif mode==31: GetLinks_base(url,name,iconimage)
elif mode==32: GETSERIESCRAVING(url,name)
elif mode==33: GETSERIESCRAVING_EP(url,name)
elif mode==34: GETLINKS_SCRAVING(url,name,iconimage)
elif mode==35: GETMOVIESDB(url,name)
elif mode==36: GETLINKSDB(url,name,iconimage)
elif mode==37: AFDAH()
elif mode==38: GETMOVIESAFDAH(url,name)
elif mode==39: GETMOVIES2K(url,name)
elif mode==100: PLAYLINK(name,url,iconimage)
elif mode==101: PLAYLINKFREEFULLMOVIES(name,url,iconimage)
elif mode==102: PLAYLINKMAZE(name,url,iconimage)
elif mode==103: PLAYLINKMOVIEWATCHER(name,url,iconimage)
elif mode==104: PLAYLINKXMOVIES(name,url,iconimage)
elif mode==105: PLAYLINKAFDAH(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

