email_text = input("Enter email content: ").lower()

suspicious_words = [
    "urgent",
    "verify your account",
    "click here",
    "password",
    "bank account",
    "login",
    "winner",
    "claim prize"
]

risk_found = False

for word in suspicious_words:
    if word in email_text:
        risk_found = True
        print("Suspicious keyword detected:", word)

if risk_found:
    print("\n⚠ Warning: This email may be a phishing or risky email.")
else:
    print("\n✅ Email appears safe.")