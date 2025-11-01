from flask import Flask, render_template  # Import Flask for web app, render_template for HTML pages

app = Flask(__name__)  # Create the app instance—think of this as starting your engine

@app.route('/')  # This decorator says: When someone visits the root URL (like localhost:5000/), run this function
def home():
    return render_template('index.html')  # Serve the index.html page from templates folder

if __name__ == '__main__':  # This checks if we're running the file directly (not importing it)
    app.run(debug=True)  # Start the server in debug mode—auto-reloads on changes, shows errors nicely