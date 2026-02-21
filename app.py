from os import name

from flask import Flask, render_template, request
from utils.triage import triage_symptoms
from utils.queue_sim import predict_waiting_time, remove_patient, add_patient, queue, urgency
from utils.notifications import send_sms
from utils.audit import log_action

app = Flask(__name__)

# Simulated current queue length
current_queue_length = 5

@app.route("/", methods=["GET","POST"])
def index():
    alert_msg = ""
    if request.method == "POST":
        symptoms = request.form.get("symptoms")
        phone = request.form.get("phone")
        urgency, recommended_time = triage_symptoms(symptoms)
        
        # Add patient to queue
        add_patient(f"Patient_{len(queue)+1}", urgency)

        # Predict waiting time
        waiting_time = predict_waiting_time()

        # Create alert message
        alert_msg = f"Urgency: {urgency}. Recommended time: {recommended_time}. Current predicted wait: {waiting_time} mins."

        # Send SMS (Twilio)
        if phone:
            send_sms(phone, alert_msg)
            
        log_action("TriagePerformed", patient=f"Patient_{len(queue)}", details={"urgency": urgency})
        log_action("SMSSent", patient=f"Patient_{len(queue)}", details={"message": alert_msg})


    return render_template("index.html", alert_msg=alert_msg)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", queue=queue, predicted_wait=predict_waiting_time())


if __name__ == "__main__":
    app.run(debug=True)