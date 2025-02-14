from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body", "").strip().lower()
    response = MessagingResponse()
    msg = response.message()

    if incoming_msg in ["hello", "hi"]:
        msg.body(
            "Welcome to Rhino Mabati! Please choose an option:\n"
            "1️⃣ Types of Roofing Sheets\n"
            "2️⃣ Available Colors\n"
            "3️⃣ Pricing & Delivery"
        )

    elif incoming_msg == "1":
        msg.body(
            "We offer the following roofing sheets:\n"
            "1️⃣ Germania\n"
            "2️⃣ Romania\n"
            "3️⃣ Brit\n"
            "4️⃣ Orientile\n"
            "5️⃣ Jamii Max\n"
            "6️⃣ Corrugated"
        )

    elif incoming_msg == "2":
        msg.body(
            "Available colors:\n"
            "🎨 Charcoal Grey\n"
            "🎨 Blue\n"
            "🎨 Maroon\n"
            "🎨 Brick Red\n"
            "🎨 Wood Effect"
        )

    elif incoming_msg == "3":
        msg.body(
            "Pricing & Delivery:\n\n"
            "🔹 *Matte Finish*\n"
            "G28: Ksh 745 (Self Collection) | Ksh 745 (Delivery)\n"
            "G30: Ksh 600 (Self Collection) | Ksh 680 (Delivery)\n\n"
            "🔹 *Glossy Finish*\n"
            "G28: Ksh 625 (Self Collection) | Ksh 680 (Delivery)\n"
            "G30: Ksh 500 (Self Collection) | Ksh 575 (Delivery)"
        )

    else:
        msg.body(
            "Sorry, I didn't understand that. Please reply with:\n"
            "1️⃣ Types of Roofing Sheets\n"
            "2️⃣ Available Colors\n"
            "3️⃣ Pricing & Delivery"
        )

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
