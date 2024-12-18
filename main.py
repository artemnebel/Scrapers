import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://weworkremotely.com/remote-jobs"

# Send GET request to the website
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract job listings
    jobs = soup.find_all('li', class_='feature')  # 'feature' class holds job listings

    # Prepare lists for data
    titles = []
    companies = []
    links = []

    for job in jobs:
        # Extract job title
        title = job.find('span', class_='title').text.strip() if job.find('span', class_='title') else "N/A"
        # Extract company name
        company = job.find('span', class_='company').text.strip() if job.find('span', class_='company') else "N/A"
        # Extract job link
        link = job.find('a')['href'] if job.find('a') else "N/A"
        full_link = f"https://weworkremotely.com{link}"  # Complete the relative link

        # Append to lists
        titles.append(title)
        companies.append(company)
        links.append(full_link)

    # Create a DataFrame
    data = pd.DataFrame({
        'Title': titles,
        'Company': companies,
        'Link': links
    })

    # Save to CSV
    data.to_csv('remote_jobs.csv', index=False)
    print("Scraping complete! Data saved to remote_jobs.csv.")
else:
    print(f"Failed to fetch job listings. Status code: {response.status_code}")