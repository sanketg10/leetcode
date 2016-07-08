#To open a file and read its content

import urllib
import os 

def reading_text(): 
  # ratings = open(os.path.expanduser("/Users/sanketgupta/leetcode/Python/Non-Leetcode/ratings.txt"))
  # ratings = open("/Users/sanketgupta/leetcode/Python/Non-Leetcode/ratings.txt")
  # content = ratings.read()
  sending = "whatsup star shot"
  content_checker(sending) 

def content_checker(text): 
  connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text).read() 
  print connection 
  #connection.close() 

reading_text()