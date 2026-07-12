# Smart Grammar-Based FAQ Assistant
### DeKUT’s School of Computer Science & IT

A smart voice- and text-based FAQ assistant designed to understand and respond to student questions directed to the Chair of Department (COD) and the Dean. The system models student queries using Context-Free Grammar (CFG) via NLTK, parses intents, and communicates seamlessly over WhatsApp using the Twilio API framework.

---

## 🛠️ Setup & Installation Procedure

Follow these steps sequentially to set up your local development environment on Windows 11.

### 1. Environment & Python Dependencies
Clone the repository, initialize a virtual environment, and install the optimized requirements tracking matrix:
```bash
# Initialize the virtual environment
python -m venv venv

# Activate the virtual environment
# For Git Bash / Linux:
source venv/Scripts/activate
# For Windows PowerShell:
# .\venv\Scripts\Activate.ps1

# Install core required dependencies
pip install -r requirements.txt

```

### 2. System Dependency: FFmpeg Audio Processing

The backend handles incoming `.ogg` WhatsApp voice recordings. To convert these files locally to `.wav`, you must install FFmpeg globally:

1. Open **PowerShell as an Administrator** and execute:
```powershell
winget install Gyan.FFmpeg

```


2. Close all terminal instances, reopen them, and verify the path mapping works correctly:
```bash
ffmpeg -version

```



### 3. Setup NLTK Language Data

Download the core tokenization models required by the CFG grammar extraction parser layers:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

```

### 4. Public Gateway Tunneling: ngrok

Because your backend handles local requests on port `5000`, you must provision a public proxy gateway to receive automated event payloads from Twilio:

1. Install ngrok globally using npm:
```bash
npm install -g ngrok

```


2. Create a free account at the [ngrok Dashboard](https://dashboard.ngrok.com/).
3. Retrieve your secure **Authtoken** from the panel and authenticate your local configuration:
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE

```



### 5. Telephony Integration: Twilio Sandbox Setup

1. Log into the [Twilio Console](https://console.twilio.com/).
2. Create a local environment variables file named `.env` in your project root using the configuration matching `.env.example`:
```env
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here

```


3. Navigate to **Messaging** -> **Try it out** -> **Send a WhatsApp message**.
4. Link your personal device to the sandbox by scanning the provided QR code or sending the specific passphrase (e.g., `join machine-tape`) to the designated Twilio sandbox phone number.

---

## 🚀 Execution & Testing Workflow

Always run your services in separate terminal sessions with your virtual environment `(venv)` active.

### Step 1: Fire Up the Public Tunnel

Expose your local development port to the internet:

```bash
ngrok http 5000

```

> ⚠️ **Important:** Copy the generated `https://xxxx-xxxx.ngrok-free.dev` forwarding URL address from the status window.
> Go to **Twilio Console -> Messaging -> Settings -> WhatsApp Sandbox Settings**. Paste the link into the **"When a message comes in"** configuration field, append `/whatsapp` to the end, ensure the method is **POST**, and click **Save**.

### Step 2: Validate CFG Parsing Accuracy

Open a secondary terminal window and verify the compiler constraints and grammar tree alignments:

```bash
python evaluate.py
python evaluate_ambiguity.py

```

### Step 3: Launch the Core Application Backend

Run the live Flask web application:

```bash
python app.py

```

---

## 🔗 Live Testing Access

* **Sandbox Onboarding Link:** Click [here to join the WhatsApp Sandbox](https://wa.me/14155238886?text=join%20machine-tape) *(Pre-fills your client text entry box with the required activation string).*
* **Deployed Bot Server Status:** `Active` 🚀

```

```