#!jobqueuevirtualenv/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

queue_tasks = [

]

#get list of queue tasks
@app.route('/jobqueue/api/v1.0/queue_tasks', methods=['GET'])
def getqueue():
	return jsonify({'queue_tasks': queue_tasks})

#get specific queue task
@app.route('/jobqueue/api/v1.0/queue_tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in queue_tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'queue_task': task[0]})

#create a new queue task
@app.route('/jobqueue/api/v1.0/queue_tasks', methods=['POST'])
def create_task():
    if not request.json or not 'url' in request.json:
        abort(400)

    #handle empty dictionary
    if len(queue_tasks)>0:
    	task_id = queue_tasks[-1]['id'] + 1
    else:
    	task_id = 1
    #task to be posted
    task = {
        'id': task_id,
        'url': request.json['url'],
        'status': 'Waiting'
    }
    queue_tasks.append(task)
    return jsonify({'queue_task': task}), 201

if __name__ == '__main__':
	app.run(debug=True)