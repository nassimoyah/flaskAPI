from flask import Flask, jsonify, request ,render_template
  
# creating a Flask app 
app = Flask(__name__) 
  

@app.route('/home', methods = ['GET']) 
def home(): 
    return render_template('home.html') 
  

 
if __name__ == '__main__': 
  
    #app.run(debug=True, port=3000)        ###  ACCESSIBLE ONLY FOM THIS MACHINE 
    app.run(host='0.0.0.0', port=5000) 