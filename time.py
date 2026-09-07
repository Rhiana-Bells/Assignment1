from datetime import datetime
from collections import Counter

def find_peak_usage(logs):
    """
    Determines the hour of the day (0-23) with the highest volume of logins.

    Parameters:
        logs (list of str): List of ISO-formatted timestamp strings,
                             e.g., "2026-08-04T13:21:18"

    Returns:
        int: The peak hour (0-23). If there is a tie, the earliest hour is returned.
    """
    if not logs:
        return None  # No logs to process

    hour_counts = Counter()

    for timestamp in logs:
        dt = datetime.fromisoformat(timestamp)
        hour_counts[dt.hour] += 1

    # Find the maximum count value
    max_count = max(hour_counts.values())

    # Among hours with the max count, return the smallest (earliest) hour
    peak_hour = min(hour for hour, count in hour_counts.items() if count == max_count)

    return peak_hour


# ---------- Example usage / test ----------
if __name__ == "__main__":
    logs = [
        "2026-08-04T13:21:18",
        "2026-08-04T13:45:02",
        "2026-08-04T09:10:00",
        "2026-08-04T09:59:59",
        "2026-08-04T14:00:00",
        "2026-08-04T14:30:00",
        "2026-08-05T09:05:00",   # another login in hour 9, across a different day
    ]

    peak = find_peak_usage(logs)
    print(f"Peak usage hour: {peak}:00")