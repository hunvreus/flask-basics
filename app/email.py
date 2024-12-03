import resend
from flask import current_app

def send_email(
    subject: str,
    sender: str | tuple[str, str],
    recipients: str | list[str],
    text_body: str,
    html_body: str
) -> None:
    """Send email using Resend in production, print to console in development"""
    sender_str = f"{sender[0]} <{sender[1]}>" if isinstance(sender, tuple) else sender
    email_data = {
        "from": sender_str,
        "to": recipients,
        "subject": subject,
        "text": text_body,
        "html": html_body,
    }

    if current_app.config['DEBUG'] or not current_app.config['RESEND_API_KEY']:
        print('--------------- EMAIL ---------------')
        print(f'From: {sender_str}')
        print(f'To: {recipients}')
        print(f'Subject: {subject}')
        print('--------------- TEXT ---------------')
        print(text_body)
        print('--------------- HTML ---------------')
        print(html_body)
        print('-----------------------------------')
        return
    
    resend.api_key = current_app.config['RESEND_API_KEY']
    resend.Emails.send(email_data)