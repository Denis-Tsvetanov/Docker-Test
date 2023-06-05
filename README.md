# Docker-Test
### Model Summary
Dataset: Iris dataset
Model: Logistic Regression
This model is trained to perform logistic regression on the Iris dataset. Logistic regression is a classification algorithm used to predict the probability of an instance belonging to a particular class. In this case, the model is trained to classify Iris flowers into different species based on features such as sepal length, sepal width, petal length, and petal width.

### Downloading Required Files
To create a Docker image and test the API, you'll need the following files:

Python code file (main.py): Contains the FastAPI code for the API.
Trained model file (irislogreg.pkl): Contains the serialized logistic regression model.
Dockerfile: Specifies the instructions to build the Docker image.
You can download the Python code, model file, and Dockerfile from the repo

### Building Docker Image and Testing the API
To create a Docker image and test the API, follow these steps:

Install Docker: Download and install Docker from the official Docker website (https://www.docker.com/get-started) for your operating system.

##### Build the Docker image:

"docker build -t my_app_image ."
This command builds a Docker image using the Dockerfile in the current directory. The -t flag assigns a tag (name) to the image. In this example, the tag is set as my_app_image. Ensure that you run this command in the same directory where the Dockerfile and other required files are located.

##### Run the Docker container:

"docker run -d -p 8000:8000 my_app_image"
This command starts a Docker container based on the image. The -d flag runs the container in detached mode, and the -p flag maps the host machine's port 8000 to the container's port 8000. Again, replace my_app_image with the actual image name you provided in the previous step.

### Test the API:
You can now send requests to the API using tools like curl or Postman. For example, using curl:

curl -X POST -H "Content-Type: application/json" -d '{"data": [1, 2, 3, 4]}' http://localhost:8000/predict
This command sends a POST request to the specified URL with a JSON payload containing the data field. Adjust the payload data to match the expected format for your API.

Make sure the Docker daemon is running, and the container is successfully started before testing the API.
