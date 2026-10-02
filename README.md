SWYNEX-Model-or-API-Integration

Fake Review Detection Prototype 🤖
Task: Integrate a Model, Library, or Public AI API into a Small Prototype

A small web-based prototype developed as part of the SWYNEX Technologies AI Internship Task to analyze customer reviews and identify potentially suspicious or fake reviews.

The prototype is designed around the B2B PET Bottle Review Intelligence System defined in the previous AI problem-design task.

📌 Project Overview

B2B businesses can receive a large number of customer and supplier reviews through different platforms and communication channels.

Manually checking every review can be time-consuming, especially when reviews contain:

Excessive promotional language
Repeated words
Too many exclamation marks
Highly exaggerated claims
Suspiciously positive statements

This prototype provides a simple automated approach to identify such patterns.

The user enters a review into the web application, and the system analyzes the text using predefined NLP-based rules and generates a Fake/Real classification with a score.

🎯 Objective

The main objective of this prototype is to demonstrate how review text can be automatically analyzed to assist a business analytics or quality team.

The prototype aims to:
Analyze review text automatically
Detect suspicious language patterns
Identify exaggerated promotional expressions
Calculate a suspicion/fake score
Classify the review as Potentially Fake or Potentially Real
Provide an easy-to-use web interface
🏭 B2B PET Bottle Use Case

The prototype is designed for a B2B PET bottle business environment.

For example, a company may receive reviews such as:

"PET bottle quality is excellent and delivery was on time."

or:

"This supplier is the BEST EVER!!! 100% AMAZING!!! MUST BUY!!!"

The system can flag reviews containing multiple suspicious patterns so that the Business Analytics Team or Quality Manager can review them further.

Possible business applications

1. Supplier Review Monitoring

Suspicious reviews can be flagged for additional verification before making supplier decisions.

2. Customer Feedback Analysis

Genuine reviews can help identify actual product or service issues such as:

Bottle quality
Leakage
Thickness
Packaging
Delivery delays
Supplier service

3. Brand Protection

The system can help identify unusually promotional or suspicious negative/positive reviews that require human verification.

⚙️ How the Prototype Works

The current prototype follows this workflow:

User enters review
        ↓
Text preprocessing
        ↓
Pattern analysis
        ↓
Suspicious keyword detection
        ↓
Excessive punctuation detection
        ↓
Exaggerated phrase detection
        ↓
Fake/Suspicion Score
        ↓
Final Classification
🧠 Detection Logic

The current prototype uses a rule-based NLP approach rather than a trained machine-learning model.

The system checks for patterns such as:

1. Excessive punctuation

Example:

Amazing product!!!
BEST EVER!!!

Multiple ! characters increase the suspicion score.

2. Exaggerated keywords

Examples include:

best ever
amazing
must buy
100% amazing
awesome supplier

These expressions can contribute to the suspicion score.

3. Repeated promotional language

For example:

Amazing amazing amazing!!!

Repeated promotional words can be treated as a suspicious pattern.

4. Final score

The detected patterns contribute to a total score.

Example:

Input:
This product is best ever!!! Amazing amazing must buy!!!

Output:
Potentially Fake
Score: 4
🖥️ Prototype Interface

The application provides a simple web interface where the user can enter a review and click "Check Karo".

Example interface:

🧪 Example Inputs and Outputs
Example 1 – Suspicious Review
Input
This product is best ever!!! Amazing amazing must buy!!!
Output
FAKE
Score: 4
Reason: Multiple suspicious promotional patterns detected
Example 2 – Normal Review
Input
Product quality is okay, delivery was late but works fine.
Output
REAL
Score: 0
Reason: No major suspicious patterns detected
Example 3 – B2B PET Bottle Review
Input
PET bottle quality is 100% best!!! Wow awesome supplier!!!
Output
FAKE
Score: 5
Reason: Exaggerated promotional language detected
🛠️ Technology Stack
Technology	Purpose
Python	Application logic
Flask	Web application framework
HTML	User interface
CSS	UI styling
Rule-based NLP	Review pattern analysis
📁 Project Structure
SWYNEX-Model-or-API-Integration/
│
├── app.py
├── README.md
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/

