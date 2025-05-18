<h1>
  <img src="assets/day_pilot_logo_transparent.png" width="100" style="vertical-align: middle; margin-right: 10px;">
  DayPilotAI
  <img src="https://img.shields.io/badge/DayPilot-In_Development-blue" style="vertical-align: middle; margin-left: 10px;">
</h1>

## Introduction:
This repository contains the AI backend for the DayPilot project, focused on processing speech-to-text inputs into structured task data. Built with Flask, this API serves as the connection between the Android mobile app (built in Android Studio) and the task generation logic.

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
  **Api**:

## Development Setup:

## Contributors:

## Project Status:
