Use Addon REST API Tester
To test server

# Flask-Redis API with Docker Compose

This project demonstrates a simple Flask API with Redis as a backend database, encapsulated in Docker containers. Follow the steps below to set up and run the project.

## Prerequisites

1. [Docker](https://www.docker.com/get-started) installed on your machine.
2. [Python](https://www.python.org/downloads/) installed.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/isaquerr25/server-python-redis
cd server-python-redis
```

### 2. Start Redis with Docker Compose

```bash
cd redis
docker-compose up -d
```

This will start a Redis container in the background.

### 3. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate

```

### 4. Install Dependencies

```bash
pip install -r requirements.txt

```

### 5. Start the Flask API

```bash
python app.py

```

The API will be running at http://localhost:5000/.

### API Endpoints

    GET /get/{key}: Retrieve the value for a specific key.
    POST /set: Set a value for a specific key.
        Request Body: { "key": "your_key", "value": "your_value" }
    PUT /update: Update the value for an existing key.
        Request Body: { "key": "your_key", "value": "new_value" }
    DELETE /delete/{key}: Delete a key-value pair.
    GET /getall: Retrieve all key-value pairs.
