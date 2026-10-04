"""Accuracy check on a small hand-written test set (rules only). Run: python eval.py"""
import os; os.environ.pop("LLM_API_KEY", None)
from main import rule_analysis
SCAM = [
 "Dear customer your HDFC account is suspended. Update KYC now at http://bit.ly/hdfc-kyc or share OTP",
 "Congratulations! You won 25 lakh in lucky draw. Pay Rs 5000 processing fee to claim your prize today",
 "This is cyber police. Your Aadhaar is linked to money laundering. Stay on video call or you will be arrested",
 "Earn Rs 5000 daily work from home by liking videos. Pay registration fee Rs 500 to start. Join Telegram",
 "Your electricity will be disconnected tonight. Call officer 9876500000 and pay immediately",
 "Your parcel is held at customs. Pay Rs 49 fee at http://track-parcel.xyz within 2 hours",
 "Scan this QR code to receive your refund of Rs 4999. Enter UPI PIN to confirm",
 "Guaranteed 40% weekly returns. Join our private USDT trading group, deposit now",
 "Install AnyDesk so our executive can fix your account block urgently. Do not tell anyone",
 "Last warning: your SIM will be blocked in 1 hour. Share Aadhaar and OTP to keep it active",
 "Income tax refund pending. Click http://refund-gov.top and enter card number and CVV immediately",
 "Dear user your PAN card has expired. Pay Rs 200 to reactivate or face legal action today",
]
SAFE = [
 "Hi, are we still on for lunch at 1pm tomorrow? I will bring the class notes.",
 "Your OTP is 482913. Do not share it with anyone.",
 "Your Amazon order has been delivered. Rate your experience in the app.",
 "Reminder: dentist appointment on Friday at 10:30 am. Reply C to confirm.",
 "Your electricity bill for September has been paid. Thank you.",
 "Team meeting moved to 3pm today in room 204. Please bring your laptops.",
 "Your account statement for August is ready. Log in to the official app to view it.",
 "Happy birthday! Dinner at my place on Saturday, let me know if you can come.",
 "The assignment deadline has been extended to Monday. Submit through the college portal.",
 "Your offer letter is attached. Please sign and return by next week. No fees are involved.",
 "Rs 500 debited from your account at a grocery store. If this was you, no action is needed.",
 "Your flight is on time. Gate 14, boarding starts at 6:15 pm.",
]
bad = []
tp = sum(rule_analysis(t)[4] != "Looks safe" for t in SCAM)
tn = sum(rule_analysis(t)[4] == "Looks safe" for t in SAFE)
for t in SCAM:
    if rule_analysis(t)[4] == "Looks safe": bad.append(("missed scam", t))
for t in SAFE:
    if rule_analysis(t)[4] != "Looks safe": bad.append(("false alarm", t))
n = len(SCAM) + len(SAFE)
print(f"Correct {tp + tn}/{n} ({100*(tp+tn)//n}%). Scams caught {tp}/{len(SCAM)}, safe passed {tn}/{len(SAFE)}")
for k, t in bad: print(" ", k, "->", t)
