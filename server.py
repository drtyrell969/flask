# import the nessecary pieces from Flask
from flask import Flask,render_template, request,jsonify,Response, url_for
from flaskext.mysql import MySQL

#Create the app object that will route our calls
app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Brav08root!!'
app.config['MYSQL_DATABASE_DB'] = 'laravel'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

query_string = "SELECT * FROM sptg_acts"
cursor.execute(query_string, (app.config['MYSQL_DATABASE_USER'],app.config['MYSQL_DATABASE_PASSWORD']))

data = cursor.fetchall()
 
if len(data) is 0:
    conn.commit()
    json.dumps({'message':'User created successfully !'})
else:
    json.dumps({'error':str(data[0])})



# Route the user to the homepage
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

#When run from command line, start the server
if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)