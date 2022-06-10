from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World!"

@app.route('/dojo')
def something():
   return "Dojo!"

@app.route('/say/<name>')
def say(name):
   return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
   for i in range(num):
      # return f"{word * num}" -
      # I would think that there would be a way to enter a line break of some sort \ or even a string break \n 
      # but neither seem to be working :( 

      output = ''
      for i in range(0,num):
         output += f"<p>{word}</p>"  # This utilizes inline-block ensures its own line
      return output

      


if __name__ == "__main__":
   app.run(debug = True)