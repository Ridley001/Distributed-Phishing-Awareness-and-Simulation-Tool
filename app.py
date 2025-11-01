from flask import Flask, render_template  # Import Flask for web app, render_template for HTML pages
from flask import request  # For handling form data later (we'll use this in future phases)

app = Flask(__name__)  # Create the app instance FIRST—think of this as starting your engine before driving

@app.route('/')  # This decorator says: When someone visits the root URL (like localhost:5000/), run this function
def home():
    return render_template('index.html')  # Serve the index.html page from templates folder

@app.route('/generate_email', methods=['GET'])  # New route for email preview—visit /generate_email to see it
def generate_email():
    # Simple template
    template = """
Subject: Urgent Account Update Required

Dear NSAILA RIDLEY,

We've detected unusual activity on your account. Click here to verify: https://x.com/

Best,
X Team (Formerly known as Twitter) 
    """
    # Replace placeholders with values— this makes it reusable (fix any typos like "knwon" to "known")
    email_content = template.format(name="Test User", link="http://localhost:5000/track_click?user_id=1")
    return f"<pre>{email_content}</pre>"  # Show as preformatted text in browser for preview (keeps formatting nice)

if __name__ == '__main__':  # This checks if we're running the file directly (not importing it)
    app.run(debug=True)  # Start the server in debug mode—auto-reloads on changes, shows errors nicely