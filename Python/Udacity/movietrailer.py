import webbrowser    #This is the package, it can be used by webbrowser.any function within it()

class MovieTrailer():   
    """This class provides a way to show movie trailers"""  #This info can be accessed via __doc__ variable
    VALID_RATINGS = ["UA","A","U"]   #Universal variables preferably in caps
    def __init__(self,title,story,review,youtube_link):  #__init__ function gets called whenever a new instance of a class is created
      self.title = title    #This allows the object's title property to be linked to title which is sent to this function while the object is created
      self.story = story
      self.review =review 
      self.youtube_link = youtube_link 


    def show_trailer(self): 
      webbrowser.open(self.youtube_link)    #Need to use self.youtube_link as it is universal NOT youtube_link


class Documentaries(MovieTrailer):  #To learn inheritance -- to inherit a class use it in parantheses