venv/ should not be uploaded to GitHub. Add it to .gitignore.

🚀 How to Run the Project
Step 1 – Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project folder:

cd SWYNEX-Model-or-API-Integration
Step 2 – Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
Step 3 – Install dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install Flask
Step 4 – Run the application
python app.py

You should see:

Running on http://127.0.0.1:5000

Open the address in your browser:

http://127.0.0.1:5000
🔐 API Key & Security

This project does not require a secret API key in its current implementation.

No passwords, API keys, tokens, or other credentials should be committed to the GitHub repository.

If a public AI API is integrated in a future version, credentials should be stored using environment variables such as:

.env

and the .env file should be added to:

.gitignore
📊 Current Prototype Limitations

This prototype is an initial proof of concept.

The current version uses predefined rules rather than a trained machine-learning model.

Therefore, it may not correctly identify:

Sarcasm
Complex fake-review behavior
Human writing variations
Sophisticated AI-generated reviews
Coordinated review manipulation
Context-dependent sentiment
Reviews written in multiple languages

The output should therefore be treated as a screening signal rather than a final decision.

🔮 Future Improvements

The prototype can be extended by integrating an actual NLP model or public AI API.

Possible future improvements include:

1. Sentiment Analysis

Classify reviews as:

Positive
Negative
Neutral
2. Review Type Classification

Classify reviews into categories such as:

Product Quality
Delivery
Packaging
Customer Service
Pricing
Supplier Experience
Other
3. AI-Based Fake Review Detection

A trained NLP/transformer model could be integrated to identify more complex suspicious patterns.

4. Confidence Score

Instead of only returning a score, the application could provide:

Prediction: Potentially Fake
Confidence: 92%
5. Dashboard

A future version could analyze hundreds of reviews and display:

Total reviews
Positive reviews
Negative reviews
Suspicious reviews
Review categories
Monthly trends
🎯 Expected Business Impact

A more advanced version of this system could help a B2B analytics team reduce the amount of manual review screening required.

It could support:

Review → Automated Analysis → Suspicious Review Flag → Human Verification → Business Decision

The system is intended to assist human decision-making rather than automatically reject a customer or supplier based on a single review.

📌 Task Connection

This prototype is a continuation of the previous SWYNEX AI problem-design task:

Previous Task

Define a Practical AI Problem and Success Criteria

Problem:

B2B PET Bottle Review Intelligence System

Current Task

Integrate a Model, Library, or Public AI API into a Small Prototype

This prototype demonstrates the first working stage of that system by taking review text as input and automatically analyzing it for suspicious patterns.

📈 Future System Architecture
                    B2B Customer Reviews
                            │
                            ▼
                     Review Input
                            │
                            ▼
                  NLP / AI Processing
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          Sentiment     Review Type    Fake Review
           Analysis      Detection      Detection
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                     Analysis Output
                            │
                            ▼
                 Business Analytics Team
                            │
                            ▼
                    Human Verification
👩‍💻 Developed By

Priyanka Baderia

Developed as part of an AI Internship Task provided by SWYNEX Technologies.

🏷️ Keywords
Artificial Intelligence
NLP
Natural Language Processing
Python
Flask
Fake Review Detection
B2B Analytics
PET Bottle Industry
Review Intelligence
AI Prototype
Text Classification
Data Analytics
⚠️ Ek cheez abhi karni zaroori hai

Tumhara UI prototype achha ban gaya hai, lekin SWYNEX ke task ke exact wording mein “model, library, or public AI API” maanga gaya hai.

Tumhare current code mein:

Rule-based NLP ≠ actual AI model/library/API integration

Isliye main suggest karunga ki isi existing Flask project ko waste na karke, ismein ek actual NLP model/library integrate karein. For example:

Review
   ↓
Hugging Face / Transformers model
   ↓
Sentiment prediction
   ↓
Fake-review rule/model analysis
   ↓
Flask UI
   ↓
Result
Review
   ↓
Hugging Face / Transformers model
   ↓
Sentiment prediction
   ↓
Fake-review rule/model analysis
   ↓
Flask UI
   ↓
Result
