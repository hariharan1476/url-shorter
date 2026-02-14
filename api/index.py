from flask import Flask, request, redirect, render_template
import string
import random

# IMPORTANT: template folder path
app = Flask(__name__, template_folder="../templates")

# In-memory storage (Vercel compatible)
url_map = {}

def generate_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        long_url = request.form["long_url"]
        short_code = generate_short()

        url_map[short_code] = long_url

        short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_url(short_code):

    if short_code in url_map:
        return redirect(url_map[short_code])

    return "URL not found"


# REQUIRED FOR VERCEL
def handler(request):
    return app
