def filter_fresher_jobs(jobs):
    fresher_keywords = ["fresher", "entry", "junior", "intern", "graduate", "trainee"]
    role_keywords = ["developer", "sql developer", "python developer", "data analyst", "associate engineer"]
    location_keywords = ["remote", "chennai", "bangalore", "mumbai", "hyderabad"]

    filtered = []
    seen_jobs = set()  # to avoid duplicates (using title + company)

    for job in jobs:
        title = job.get("title", "").lower()
        description = job.get("description", "").lower()
        company = job.get("company_name", "").lower()
        combined_text = title + " " + description

        print("Checking job:", title)

        if any(fk in combined_text for fk in fresher_keywords) and \
           any(rk in combined_text for rk in role_keywords):
            # Optional: Soft location filtering (do not block if not present)
            if any(loc in combined_text for loc in location_keywords):
                print("📍 Location matched")

            # Avoid duplicates
            unique_key = f"{title}_{company}"
            if unique_key not in seen_jobs:
                seen_jobs.add(unique_key)
                filtered.append(job)
            else:
                print("⚠️ Duplicate skipped:", title)

    return filtered