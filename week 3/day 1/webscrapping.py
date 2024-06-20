import requests
from bs4 import BeautifulSoup
def fetch_and_parse(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return None
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
def extract_weather_info(soup):
    weather_info = {}
    # Example: Extract current temperature and weather condition
    temp = soup.find('div', class_='CurrentConditions--tempValue--3KcTQ').text.strip()
    condition = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text.strip()
    
    weather_info['Temperature'] = temp
    weather_info['Condition'] = condition
    
    return weather_info
def main():
    url = 'https://weather.com/weather/today/l/USCA0987:1:US'
    
    # Fetch and parse the web page
    soup = fetch_and_parse(url)
    if not soup:
        return
    
    # Extract weather information
    weather_info = extract_weather_info(soup)
    
    # Print the extracted weather information
    print("Current Weather Information:")
    print(f"Temperature: {weather_info['Temperature']}")
    print(f"Condition: {weather_info['Condition']}")
    
if __name__ == "__main__":
    main()
