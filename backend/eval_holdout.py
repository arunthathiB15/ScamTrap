"""Second test set (different wording, Hinglish, and tricky legitimate messages). Rules only."""
import os; os.environ.pop("LLM_API_KEY", None)
from main import rule_analysis
SCAM = [
 "Hi mom this is my new number. My phone broke. Please send Rs 15000 urgently, I will explain later",
 "Aapka bijli connection aaj raat kat jayega. Abhi 9876500000 par call karein aur bill pay karein",
 "Sir your Paytm KYC is pending. Account will be closed. Click http://paytm-kyc.vip/update now",
 "Hello, I am from TRAI. Your number is used for illegal ads. Press 9 to talk to police officer or SIM blocked",
 "You have been selected for a part time job. Earn Rs 3000 per day. Send Rs 999 deposit to unlock tasks",
 "Dear customer, reward points worth Rs 8450 expire today. Redeem now at http://hdfc-rewards.top",
 "I am Major from army, selling my car cheap. Pay advance Rs 5000 on UPI to book, do not tell anyone",
 "Your Netflix subscription failed. Update card details and CVV immediately at http://netflix-billing.icu",
 "Invest in our IPO tips group, guaranteed double money in 15 days. Deposit minimum Rs 10000",
 "Courier executive: your package address is wrong. Confirm via http://bit.ly/courier-fix and pay Rs 30",
 "Sir I am calling from SBI. Your debit card is blocked. Tell me the OTP you just received to unblock",
 "Cyber crime branch notice: FIR registered against your Aadhaar. Pay fine today or you will be arrested",
 "Congratulations, you are our lucky winner of an iPhone. Pay Rs 299 shipping to claim your prize",
 "Download this apk to update your electricity bill details, otherwise connection will be suspended tonight",
 "Pay Rs 1 via this link to verify your account and get cashback of Rs 500: http://upi-cash.xyz/get",
]
SAFE = [
 "Your Swiggy order is on the way. Pay Rs 340 cash on delivery. Rider: Ramesh.",
 "Rs 2,300 credited to your account from RENT PAYMENT. Available balance Rs 18,240.",
 "Alert: Rs 1,200 debited at AMAZON PAY. Never share your OTP or PIN with anyone, including bank staff.",
 "Your electricity bill of Rs 840 is due on 15 Oct. Pay online through the official app to avoid late fee.",
 "Hi, I transferred Rs 2000 to your account for the movie tickets. Please check.",
 "Your KYC has been successfully updated. No further action required.",
 "Interview scheduled tomorrow at 11 am. Please carry your ID proof and resume.",
 "Mom: Call me when you reach home. Don't forget to take the medicines.",
 "Your IRCTC ticket PNR 4521896345 is confirmed. Train departs at 21:40 from Chennai Central.",
 "Please pay the hostel fee of Rs 45,000 by 20 October at the college accounts office or online portal.",
 "Your card ending 4417 was used for Rs 899 at ZOMATO. If not you, call the number on the back of your card.",
 "The police verification form is available at the passport seva kendra. Bring original documents.",
 "Reminder: your car insurance renews on 3 November. Renew through our official app or website.",
 "Congrats on the new job! Let's celebrate this weekend, dinner is on me.",
 "Your Jio recharge of Rs 299 is successful. Validity till 2 November.",
]
def run(show=True):
    miss = [t for t in SCAM if rule_analysis(t)[4] == "Looks safe"]
    fa = [t for t in SAFE if rule_analysis(t)[4] != "Looks safe"]
    n = len(SCAM) + len(SAFE); ok = n - len(miss) - len(fa)
    print(f"Holdout: correct {ok}/{n} ({100*ok//n}%). Scams caught {len(SCAM)-len(miss)}/{len(SCAM)}, safe passed {len(SAFE)-len(fa)}/{len(SAFE)}")
    if show:
        for t in miss: print("  missed scam ->", t)
        for t in fa: print("  false alarm ->", t)
if __name__ == "__main__": run()
