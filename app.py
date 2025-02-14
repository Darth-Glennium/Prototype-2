import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Store user states (this should be stored in a database for production)
user_sessions = {}

@app.route("/webhook", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    sender_number = request.values.get('From')  # Unique identifier for users
    resp = MessagingResponse()
    msg = resp.message()

    # Check if user exists in session
    if sender_number not in user_sessions:
        user_sessions[sender_number] = {"step": "menu"}  # Start at menu

    step = user_sessions[sender_number]["step"]

    # Greet user and show menu if they send "hello"
    if step == "menu" and incoming_msg in ["hello", "hi"]:
        response_text = (
            "Hello! Welcome to Rhino Mabati. How can we assist you today?\n\n"
            "1️⃣ Profile\n"
            "2️⃣ Products\n"
            "3️⃣ Pricing\n"
            "4️⃣ Order Process\n"
            "5️⃣ Contact Us\n"
            "Reply with a number to choose an option."
        )
        user_sessions[sender_number]["step"] = "waiting_for_choice"

    elif step == "waiting_for_choice":
        if incoming_msg == "1":
            response_text = "📌 *Profile*\nRhino Mabati is a leading supplier of high-quality roofing materials..."
        elif incoming_msg == "2":
            response_text = "🏠 *Products*\nWe offer different types of mabati including corrugated, tile, and box profiles."
        elif incoming_msg == "3":
            response_text = "💰 *Pricing*\nOur pricing depends on size and type. Please visit our website for a full catalog."
        elif incoming_msg == "4":
            response_text = "🛒 *Order Process*\nTo place an order, visit our website or call us at +2547XXXXXXX."
        elif incoming_msg == "5":
            response_text = "📞 *Contact Us*\nYou can reach us via WhatsApp, email, or call: +2547XXXXXXX."
        else:
            response_text = "⚠️ Invalid choice. Please reply with a number (1-5)."

        # After responding, send them back to menu
        response_text += "\n\nType *hello* to return to the main menu."
        user_sessions[sender_number]["step"] = "menu"

    else:
        response_text = "I didn't understand that. Type *hello* to start over."

    msg.body(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
