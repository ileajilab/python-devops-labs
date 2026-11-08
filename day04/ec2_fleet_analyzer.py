
# Day 4: AWS EC2 Fleet Cost Analyzer

HOURS_PER_MONTH_DAYS = 30
COST_THRESHOLD = 100

instances = [
    {
        "id": "i-001",
        "type": "t3.medium",
        "hourly_rate": 0.0416,
        "hours_per_day": 24,
        "environment": "PROD"
    },
    {
        "id": "i-002",
        "type": "t3.small",
        "hourly_rate": 0.0208,
        "hours_per_day": 8,
        "environment": "dev"
    },
    {
        "id": "i-003",
        "type": "t3.large",
        "hourly_rate": 0.0832,
        "hours_per_day": 24,
        "environment": " Prod "
    },
    {
        "id": "i-004",
        "type": "t3.micro",
        "hourly_rate": 0.0104,
        "hours_per_day": 8,
        "environment": "DEV"
    },
    {
    "id": "i-005",
    "type": "t3.small",
    "hourly_rate": 0.0208,
    "hours_per_day": 8,
    "environment": " DEV "
}
]

total_monthly_cost = 0
prod_total = 0
dev_total = 0

print("===== EC2 FLEET COST REPORT =====")

for instance in instances:

    # Clean inconsistent environment values
    environment = instance["environment"].strip().lower()

    # Calculate monthly cost
    monthly_cost = (
        instance["hourly_rate"]
        * instance["hours_per_day"]
        * HOURS_PER_MONTH_DAYS
    )

    total_monthly_cost += monthly_cost

    if environment == "prod":
        prod_total += monthly_cost
    elif environment == "dev":
        dev_total += monthly_cost

    print(f"\nInstance ID: {instance['id']}")
    print(f"Type: {instance['type']}")
    print(f"Environment: {environment}")
    print(f"Monthly Cost: ${monthly_cost:.2f}")

    if monthly_cost > COST_THRESHOLD:
        print("ALERT: High-cost instance")
    else:
        print("STATUS: Cost within threshold")

print("\n===== FLEET SUMMARY =====")
print(f"Total Instances: {len(instances)}")
print(f"Total Monthly Cost: ${total_monthly_cost:.2f}")
print("=========================")

print("\n===== ENVIRONMENT SUMMARY =====")
print(f"Production Cost: ${prod_total:.2f}")
print(f"Development Cost: ${dev_total:.2f}")
print("=========================")
