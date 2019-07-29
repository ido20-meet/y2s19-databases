from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wiki_id, title, topic, rating):
	new_article = Knowledge(wiki_id=wiki_id, title=title, topic=topic, rating=rating)
	session.add(new_article)
	session.commit()

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic():
	articles = session.query(Knowledge).first()
	return articles

def delete_article_by_wiki_id(wiki_id):
	session.query(Knowledge).filter_by(wiki_id=wiki_id).delete()
	session.commit()
def delete_all_articles():
	pass

def edit_article_rating():
	pass
# add_article(3, "Dogs", "Animals",10)
# add_article(2, "MIT", "University",7)

print(query_all_articles())
# print(query_article_by_topic())
# delete_article_by_wiki_id(2)