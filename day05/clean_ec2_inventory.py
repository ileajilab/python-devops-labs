
# Day 5: Clean AWS EC2 Inventory
# Concepts: lists, dictionaries, sets, loops, CSV

import csv

# Sample messy EC2 inventory
instances = [
    {"id": "i-001", "type": "t3.medium", "environment": "PROD"},
    {"id": "i-002", "type": "t3.small", "environment": "dev"},
    {"id": "i-001", "type": "t3.medium", "environment": "prod"},
    {"id": "i-003", "type": "t3.large", "environment": " Prod "},
    {"id": "i-004", "type": "t3.micro", "environment": "DEV"},
    {"id": "i-002", "type": "t3.small", "environment": "DEV"},
    {"id": "i-005", "type": "t3.small", "environment": ""}
]

clean_instances = []
seen_ids = set()
duplicate_count = 0

print("===== EC2 INVENTORY CLEANING =====")

for instance in instances:

    # Normalize instance ID
    instance_id = instance["id"].strip()

    # Normalize environment name
    environment = instance["environment"].strip().lower()

    if environment == "":
        environment = "unknown"

    # Check for duplicate instance IDs
    if instance_id in seen_ids:
        print(f"Duplicate found: {instance_id}")
        duplicate_count += 1
        continue

    

    # Track unique instance IDs
    seen_ids.add(instance_id)

    # Create clean record
    clean_record = {
        "id": instance_id,
        "type": instance["type"].strip(),
        "environment": environment
    }

    clean_instances.append(clean_record)

# Print clean inventory
print("\n===== CLEAN INVENTORY =====")

for instance in clean_instances:
    print(instance)

# Export to CSV
with open("clean_ec2_inventory.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "type", "environment"]
    )

    writer.writeheader()
    writer.writerows(clean_instances)

# Cleaning summary
print("\n===== CLEANING SUMMARY =====")
print(f"Original Records: {len(instances)}")
print(f"Duplicates Removed: {duplicate_count}")
print(f"Clean Records: {len(clean_instances)}")
print("CSV Export: clean_ec2_inventory.csv")
print("============================")
