import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_fresher_jobs():
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1?app_id={app_id}&app_key={app_key}&results_per_page=20&what=graduate&content-type=application/json"

    response = requests.get(url)
    jobs = []

    if response.status_code == 200:
        data = response.json()
        for item in data.get("results", []):
            job = {
                "title": item.get("title", ""),
                "company_name": item.get("company", {}).get("display_name", ""),
                "url": item.get("redirect_url", ""),
                "description": item.get("description", "")
            }
            jobs.append(job)
    else:
        print(f"❌ Error fetching jobs: {response.status_code}")

    return jobs