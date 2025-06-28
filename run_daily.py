from fetch_job import fetch_fresher_jobs
from filters_job import filter_fresher_jobs
from send_whatsapp import send_whatsapp_alert

def job_alert_task():
    print("📢 Running job alert task...")

    jobs = fetch_fresher_jobs()
    print(f"✅ Total jobs fetched: {len(jobs)}")

    fresher_jobs = filter_fresher_jobs(jobs)
    print(f"✅ Jobs after filtering: {len(fresher_jobs)}")

    for job in fresher_jobs[:10]:
        print(f"📨 Sending WhatsApp alert for: {job['title']} at {job['company_name']}")
        try:
            send_whatsapp_alert(job)
        except Exception as e:
            print(f"❌ Failed to send WhatsApp alert: {e}")

job_alert_task()
