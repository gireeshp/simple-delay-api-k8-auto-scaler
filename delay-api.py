from flask import Flask
from time import sleep
from delay import Delay

app = Flask(__name__)

@app.route("/delay")
def delay():
	print ("Inside")
	d = Delay()
	d.start_a_delay(4, 200, lambda : (False))
	return "Successful", 200

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8081)
	# app.run()