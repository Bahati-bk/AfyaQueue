# 🏥 AfyaQueue – Autonomous Health Access & Waiting-Time AI Agent

> “In Uganda, healthcare access fails in the queue. AfyaQueue is the first AI agent that treats _waiting_ as a medical risk.”

## **Project Overview**

AfyaQueue is an **AI agent** that:

- Collects patient symptoms via web form
- Performs **OpenAI-powered triage** (Low / Medium / High urgency)
- Recommends **best visit time** based on queue predictions
- Sends **SMS/WhatsApp alerts** to patients (via Twilio)
- Simulates real-time **patient queue updates**
- Provides a **facility dashboard** with live queue and waiting times

## **Features**

| Feature                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| Patient Triage          | AI-driven urgency classification               |
| Queue Simulation        | Dynamic arrivals & departures of patients      |
| Waiting-Time Prediction | Estimated wait based on urgency & queue length |
| SMS Alerts              | Real-time notifications to patients            |
| Facility Dashboard      | Live view of queue & predicted waiting time    |

## **Tech Stack**

- **Python 3.11**
- **Flask** (Web server & frontend)
- **OpenAI GPT-3.5-turbo** (Triage & urgency scoring)
- **Twilio API** (SMS/WhatsApp alerts)
- **Gunicorn** (Cloud deployment)
- **Render / Railway** (Cloud hosting)

## **Project Structure**

```text
AfyaQueue/
├─ app.py                  # Flask app
├─ requirements.txt        # Python dependencies
├─ templates/
│  ├─ index.html           # Patient input form
│  ├─ dashboard.html       # Facility dashboard
│  └─ alert.html           # Patient alert display
├─ static/
│  └─ style.css            # Optional styling
├─ utils/
│  ├─ triage.py            # OpenAI-based symptom triage
│  ├─ queue_sim.py         # Dynamic queue simulation
│  └─ notifications.py     # Twilio SMS/WhatsApp notifications
└─ README.md
```

## **Setup Instructions**

### **1. Clone the Project**

```bash
git clone <your-repo-url>
cd AfyaQueue
```

### **2. Create Virtual Environment & Install Dependencies**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Set Environment Variables**

Create `.env` file or set environment variables in your terminal/cloud:

```bash
export OPENAI_API_KEY="your_openai_api_key"
export TWILIO_ACCOUNT_SID="your_twilio_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
export TWILIO_PHONE_NUMBER="+2567XXXXXXXX"
```

> Replace the phone number with your Twilio verified number.

### **4. Run Locally**

```bash
python app.py
```

- Patient input: `http://127.0.0.1:5000/`
- Facility dashboard: `http://127.0.0.1:5000/dashboard`

You can submit symptoms + phone number to receive **live SMS alerts**.

### **5. Deploy to Cloud (Render)**

1. Push repo to GitHub.
2. On **Render → New Web Service → Connect GitHub**
3. Set runtime: **Python 3.11**
4. Command: `gunicorn app:app`
5. Add environment variables (OpenAI + Twilio keys).
6. Deploy → AfyaQueue is **live & ready**.

## **Demo Flow**

1. **Patient Submits Symptoms:** Enter symptoms + phone number → AI triage → SMS alert
2. **Facility Dashboard:** View current queue & predicted waiting time
3. **Dynamic Queue:** Queue updates every 5 seconds → simulates arrivals & departures
4. **Alert Example:**

   > “Urgency: High. Recommended time: NOW. Current predicted wait: 10 mins.”

## **Customization**

- Modify **queue simulation timing** in `utils/queue_sim.py`
- Adjust **urgency weights** or triage logic in `utils/triage.py`
- Replace **SMS simulation with real WhatsApp** via Twilio

## **Requirements**

`requirements.txt`:

```text
Flask==2.3.5
openai==1.30.0
pandas==2.1.1
numpy==1.26.5
requests==2.32.0
twilio==8.11.0
gunicorn==21.2.0
```

## **Screenshots / Demo (will be added in afew)**

- Patient Input Form
- Facility Dashboard (Queue + Waiting Time)
- SMS Alert Example

## **License**

MIT License – free to hackathon participants and students.
