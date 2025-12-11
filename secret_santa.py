import random

def assign_pairs(names: list[str]) -> dict[str, str]:
    # Create a copy we can shuffle
    recipients = names[:]
    while True:
        random.shuffle(recipients)
        # Check for any self‑assignments
        if all(giver != receiver for giver, receiver in zip(names, recipients)):
            break   # We have a proper derangement
    return dict(zip(names, recipients))

def secret_santa(participants, keep_secret=True) -> None:
    if len(participants) < 2:
        raise ValueError("At least two participants are required.")
    pairs = assign_pairs(participants)
    if keep_secret:
        for giver, receiver in pairs.items():
            with open(f"{giver}.txt", "w") as f:
                f.write(f"You will be buying a gift for: {receiver}\n")
        print("Secret Santa assignments have been saved to individual files.")
        print("The name of the file corresponds to the giver's name.")
    else:
        for giver, receiver in pairs.items():
            print(f"{giver} → {receiver}")
        return pairs

# List participants here
participants = [
    "Bob", "Alice", "Charlie", "Diana", "Eve"
]

# Run the Secret Santa assignment
# Set keep_secret to False to print assignments directly
# If keep_secret is True, assignments will be saved to files
secret_santa(participants, keep_secret=True)
