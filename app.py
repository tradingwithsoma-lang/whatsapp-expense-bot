from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

balance = 26500

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    global balance

    incoming_msg = request.form.get('Body').lower()
    resp = MessagingResponse()
    msg = resp.message()

    try:
        if "spent" in incoming_msg:
            parts = incoming_msg.split()
            amount = int(parts[1])
            note = " ".join(parts[2:])

            balance -= amount

            reply = f"✅ Expense added\n💸 {amount} - {note}\n💰 Balance: {balance}"

        elif "add" in incoming_msg:
            parts = incoming_msg.split()
            amount = int(parts[1])
            balance += amount

            reply = f"💵 Added {amount}\n💰 Balance: {balance}"

        elif "balance" in incoming_msg:
            reply = f"💰 Current Balance: {balance}"

        else:
            reply = "Send:\n- spent 100 tea\n- add 5000\n- balance"

    except:
        reply = "❌ Format error. Try: spent 100 tea"

    msg.body(reply)
    return str(resp)
