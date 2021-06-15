import pymysql
from flask import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker


engine=create_engine("mysql+pymysql://root@localhost/credit")
db=scoped_session(sessionmaker(bind=engine))

app=Flask(__name__)
app.debug=True

@app.route("/")
def home():
       res = db.execute("Select * from creditlist").fetchall()
       db.commit()
       return render_template("homepage.html",result=res)


if __name__ == "__main__":
	app.run()
	
