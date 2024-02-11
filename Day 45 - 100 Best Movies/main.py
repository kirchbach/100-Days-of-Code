from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

data = response.text

soup = BeautifulSoup(data, "html.parser")

headings = soup.find_all(name="img")

heading_list = [heading.get("alt") for heading in headings]

del heading_list[0:12]
heading_list.remove("Facebook")
heading_list.remove("Twitter")
heading_list.remove("Pinterest")

heading_list.reverse()



with open("100_movies.txt", "w") as file:
    for item in heading_list:
        file.write(f"{heading_list.index(item)+1} {item}\n")