from flask import Flask
from flask_restful import Api, Resource

# Initialize Flask app and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    # Define the HelloWorld resource
    def get(self):

        # Define the GET method
        return {"message": "Hello World!"}, 200

# Add the HelloWorld resource to the URI "/"
api.add_resource(HelloWorld, "/")

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)