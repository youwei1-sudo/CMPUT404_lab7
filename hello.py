#!/usr/bin/env python3

"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)

# we will get hellow world from code above
"""

# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
# data transfered to json

# api.add_resource(HelloWorld, "/")


# if __name__ == "__main__":
#     app.run(debug=True)

#!/usr/bin/env python3

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

# flask default port 5000 instead 8000

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

TODOs = {
    1: {"task": "build an API"},
    2: {"task": "?????"},
    3: {"task": "profit"},
}


fancy_html = """
	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta http-equiv="content-type" content="text/html; charset=utf-8" />
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<title>ChatByte | This is the Coolest Social Network</title>
			<!-- Stylesheets
	    ================================================= -->
			<link rel="stylesheet" href="{% static 'polls/css/bootstrap.min.css' %}" />
			<link rel="stylesheet" href="css/style2.css" />
			<link rel="stylesheet" href="css/ionicons.min.css" />
	    <link rel="stylesheet" href="css/font-awesome.min.css" />

	    <!--Google Font-->
	    <link href="https://fonts.googleapis.com/css?family=Titillium Web" rel="stylesheet">

			<style media="screen">
				body{
					overflow: hidden;
				}
			</style>
	</head>
	<body>
		<!-- Top Banner
		================================================= -->
		<section class="banner">
			<div class="container">

				<!-- Sign In Form
				================================================= -->
				<div class="sign-in-form">
					<a href="home.html" class="logo"><img src="" alt="Logo"/></a>
					<h1 class="text-white">CHATBYTE</h1>
					<hr class="solid">

					<div class="form-wrapper">
						<p class="signin-text">Sign in now and connect with awesome programming enthusiatics around the world!</p>
						<form action="post">
							<!-- <fieldset class="form-group">
								<input type="text" class="form-control" id="example-name" placeholder="Enter name">
							</fieldset>
							<fieldset class="form-group">
								<input type="email" class="form-control" id="example-email" placeholder="Enter email">
							</fieldset>
							<fieldset class="form-group">
								<input type="password" class="form-control" id="example-password" placeholder="Enter a password">
							</fieldset> -->
						    {% csrf_token %}
						    {{ form.as_p }}
						    <button type="submit" class="btn-secondary">Sign in</button>
						</form>
					</div>
					<a href="#">Do not have an account?</a>
					<img class="form-shadow" src="images/bottom-shadow.png" alt="" />
				</div><!-- Sign Up Form End -->


			</div>
		</section>

		<img class="back" src="images/tech_back.jpg"/>







		<!--preloader-->
		<div id="spinner-wrapper">
			<div class="spinner"></div>
		</div>

		<!-- Scripts
		================================================= -->
		<script src="js/jquery-3.1.1.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/jquery.sticky-kit.min.js"></script>
		<script src="js/jquery.scrollbar.min.js"></script>
		<script src="js/script.js"></script>
	</body>

"""

@app.route("/fancy")
def hello():
	# todo_items = [f"<li> {task["task"]}</li>" for task in TODOs]
    return fancy_html

def abort_if_todo_not_found(todo_id):
    if todo_id not in TODOs:
        abort(404, message="TODO {} does not exist".format(todo_id))


def add_todo(todo_id):
    args = parser.parse_args()
    todo = {"task": args["task"]}
    TODOs[todo_id] = todo
    return todo

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
# data transfered to json

class Todo(Resource):
    """
    Shows a single TODO item and lets you delete a TODO item.
    """


    # let use HTTP get to do resource
    def get(self, todo_id):
        abort_if_todo_not_found(todo_id)
        return TODOs[todo_id]

    # let use HTTP delete to do resource
    def delete(self, todo_id):
        abort_if_todo_not_found(todo_id)
        del TODOs[todo_id]
        return "", 204

    # let use HTTP put to do resource
    def put(self, todo_id):
        return add_todo(todo_id), 201


class TodoList(Resource):
    """
    Shows a list of all TODOs and lets you POST to add new tasks.
    """

    def get(self):
        return TODOs

    def post(self):
        todo_id = max(TODOs.keys()) + 1
        return add_todo(todo_id), 201


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos") # add class todolist to reasources
api.add_resource(HelloWorld, "/")
# http://127.0.0.1:5000/todos

if __name__ == "__main__":
    app.run(debug=True)