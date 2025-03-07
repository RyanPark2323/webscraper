import requests
from bs4 import BeautifulSoup

# Website info that we are scraping
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Parsing HTML
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

# Filter Out Jobs so only Python ones show up
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Print Our Results to See
for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")