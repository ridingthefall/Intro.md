# Growth Marketing Example: Analyze user engagement

users = [
    {"name": "Alice", "engaged": True},
    {"name": "Bob", "engaged": False},
    {"name": "Charlie", "engaged": True},
]

# Count engaged users
engaged_count = sum(1 for user in users if user["engaged"])
total_users = len(users)
engagement_rate = engaged_count / total_users * 100

print(f"Engagement rate: {engagement_rate:.2f}%")
