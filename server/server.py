from flask import Flask, request, jsonify
import sys
import os
#need so my model package works 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.day_pilot_ai_model import get_time_date_description

app = Flask(__name__)

@app.route("/tasks", methods=["POST"]) #route is more explicit post fr multiple http handle
def create_task():
    try:
        abuGrabber = request.get_json(force=True) # to grab incomin post 
        user_text = abuGrabber.get("text", "") #"text" cn be like key value pair n text needs to be exact 


        print("Received from Android:", user_text) # abu this for debugging delete later 
        
        if not user_text: # if not user text n give me error code for 400
            return jsonify({"success": False, "error": "no text provided"}), 400

        result = get_time_date_description(user_text)

        user_text_jsonify = jsonify(success=True, **result)

        print("json response:", user_text_jsonify.get_data(as_text=True)) # for debugging delete later 
        
        return user_text_jsonify

    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

