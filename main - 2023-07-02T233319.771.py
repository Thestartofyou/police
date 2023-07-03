import requests
from bs4 import BeautifulSoup

def scrape_police_reports(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing the police reports
        table = soup.find('table')
        
        # Iterate over the rows in the table
        for row in table.find_all('tr'):
            # Extract the data from each cell in the row
            cells = row.find_all('td')
            
            # Assuming the relevant information is in the first two cells (date and description)
            if len(cells) >= 2:
                date = cells[0].text.strip()
                description = cells[1].text.strip()
                
                # Process the event data here (e.g., store in a database, print, etc.)
                print(f"Date: {date}")
                print(f"Description: {description}")
                print("------------")
    else:
        print("Failed to retrieve the police reports.")

# URL of the website with the police reports
police_reports_url = 'https://www.example.com/police-reports'

# Call the function to scrape and process the police reports
scrape_police_reports(police_reports_url)

