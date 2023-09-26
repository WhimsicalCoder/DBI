import datetime

# Function to calculate the cost per mille (CPM)
def calculate_cpm(budget, impressions):
    return (budget / impressions) * 1000

# Function to calculate budget and impression pacing
def calculate_pacing(current_spend, current_impressions, start_date, end_date, total_budget, booked_impressions):
    current_date = datetime.datetime.now()
    days_elapsed = (current_date - start_date).days
    days_remaining = (end_date - current_date).days
    budget_spent = current_spend
    impressions_delivered = current_impressions

    remaining_budget = total_budget - budget_spent
    remaining_impressions = booked_impressions - impressions_delivered
    daily_budget = remaining_budget / days_remaining
    daily_impressions = remaining_impressions / days_remaining

    return remaining_budget, remaining_impressions, daily_budget, daily_impressions

# User input
campaign_name = input("Campaign Name: ")
total_budget = float(input("Total Budget: $"))
booked_impressions = float(input("Booked Impressions: "))
start_date = datetime.datetime.strptime(input("Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
end_date = datetime.datetime.strptime(input("End Date (YYYY-MM-DD): "), "%Y-%m-%d")

# Calculate CPM
cpm = calculate_cpm(total_budget, booked_impressions)

print(f"Cost Per Mille (CPM): ${cpm:.2f}")

while True:
    current_spend = float(input("Current Spend: $"))
    current_impressions = float(input("Current Impressions: "))

    remaining_budget, remaining_impressions, daily_budget, daily_impressions = calculate_pacing(
        current_spend, current_impressions, start_date, end_date, total_budget, booked_impressions)

    print(f"Remaining Budget: ${remaining_budget:.2f}")
    print(f"Remaining Impressions: {remaining_impressions}")
    print(f"Daily Budget Pacing: ${daily_budget:.2f}")
    print(f"Daily Impression Pacing: {daily_impressions}")

    continue_input = input("Do you want to input more data (Y/N)? ").strip().lower()
    if continue_input != "y":
        break
