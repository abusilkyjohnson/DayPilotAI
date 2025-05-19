<h1>
  <img src="assets/day_pilot_logo_transparent.png" width="100" style="vertical-align: middle; margin-right: 10px;">
  DayPilotAI
  <img src="https://img.shields.io/badge/DayPilot-In_Development-blue" style="vertical-align: middle; margin-left: 10px;">
</h1>

## Introduction:
This repository acts as a sister repo to https://github.com/memo609memo/DayPilot which contains the AI backend for the DayPilot project, focused on processing speech-to-text inputs into structured task data. Built with Flask, this API serves as the connection between the Android mobile app (built in Android Studio) and the task generation logic.

When a user taps the microphone button in the Android app, the device captures voice input using Android’s built-in speech-to-text feature. That converted text is then sent to this AI model via a POST request. Upon receiving the text, the model interprets the user's intent and returns a structured response that the app uses to create a new task.

This AI system acts as the ears of the app turning casual voice input into actionable task data for a smarter, faster task-creation experience.

## Feactures:

- Converts voice input from Android into structured task data
- Receives speech-to-text text via API
- Analyzes user intent using AI model
- Returns parsed task components (title, time, date, etc)
- ### How It Works

  1. 📱 Android app captures user speech and converts it to text.
  2. 🌐 The Android app sends the text to the AI backend endpoint using an HTTP request.
  3. 🧠 AI model analyzes the text and identifies task-related information (e.g. title, date, time).
  4. 🔁 The response is sent back to the Android app to generate the task.

## Technologies:
- **Python 3.12.8** – Core programming language used for AI logic and API
- **Tensor Flow** – Deep learning model integration
- **JSON** – Data format for request/response between app and server
  
  <h3 align="center">API</h3>

**Flask** – Lightweight Python framework for building RESTful APIs
-  Flask receives incoming POST requests from the Android app.
- It parses the JSON data that contains the user's spoken input (converted to text by android built-in MicrophoneX).
- The text is passed to the AI model for intent parsing and task extraction.
- Flask then sends the model’s response back to the app in structured JSON format.
 
All of this logic is contained in the Flask app within this repository.

## Installation:
This repo is meant for backend usage. Users must:

1. Clone the repo  
2. Create a virtual environment  
3. Activate the virtual environment  
4. Install dependencies with `pip install -r req.txt`

Once dependencies are installed, the project will compile and the user can input text into the model for task related label generation.

## License:
©[Michael DiBella, Ryan Reese, Luis Orellana, Abubakar Mohammed] [2025]. This project is under development. License will be determined later on.

## Development Setup:
To any new developer joining this repository:
This is the AI component of the Capstone project and is responsible for handling backend logic and natural language processing. The codebase is designed to be modular and reusable; it can be integrated with any application that interacts with a Flask API.

This backend receives text input (typically from an Android app's speech-to-text feature), processes it through an AI model, and returns structured task information.

To get started, please follow the installation instructions below to ensure all required dependencies are installed correctly and the API can compile and run without issues.

<h3 align="center">Repository Access </h3>
This AI backend is a core part of our Capstone project. Only approved team members are permitted to push changes directly to this repository.

If you are not a designated contributor but would like to experiment or suggest changes:
- Please **fork** this repository
- Work in your forked version
- Open a **pull request** for review 

## Contributors:
Abubakar Sadiq Mohammed

## Project Status: 
<img src="https://img.shields.io/badge/DayPilot-In_Development-blue" style="vertical-align: middle; margin-left: 10px;">

