from flask import Flask, render_template, request  # Import Flask for web app, render_template for HTML pages, request for form data
import smtplib  # Built-in for sending emails
from email.mime.text import MIMEText  # For formatting emails
from dotenv import load_dotenv  # Load .env secrets
import os  # For accessing environment variables

app = Flask(__name__)  # Create the app instance—think of this as starting your engine

load_dotenv()  # Load .env at startup—now os.getenv() can grab values safely (secrets like email creds)

@app.route('/')  # This decorator says: When someone visits the root URL (like localhost:5000/), run this function
def home():
    return render_template('index.html')  # Serve the index.html page from templates folder

@app.route('/generate_email', methods=['GET'])  # New route for email preview—visit /generate_email to see it
def generate_email():
    # Simple template—made dynamic with placeholders to match your .format() call below (avoids errors)
    template = """
Subject: Urgent Account Update Required

Dear NSAILA RIDLEY,

We've detected unusual activity on your account. Click here to verify: https://x.com/

Best,
X Team (Formerly known as Twitter) 
    """
    # Replace placeholders with values—this makes it reusable!
    email_content = template.format(name="NSAILA RIDLEY", link="https://x.com/")  # Updated to match your custom values; change as needed
    return f"<pre>{email_content}</pre>"  # Show as preformatted text in browser for preview (keeps formatting nice)

@app.route('/send_email', methods=['GET', 'POST'])  # New route: Handles form submit (GET shows form, POST sends)
def send_email():
    if request.method == 'POST':  # If form submitted
        recipient = request.form['recipient']  # Get input from form
        name = request.form['name']  # Custom name for personalization

        # Reuse our template—dynamic!
        template = """
Subject: Urgent Account Update Required

Hello NSAILA RIDLEY,

We've detected unusual activity on your account. Click here to verify: https://x.com/

Best,
X Team (Formerly known as Twitter)
        """
        link = "http://localhost:5000/track_click?user_id=1"  # Placeholder tracking link (we'll make real tracking later)
        email_content = template.format(name=name, link=link)

        # Set up email message
        msg = MIMEText(email_content)
        msg['Subject'] = 'Urgent Account Update Required'  # Redundant but explicit
        msg['From'] = os.getenv('EMAIL_USER')
        msg['To'] = recipient

        try:
            # Connect to SMTP server—ethics: Only for consented tests! Use test accounts only.
            server = smtplib.SMTP(os.getenv('EMAIL_HOST'), os.getenv('EMAIL_PORT'))
            server.starttls()  # Secure connection
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            server.quit()
            return "Email sent successfully! Check your inbox (and spam)."
        except Exception as e:
            return f"Error sending: {str(e)}"  # Debug help—don't expose in production!

    return render_template('send_form.html')  # Show form on GET (initial visit)

if __name__ == '__main__':  # This checks if we're running the file directly (not importing it)
    app.run(debug=True)  # Start the server in debug mode—auto-reloads on changes, shows errors nicely