#!jobqueuevirtualenv/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

queue_tasks = [
	{
		'id': 1,
		'url': 'http://erikyangs.github.io/',
		'status': 'Done'
	},
	{
		'id': 2,
		'url': 'http://petr-lee.github.io/',
		'status': 'In Progress'
	},
	{
		'id': 3,
		'url': 'http://tianruichen.github.io/',
		'status': 'Waiting'
	}
]

@app.route('/jobqueue/api/v1.0/queue_tasks', methods=['GET'])
def getqueue():
	return jsonify({'queue_tasks': queue_tasks})

if __name__ == '__main__':
	app.run(debug=True)