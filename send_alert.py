def send_job_alerts(jobs):
    if not jobs:
        print("No freshers job found today")
        return
    
    print("📢 Job Alert! Fresh Opportunities:\n")
    for job in jobs:
        print("Title:", job["title"])
        print("Company:", job["company_name"])
        print("Apply here:", job["url"])
        print("-" * 30)