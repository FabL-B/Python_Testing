# GÜDLFT

## Description

Améliorez une application Web Python par des tests et du débogage

## Features

- Unit testing to ensure the reliability of existing features.
- Debugging to identify and resolve potential issues.
- Performance testing with Locust.

## Installation:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/FabL-B/Python_Testing
    cd Python_Testing
    ```

2. Create and activate the virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate (for Linux and Mac)
    env\Scripts\activate (for Windows)
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the application:

1. Set up Flask:

    ```bash
    export FLASK_APP=server.py (for Linux and Mac)
    $env:FLASK_APP = "server.py" (for Windows)
    ```

2. Start the server:

    ```bash
    flask run
    ```

3. Open your browser and navigate to:

    ```bash
    http://127.0.0.1:5000
    ```

4. To test the application, you can log in using one of the following email addresses:

    - john@simplylift.co
    - admin@irontemple.com
    - kate@shelifts.co.uk

- Use the competition named "TEST" for booking to avoid restrictions.

## Running the Tests:

### **Unit and Integration Tests**
- To run all tests, execute:

    ```bash
    pytest
    ```
- To check the test coverage, use:
    ```bash  
    pytest --cov=server tests/
    ```

- For a detailed coverage report, generate an HTML report:
    ```bash
    pytest --cov=server --cov-report=html tests/
    ```
- The generated report will be available in the htmlcov/ folder. Open htmlcov/index.html in your browser to view the results.

## Performance Testing with Locust:
### Starting Locust

1. To run performance tests using Locust, start by launching the server in one terminal:

    ```bash  
    flask run
    ```

2. Then, in another terminal, navigate to the project directory and run:

    ```bash  
    locust
    ```

3. This will start Locust's web interface, accessible at:

    ```bash  
    http://127.0.0.1:8089
    ```

4. Configuring Locust

    - Open http://127.0.0.1:8089 in your browser.

    - Set the number of users to 6.

    - Ensure the Host field is set to:

        ```bash  
        http://127.0.0.1:5000
        ```

5. Click Start Swarming to begin the performance test.