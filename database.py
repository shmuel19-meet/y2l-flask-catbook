from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name, votes=0)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_cat_by_id(id):

	cat = session.query(Cat).filter_by(id = id).first()
	return cat

def vote_cat(id):
	cat = get_cat_by_id(id)
	print("WORKS")
	print(cat.votes)
	cat.vote_cat()
	session.add(cat)
	session.commit()