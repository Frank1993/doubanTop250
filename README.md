# doubanTop250
a crawl to extract information of movies rated as top 250 on douban, a rating website for movies, music and so like.

##fields extracted
ranking,titles,director,actors,types,rating,number of rating

##models used

 - urllib  download movie page
 - BeautifulSoup parse the html and extract desired informations
 - os get the path of the python file 
 - codecs handle chinese character when useing write() function to write informations of movies into a .txt file
 
