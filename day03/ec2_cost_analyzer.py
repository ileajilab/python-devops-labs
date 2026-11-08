def analyze_ec2_cost():
    print("=========EC2 Cost Analyzer=========")

    instance_type = input("EC2 instance type: ")
    hourly_rate = float(input("Hourly rate: "))
    instance_count = int(input("Number of instances: "))
    hours_per_day = float(input("Hours per day: "))
    monthly_budget = float(input("Monthly budget: "))

    monthly_cost = (
        hourly_rate * instance_count
        * hours_per_day * 30
    )

    print("\n===== Cost Report =====")
    print(f"Instance type: {instance_type}")
    print(f"Monthly cost: ${monthly_cost:.2f}")

    #Classify monthly spending
    if monthly_cost > 200:
        print("Spending level: HIGH")
    elif monthly_cost > 100:
        print("Spending level: MEDIUM")
    else:
        print("Spending level: LOW")

    # Check the monthly budget    
    if monthly_cost > monthly_budget:
        over_budget = monthly_cost - monthly_budget
        print("ALERT: Monthly budget exceeded!")
        print(f"Over budget by: ${over_budget:.2f}")
    else:
        print("STATUS: Within monthly budget")

    # Recommend Cost optimization    
    if hours_per_day == 24:
        print("TIP: Consider scheduling EC2 shutdowns")
        print("when instances are not needed")

    else:
        print("TIP: Limited runtime helps reduce costs.")

    print("==================")

    # optimization report
    print("\n===== Optimization Report =====")
    print(f"if hours_per_day: {hours_per_day}")

    current_monthly_cost = hourly_rate * instance_count * 24 * 30
    optimized_monthly_cost = hourly_rate * instance_count * hours_per_day * 30
    potential_savings = current_monthly_cost - optimized_monthly_cost

    print(f"Current monthly cost: ${current_monthly_cost:.2f}")
    print(f"Optimized monthly cost: ${optimized_monthly_cost:.2f}")
    print(f"Potential savings: ${potential_savings:.2f}")
    

if __name__ == "__main__":
    analyze_ec2_cost()