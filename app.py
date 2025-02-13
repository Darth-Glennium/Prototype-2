from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Dictionary of predefined questions and answers for a roofing company
qa_pairs = {
    "hello": "Hello! Welcome to Rhino Mabati. How can we assist you today?",
    "do you sell mabati": "Yes, we sell high-quality roofing sheets. What type are you looking for?",
    "what types of mabati do you have": "We have corrugated sheets, box profile, tile profile, and polycarbonate sheets.",
    "do you offer free delivery": "We offer free delivery within selected areas. Please share your location to confirm.",
    "how much does a mabati sheet cost": "Prices vary depending on type and size. Please specify the mabati type and length.",
    "what sizes of mabati do you have": "We offer sheets in sizes from 2 meters to 12 meters. Custom sizes are also available.",
    "where is your company located": "We are located at [Company Address]. You can visit us or order online.",
    "how do i place an order": "You can order through our website, WhatsApp, or by calling us at [Phone Number].",
    "do you offer installation services": "Yes, we offer professional installation services. Let us know your location for a quote.",
    "do you have a warranty": "Yes! Our mabati sheets come with a [X-year] warranty against rust and corrosion.",
    "what colors do you have": "Our mabati comes in red, blue, green, charcoal, and more! Let us know your preference.",
    "can i get a quotation": "Sure! Please provide the type, size, and quantity of mabati sheets you need.",
    "bye": "Thank you for reaching out to Rhino Mabati. Have a great day!",
}

@app.route("/webhook", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Check if the incoming message matches a predefined question
    response = qa_pairs.get(incoming_msg, "I'm sorry, I didn't understand that. Can you please rephrase?")
    
    msg.body(response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
