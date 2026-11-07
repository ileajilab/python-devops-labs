# AWS EC2 Cost Calculator

hours_per_month = 730

def calculate_ec2_cost():
    print("===AWS EC2 Cost Calculator===")

    instance_type = input("Enter instance type: ")

    hourly_rate = float(input("Enter hourly rate: "))

    hours_per_day = float(input("Enter hours per day: "))

    instance_count = int(input("Enter number of instances: "))

    daily_cost = hourly_rate * hours_per_day * instance_count

    monthly_cost = daily_cost * 30
    yearly_cost = daily_cost * 365

    print("\n====== Cost Estimate ======")
    print(f"Instance type: {instance_type}")
    print(f"Instance Count: {instance_count}")
    print(f"Hourly rate: ${hourly_rate:.4f}")
    print(f"Hours per day: {hours_per_day}")    
    print(f"Daily cost: ${daily_cost:.2f}")
    print(f"Monthly cost: ${monthly_cost:.2f}")
    print(f"Yearly cost: ${yearly_cost:.2f}")
    print("=============================")


if __name__ == "__main__":
    calculate_ec2_cost()