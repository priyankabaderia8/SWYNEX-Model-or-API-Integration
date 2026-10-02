from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<html>
<head>
<title>SWYNEX AI</title>
<style>
 body { font-family: 'Segoe UI'; background: #ffe6f2; text-align:center; padding: 20px; }
 .card { background: white; max-width: 500px; margin: auto; padding: 30px; border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
 h1 { color: #ff1493; }
 textarea { width: 100%; border: 2px solid #ffb6d9; border-radius: 15px; padding: 15px; font-size: 15px; }
 button { background: linear-gradient(90deg, #ff69b4, #ff1493); color: white; border: none; padding: 12px 30px; border-radius: 25px; font-size: 16px; cursor: pointer; margin-top:15px; font-weight:bold; }
 .result { margin-top:20px; padding:15px; border-radius:15px; font-weight:bold; font-size:18px; }
 .fake { background: #ffcccc; color: #cc0000; }
 .real { background: #ccffcc; color: #006600; }
 .char { font-size: 60px; }
</style>
</head>
<body>
 <div class="char">🤖✨💖</div>
 <h1>SWYNEX AI</h1>
 <p>Fake Review Detector - By You!</p>
 <div class="card">
   <p>👇 Yaha review likho Jaaneman 👇</p>
   <form method="POST">
     <textarea name="review" rows="4" placeholder="Ex: This product is best ever!!! Wow amazing..."></textarea><br>
     <button type="submit">✨ Check Karo ✨</button>
   </form>
   {% if result %}
   <div class="result {{cls}}">{{char}}<br>{{result}}</div>
   {% endif %}
 </div>
 <p style="margin-top:20px">Made with 💖 for SWYNEX</p>
</body>
</html>
"""

def check(review):
    low = review.lower()
    fake_words = ["best ever","must buy","amazing","awesome","100%","!!!","wow"]
    score = sum(1 for w in fake_words if w in low) + review.count("!")//2
    return score

@app.route("/", methods=["GET","POST"])
def home():
    result = None
    cls = ""
    char = ""
    if request.method == "POST":
        r = request.form.get("review","")
        s = check(r)
        if s >= 2:
            result = f"YE FAKE HAI! 😱 Score: {s}"
            cls = "fake"
            char = "🚨🤥"
        else:
            result = f"YE REAL HAI! ✅ Score: {s}"
            cls = "real"
            char = "🌸😊"
    return render_template_string(HTML, result=result, cls=cls, char=char)

if __name__ == "__main__":
    app.run(debug=True)
