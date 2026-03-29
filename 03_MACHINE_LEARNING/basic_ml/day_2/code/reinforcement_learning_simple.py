# Simplified concept example / مثال مبسط
state = 0
for step in range(5):
    action = step % 2  # choose action 0 or 1
    reward = 1 if action == 1 else -1
    print(f"Step {step}, Action {action}, Reward {reward}")