from flask import Flask, jsonify, request ,render_template
import os 

# creating a Flask app 
app = Flask(__name__) 
  

@app.route('/', methods = ['GET']) 
def home(): 
    return render_template('home.html') 
  

 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port, default to 5000 for local testing
    app.run(host='0.0.0.0', port=port)