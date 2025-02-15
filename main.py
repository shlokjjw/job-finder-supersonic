import pandas as pd
from jobspy import scrape_jobs

# Scrape jobs
jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
    search_term="software engineer",
    google_search_term="software engineer jobs near Bangalore since yesterday",
    location="Bangalore",
    results_wanted=10,
    hours_old=72,
    country_indeed="india",
)

print(f"Found {len(jobs)} jobs")
print(jobs.head())
print(jobs.dtypes)

# Convert to DataFrame
df = pd.DataFrame(jobs)

# Select only required columns
df = df[["site", "job_url", "job_url_direct", "company", "location"]]

# Convert links to clickable hyperlinks
df["job_url"] = df["job_url"].apply(lambda x: f'=HYPERLINK("{x}", "Click Here")' if pd.notna(x) else "")
df["job_url_direct"] = df["job_url_direct"].apply(lambda x: f'=HYPERLINK("{x}", "Click Here")' if pd.notna(x) else "")

# Save as Excel with clickable links
df.to_excel("jobs.xlsx", index=False, engine="openpyxl")

print("Excel file with clickable links saved as jobs.xlsx")
