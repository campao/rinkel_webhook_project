# Rinkel Webhook Project

## Overview
This project uses Flask and ngrok to set up a local webhook listener for testing and interacting with the Rinkel REST API.

## Features
- Local webhook endpoint exposed via ngrok.
- Flask server to receive and process webhook events.
- Integration with Rinkel's REST API for tracking call data.

## Requirements
- Python 3.9
- Flask
- ngrok
- Git

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/campao/rinkel_webhook_project.git
   cd rinkel_webhook_project

2. Create and activate a Conda environment:
```bash
   conda create --name webhook_env python=3.9
   conda activate webhook_env

3. Install dependencies:
   ```bash
   pip install flask pyngrok

4. Run the Flask server:
   ```bash
   python src/webhook_listener.py

5. Start ngrok to expose the server:
   ```bash
   ngrok http 5000

6. Use the HTTPS URL provided by ngrok as your webhook endpoint.

