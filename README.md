# jobqueue
**Originally developed as a coding challenge for [Massdrop](https://www.massdrop.com)**

A job queue whose workers fetch data from a URL and store the results in a database.  The job queue should expose a REST API for adding jobs and checking their status / results.

_Example:_

User submits www.google.com to your endpoint.  The user gets back a job id. Your system fetches www.google.com (the result of which would be HTML) and stores the result.  The user asks for the status of the job id and if the job is complete, he gets a response that includes the HTML for www.google.com

## Setup
* Install Python 2.7.
* Install Flask.
* Run ./app.py to start the server (on Windows use flask\Scripts\python app.py instead).
* Use curl to POST to job queue, and GET to receive information about the queue or the results from each job.

## Usage
**Add Job**

To add jobs, you can use the following:

<code>POST /jobqueue/api/v1.0/queue_tasks</code>

**Check Job Queue**

To check on the status of all jobs in the job queue, use:

<code>GET /jobqueue/api/v1.0/queue_tasks</code>

**Check Specific Job in Job Queue**

To check on the status of a specific jobs in the job queue, use:

<code>GET /jobqueue/api/v1.0/queue_tasks/:task_id</code>

**Receive Result List**

To check on the results of all jobs, you can use the following:

<code>GET /jobqueue/api/v1.0/results</code>

**Receive Result of Specific Task**

To check on the result of a certain job, you can use the following:

<code>GET /jobqueue/api/v1.0/results/:task_id</code>

## Implementation
**Languages/Frameworks**

_Front-End_
* HTML
* CSS
  * Bootstrap Grid
* Javascript

_Back-End_
* Flask

## Approach
I decided to build this project like I would in a hackathon. I started with my first few hours installing and learning Flask on Youtube.

**Challenges**

Before starting this challenge, I had no experience whatsoever with back-end development. However, I went in with a lot of front-end experience; I knew HTML, CSS, Javascript, JQuery, and AngularJS. Because I enjoy the simplicity of Python, I decided to learn and use Flask for this project. One of the main challenges was having to quickly learn from the ground-up.

As development continues, I will update this.

## Potential Issues/Bugs
As development continues, I will update this.
