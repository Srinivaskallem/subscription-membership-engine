from datetime import datetime, timedelta

class SubscriptionTier:
    def __init__(self, name, price, features, duration_days):
        self.name = name
        self.price = price
        self.features = features
        self.duration_days = duration_days

class User:
    def __init__(self, username, tier):
        self.username = username
        self.tier = tier
        self.start_date = datetime.now()
        self.expiry_date = self.start_date + timedelta(days=tier.duration_days)
        self.active = True

    def check_expiry(self):
        if datetime.now() > self.expiry_date:
            self.active = False
        return self.active

    def upgrade(self, new_tier):
        print(f"\n🔄 {self.username} upgrading from {self.tier.name} to {new_tier.name}")
        self.tier = new_tier
        self.start_date = datetime.now()
        self.expiry_date = self.start_date + timedelta(days=new_tier.duration_days)
        self.active = True

    def access_feature(self, feature):
        if not self.check_expiry():
            print("❌ Subscription Expired!")
            return

        if feature in self.tier.features:
            print(f"✅ Access Granted to {feature}")
        else:
            print(f"⛔ Access Denied to {feature}")

    def show_details(self):
        print("\n===== USER DETAILS =====")
        print("Username:", self.username)
        print("Tier:", self.tier.name)
        print("Price: $", self.tier.price)
        print("Features:", self.tier.features)
        print("Start Date:", self.start_date.strftime("%Y-%m-%d"))
        print("Expiry Date:", self.expiry_date.strftime("%Y-%m-%d"))
        print("Active:", self.check_expiry())
        print("=========================")


# Define Subscription Tiers
free = SubscriptionTier("Free", 0, ["Basic Access"], 30)
silver = SubscriptionTier("Silver", 10, ["Basic Access", "Reports"], 30)
gold = SubscriptionTier("Gold", 25, ["Basic Access", "Reports", "Analytics"], 30)
platinum = SubscriptionTier("Platinum", 50, ["Basic Access", "Reports", "Analytics", "Priority Support"], 30)


# ---------------- SIMULATION ----------------

print("🚀 Subscription Engine Simulation Started")

user1 = User("john_doe", free)

user1.show_details()
user1.access_feature("Reports")

user1.upgrade(gold)
user1.show_details()

user1.access_feature("Analytics")
user1.access_feature("Priority Support")

print("\n🎉 Simulation Completed")
