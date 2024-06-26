from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

model_path = './fine-tuned-gpt2'  # Update this to your model's path
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

@app.route("/model", methods=["POST"])
def model_endpoint():
    data = request.get_json()
    question = data.get("question", "")
    
    if not question:
        return jsonify({"answer": "Please provide a question"}), 400

    inputs = tokenizer.encode(question, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"answer": answer})

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get('Body')
    resp = MessagingResponse()
    msg = resp.message()
    
    if incoming_msg:
        # Process the incoming message and generate a response
        inputs = tokenizer.encode(incoming_msg, return_tensors='pt')
        outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        msg.body(answer)
    else:
        msg.body("Please send a valid question.")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
