def average(numbers):
    if not numbers:
        return 0.0  # or raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)

print(average([]))
