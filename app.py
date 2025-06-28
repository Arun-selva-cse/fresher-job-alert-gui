import streamlit as st
import csv
import os
from fetch_job import fetch_fresher_jobs
from filters_job import filter_fresher_jobs
from send_whatsapp import send_whatsapp_alert

FAVORITES_FILE = "favorites.csv"
ALERTED_JOBS_FILE = "alerted_jobs.txt"

st.set_page_config(page_title="Fresher Job Alert App", layout="centered")

st.title("🚀 Fresher Job Alert GUI")
st.write("Get filtered fresher jobs with roles and locations of your choice.")

# Load previously alerted jobs to avoid duplicates
if os.path.exists(ALERTED_JOBS_FILE):
    with open(ALERTED_JOBS_FILE, "r") as file:
        alerted_jobs = set(file.read().splitlines())
else:
    alerted_jobs = set()

# Search input
company_filter = st.text_input("Search jobs by company name:").lower()

if st.button("Fetch Jobs"):
    jobs = fetch_fresher_jobs()
    filtered_jobs = filter_fresher_jobs(jobs)

    if company_filter:
        filtered_jobs = [job for job in filtered_jobs if company_filter in job["company_name"].lower()]

    st.success(f"Total Jobs Fetched: {len(jobs)}")
    st.info(f"Jobs after Filtering: {len(filtered_jobs)}")

    exported_jobs = []

    for job in filtered_jobs:
        job_id = f"{job['title']}@{job['company_name']}"

        if job_id in alerted_jobs:
            continue

        st.subheader(job["title"])
        st.text(f"Company: {job['company_name']}")
        st.markdown(f"[Apply Now]({job['url']})", unsafe_allow_html=True)

        if st.button(f"❤️ Save {job['title']}", key=job_id):
            with open(FAVORITES_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([job['title'], job['company_name'], job['url']])
            st.success("Added to favorites!")

        exported_jobs.append(job)
        alerted_jobs.add(job_id)

    # Export filtered jobs to CSV
    if exported_jobs:
        with open("filtered_jobs.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Company", "URL"])
            for job in exported_jobs:
                writer.writerow([job['title'], job['company_name'], job['url']])
        st.download_button(
            label="📥 Download Filtered Jobs as CSV",
            data=open("filtered_jobs.csv", "rb"),
            file_name="filtered_jobs.csv",
            mime="text/csv"
        )

    # Save updated alerted jobs
    with open(ALERTED_JOBS_FILE, "w") as file:
        file.write("\n".join(alerted_jobs))