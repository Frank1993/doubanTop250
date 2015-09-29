import urllib
from bs4 import BeautifulSoup
import os
import codecs  #ensure the write() function can handle chinese character

baseUrl='http://movie.douban.com/top250'

#store meta infomations of movies with .txt file within the same directory which contains this
# python file
filePath=os.path.join(os.path.abspath('.'),'doubanTop250.txt')  


def PageDownloader(pageUrl):
	moviesPage=urllib.urlopen(pageUrl).read().decode('utf-8')
	soup=BeautifulSoup(moviesPage,"html.parser")
	
	all_movies=soup.find_all('div','item')
	for movie in all_movies:
		MovieParse(movie)

	nextPageLink=soup.find('span','next')
	if nextPageLink.link:
		nextPageUrl =baseUrl+nextPageLink.link['href']
		print '-'*20+'processing a new page'+'-'*20
		PageDownloader(nextPageUrl)
	else:
		print '-'*20+"Job Done!"+'-'*20

def MovieParse(movie):

	#extract ranking of movie 
	ranking = movie.find('div','pic').em.string.strip()

	# extract titles of this movie, notice that one movie can have several different 
	# names due to release in different region
	titles=movie.find_all('span','title')
	print '-'*20+'processing:'+titles[0].string.strip()+'-'*20
	titleOfMovie=''
	for title in titles:
		titleOfMovie+=title.string.strip()
	otherTitles=movie.find_all('span','other')
	for otherTitle in otherTitles:
		titleOfMovie+=otherTitle.string.strip()

	#extract info of movie,including actors and types
	infoOfMovie=movie.find('p','').strings
	infoOfMovieList = []
 	for string in infoOfMovie:
 		infoOfMovieList.append(string.strip())

 	#extract rating of movie
 	starting=movie.find('div','star').find_all('span')


	rating=starting[0].em.string.strip()
	numberOfRating=starting[1].string.strip()

	#store infomation of this movie
	MovieInfoPersistent(ranking,titleOfMovie,infoOfMovieList[0],infoOfMovieList[1],rating,numberOfRating)

def MovieInfoPersistent(ranking,titles,actors,types,rating,numberOfRating):
	infoToStore=ranking+'   '+titles+'   '+actors+'   '+types+'   '+rating+'   '+numberOfRating+'\n'

	with codecs.open(filePath,'a','utf-8') as f:
		f.write(infoToStore)

if __name__ == "__main__":
	print '-'*20+'starting processing:'+'-'*20 
	PageDownloader(baseUrl)

