import requests
from datetime import datetime

def fetch_pull_request_data(repo_owner, repo_name, pr_number):
    # Construct the API URL to fetch pull request details
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    
    # Make GET request to the API endpoint
    response = requests.get(url)
    if response.status_code == 200:
        pr_data = response.json()
        pr_opened_at = pr_data['created_at']  # Timestamp when PR was opened
        pr_approved_at = pr_data['merged_at']  # Timestamp when PR was approved/merged
        return pr_opened_at, pr_approved_at
    else:
        raise Exception(f"Failed to fetch pull request data (status code: {response.status_code})")

def calculate_duration(pr_opened_at, pr_approved_at):
    # Convert ISO 8601 formatted strings to datetime objects
    opened_time = datetime.fromisoformat(pr_opened_at)
    approved_time = datetime.fromisoformat(pr_approved_at)

    # Calculate duration between opened and approved times
    duration = approved_time - opened_time

    return duration

if _name_ == "_main_":
    repo_owner = "your_username"
    repo_name = "your_repository"
    pr_number = "1"  # Replace with your pull request number
    

    pr_opened_at, pr_approved_at = fetch_pull_request_data(repo_owner, repo_name, pr_number)

  
    duration = calculate_duration(pr_opened_at, pr_approved_at)

    # Print the duration in days, hours, and minutes
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    print(f"Time taken for approval: {days} days, {hours} hours, {minutes} minutes")
