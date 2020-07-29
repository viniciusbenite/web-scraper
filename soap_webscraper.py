import requests
from bs4 import BeautifulSoup

# Very simple search news web scraper in TechReport main page using Beautiful Soup. 

def web_scraper(word, flag):
    URL = "https://techreport.com/"
    # Stores the data sent back by the server into a python variable
    page = requests.get(URL)

    # Get information about all news in homepage
    soup = BeautifulSoup(page.content, 'html.parser')
    all_results = soup.find_all('div', class_='wrapper clear-both group')
    for results in all_results:
        result = results.find_all('div', class_='recent-posts group')
        for rrr in result:
            if flag == 1:
                # Get all news
                rr = rrr.find_all('div', class_='post-content group')
                for r in rr:
                    r.find_all('h4', class_='post-title')
                    link = r.find('a')['href']
                    print(f"Link to news: {link}\n")
            else:
                # Get news with keyword
                string_search = rrr.find_all('h4', string=lambda text: word in text.lower())
                if len(string_search) > 0:
                    for string in string_search:
                            link = string.find('a')['href']
                            print(f"Link to news with keyword -> {word}: {link}\n")
                else:
                    print(f"Nothing found with keyword -> {word}")

   
def main():
    word = input("Enter the word to search (type 'all' for all news): ")
    print()
    if word == "all":
        web_scraper(word, flag=1)
    else:
        web_scraper(word, flag=0)


main()