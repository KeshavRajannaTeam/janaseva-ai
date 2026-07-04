from whatsapp import send_message


def handle_message(phone, text):

    text = text.strip().lower()

    if text in ["hi", "hello", "start", "/start"]:

        send_message(
            phone,
            "👋 Welcome to Janaseva AI\n\n"
            "We are here to help you with government services.\n\n"
            "Please choose a service:\n\n"
            "1️⃣ Aadhaar\n"
            "2️⃣ Voter ID\n"
            "3️⃣ Gruha Guarantee\n"
            "4️⃣ Income Certificate\n"
            "5️⃣ Caste Certificate"
        )

    else:

        send_message(
            phone,
            "Sorry, I didn't understand that.\n\n"
            "Please type *Hi* to begin."
        )