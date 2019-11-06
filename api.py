from flask import Flask, request, jsonify
from time import sleep
from delay import Delay

app = Flask(__name__)

@app.route("/sleep", methods=['GET', 'POST'])
def sleep():
	"""
	Induce a simple delay of 'x' seconds by sleeping
	"""

	# Read number of seconds from arguments. If not provided, default it to 10 seconds
	seconds = int(request.args.get("seconds", "10"))

	d = Delay()
	d.simple_delay_by_sleep(seconds)

	if request.method == 'POST':
		# If it is a POST request, simply return whatever input we have received.
		input_json = request.get_json()
		resp = jsonify({"Input received": input_json})
	else:
		# If it is GET request, return "Successful"
		resp = "Successful"

	return resp, 201

@app.route("/delay", methods=['GET', 'POST'])
def delay():
	"""
	Induce a CPU intensive delay of 'x' seconds
	"""

	# Read number of seconds from arguments. If not provided, default it to 10 seconds
	seconds = int(request.args.get("seconds", "10"))

	d = Delay()
	d.cpu_intensive_delay(seconds)

	if request.method == 'POST':
		# If it is a POST request, simply return whatever input we have received.
		input_json = request.get_json()
		resp = jsonify({"Input received": input_json})
	else:
		# If it is GET request, return "Successful"
		resp = "Successful"

	return resp, 201

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8081)