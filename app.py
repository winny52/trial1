from flask import Flask
 
app=Flask(__name__)
 
@app.route("/")
def hello():
    return'I have deployed my first flask app'

if __name__ == '__main__':
  app.run()