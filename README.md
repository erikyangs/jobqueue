# jobqueue
**Originally developed as a coding challenge for [Massdrop](https://www.massdrop.com)**

A job queue whose workers fetch data from a URL and store the results in a database.  The job queue should expose a REST API for adding jobs and checking their status / results.

_Example:_

User submits www.google.com to your endpoint.  The user gets back a job id. Your system fetches www.google.com (the result of which would be HTML) and stores the result.  The user asks for the status of the job id and if the job is complete, he gets a response that includes the HTML for www.google.com

## Setup
* Install Python 2.7.
* Install Flask.
* Run app.py to start the server. (python app.py)
* Go to http://localhost:5000, and all usage rules listed down below as well as front-end UI should be present.

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
  * JQuery

_Back-End_
* Flask (Python framework)

**Features**

* Adds URL to a Queue
* Uses multithreading (worker threads) to fetch HTML data from endpoints
* Updates queue and result object when job finishes
* Notifies user of 404 and 400 errors

## Challenges

I knew a lot of front-end development: HTML, CSS, Javascript, JQuery, AngularJS.

Unfortunately, I did not know anything about back-end development. I had no clue what a RESTful API was, how to use threads, and how to fetch data from endpoints. To be honest, it was a really rough start. I spent a day trying to settle on what language and framework I would use. Eventually I chose to use Flask because I enjoy the simplicity of Python.

Learning Flask was a huge struggle. I went through Google and Youtube to get some of the basics down, and then tried coding. A lot of the time was spent scouring StackOverflow for answers. However, after a long time, I was able to get started and build up. One of the biggest challenges was figuring out how to run background tasks when fetching data from endpoints. I had to read up about worker threads and took some time to implement them into my project.

## Successes

The easy part was implementing the front-end. It was really satisfying to have everything fall into place, and have a pretty front-end to display what I had constructed on the back-end. Although it was challenging, this was quite a fulfilling project to make that gave me perspective into the other half of web development I before was too scared to learn. Hooray! Mission Success!

## Potential Issues/Bugs
* Security
  * There are no limits to who can GET and POST to the server. Future implementations should include user authentication.
* Data
  * Data is stored as a Python dictionary, and thus is not persistent. Perhaps MySQL and a Python connector to MySQL could be a solution.
* Code Style
  * All HTML, CSS, Javascript, and JQuery is all in templates/index.html. Better style would separate these languages through external linking.
  * Code is very repetitive on the front-end. For testing purposes, I consciously did so. However, a cleaner, more modular method would be to use templating, provided by frameworks like Flask or AngularJS.
* Input
  * Ironically, https://www.google.com does not work because jsonify cannot parse through the HTML String.
  * Does not work with websites such as https://www.airbnb.com because of forbidden access.
  * Works with https://www.facebook.com however!
* Output
  * The ID is generated from 1 up. In a smarter implementation ID's should be handled by a database. When researching, I found that MySQL has an auto-increment feature, which could come into use.
* UI
  * HTML text is extremely long; introduce a button to toggle which results to show, and perhaps put the data in a more organized fashion such as a table.
