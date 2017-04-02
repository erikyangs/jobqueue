#!jobqueuevirtualenv/bin/python
from flask import Flask, jsonify, abort, request, render_template
import urllib2

# ===================================

from Queue import Queue
from threading import Thread

q = Queue()

def worker():
    print "Started worker thread"
    while True:
        task = q.get()
        task['status'] = 'In Progress'
        do_work(task)
        task['status'] = 'Done'
        q.task_done()

def do_work(task):
	task_url = task['url']
	task_HTML = getURLHTML(task_url)
	result = {
		'id': task['id'],
		'data': task_HTML
	}
	results.append(result)

for i in range(2):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

def getURLHTML(url):
	return urllib2.urlopen(url).read()

# ===================================

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

queue_tasks = []
results = []

#get list of results
@app.route('/jobqueue/api/v1.0/results', methods=['GET'])
def getresults():
	return jsonify({'results': results})

#get specific result
@app.route('/jobqueue/api/v1.0/results/<int:result_id>', methods=['GET'])
def get_result(result_id):
    result = [result for result in results if result['id'] == result_id]
    if len(result) == 0:
        abort(404)
    return jsonify({'result': result[0]})

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
    q.put(task)
    return jsonify({'queue_task': task}), 201

if __name__ == '__main__':
	app.run(debug=True)