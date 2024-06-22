This is README file for  FastAPI-ML-Docker project. It includes step-by-step instructions for setting up a virtual environment, installing dependencies, structuring the project, building the Docker image, and running the container.

```markdown
# FastAPI-ML-Docker

This project demonstrates a FastAPI application for machine learning model inference using Docker. It allows users to upload an image and get predictions using a pre-trained model.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup Virtual Environment](#setup-virtual-environment)
- [Install Dependencies](#install-dependencies)
- [Running the Application Locally](#running-the-application-locally)
- [Docker Setup](#docker-setup)
- [Build Docker Image](#build-docker-image)
- [Run Docker Container](#run-docker-container)

## Project Structure
```
fastapi-ml-docker/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── model.py
├── Dockerfile
├── requirements.txt
└── run.sh
```

## Setup Virtual Environment
1. Navigate to the project directory:
   ```bash
   cd fastapi-ml-docker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## Install Dependencies
With the virtual environment activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application Locally
To run the FastAPI application locally, execute the following command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```


### Requirements File
Ensure your `requirements.txt` includes the following dependencies:
```
fastapi
uvicorn
transformers
torch
Pillow
```

### Run Script
Ensure your `run.sh` script includes the following content:
```bash
#!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Make sure `run.sh` is executable:
```bash
chmod +x run.sh
```



## STEP: Run docker init


```bash
docker init
```
STEP: Select Python image and use this command during docker init
```bash
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
## Run using Docker
To build the Docker image, run the following command in the root directory:
```bash
docker compose up --build
```
You can now access the application at `http://localhost:8000`.


## Examples
- file: cats.jpeg

   text: How many cats are there?

- file: tiger.jpeg

   text: What's the animal doing?

- file: palace.jpeg

   text: What is on top of the building?


## Additional Information
- Ensure Docker is installed and running on your machine.
- If you encounter issues with port binding, make sure no other application is using port 8000.

This README provides a full guide to setting up and running the FastAPI-ML-Docker project both locally and within a Docker container.


