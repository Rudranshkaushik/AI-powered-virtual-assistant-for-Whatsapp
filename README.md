# AI-powered-virtual-assistant-for-Whatsapp

This project demonstrates how to deploy a fine-tuned GPT-2 model as a Flask web application, which can serve responses to questions about nutrition data. The app integrates with Twilio to create a WhatsApp chatbot.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Setting Up Twilio Webhook](#setting-up-twilio-webhook)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.8+
- Flask
- Transformers
- Torch
- Twilio

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/gpt2-whatsapp-chatbot.git
   cd gpt2-whatsapp-chatbot
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Download your fine-tuned GPT-2 model and tokenizer:**

   Ensure you place the model files in a directory named `fine-tuned-gpt2` in the root of the project.

## Configuration

- **Twilio Configuration:**
  - Sign up for a Twilio account and get a Twilio phone number.
  - Set up the webhook URL in the Twilio Console (detailed below).

## Usage

To run the app locally, execute:

```sh
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Setting Up Twilio Webhook

1. **Go to the Twilio Console.**
2. **Select your Twilio phone number.**
3. **Scroll down to the "Messaging" section.**
4. **Set the "A MESSAGE COMES IN" webhook URL to:**


5. **Save the changes.**

## Project Structure

```plaintext
gpt2-whatsapp-chatbot/
├── fine-tuned-gpt2/         # Directory containing the fine-tuned model
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
└── README.md                # Project README file
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
