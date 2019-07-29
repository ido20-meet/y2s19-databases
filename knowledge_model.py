from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'Wikipedia'
    wiki_id = Column(Integer, primary_key=True)
    title = Column(String)
    topic = Column(String)
    rating = Column(Integer)

    def __repr__(self):
        return ("title: {}\n"
               "topic: {} \n"
               "rating: {} \n"
               "wiki_id: {}").format(
                    self.title, self.topic, self.rating, self.wiki_id)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
Minecraft = Knowledge(wiki_id="1", title="Minecraft", topic="video game", rating="9")
print(Minecraft)
