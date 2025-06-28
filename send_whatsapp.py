import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_alert(job):
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE")
    to_number = os.getenv("MY_PHONE")  

    client = Client(account_sid, auth_token)

    message_body = f"""
📢 *Job Alert!*

*Title:* {job['title']}
*Company:* {job['company_name']}
*Apply here:* {job['url']}
"""

    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )

    print("✅ WhatsApp alert sent:", message.sid)