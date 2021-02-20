from flask import Flask
from redis import Redis
app = Flask(__name__)
db = Redis (host="172.17.0.2")

@app.route("/")
def hello():
    visitsCounter = db.incr('visitsCounter')
    html = "<H1> Hello!!! </H1>" \
	"<b>Visits: </b>{visits}"\
	"</br>"

    return html.format(visits=visitsCounter)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)

