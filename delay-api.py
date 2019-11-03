from flask import Flask, request, jsonify
from time import sleep
from delay import Delay

app = Flask(__name__)

@app.route("/delay", methods=['GET', 'POST'])
def delay():
	# d = Delay()
	# d.start_a_delay(4, 200, lambda : (False))

	sleep(10)

	resp = "Successful"

	if request.method == 'POST':
		input_json = request.get_json()
		resp = jsonify({"Input received": input_json})

	return resp, 201

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8081)
	# app.run()