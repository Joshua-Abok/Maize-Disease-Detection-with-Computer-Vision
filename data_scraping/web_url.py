import requests 
from bs4 import BeautifulSoup

# Define the URL of the web page to scrape
url = "https://www.bing.com/images/search?view=detailv2&form=SBIHVR&lightschemeovr=1&iss=sbi&q=imgurl:https%3A%2F%2Finfonet-biovision.org%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Ffull_image_popup%2Fpublic%2Fplant_health%2Fpestsdiseasesweeds%2F1881_0.jpeg%3Fitok%3DRUN6bgC8&pageurl=https%3A%2F%2Finfonet-biovision.org%2FPlantHealth%2FPests%2Fafrican-maize-stalkborer%23expanded&pagetl=African+maize+stalkborer+%7C+Infonet+Biovision+Home.&imgalt=%3Cb%3EStemborer+damage+%3C%2Fb%3Eto+a+maize+plant.Note+the+caterpillar+and+its+frass+inside+the+split+stem&imgsz=753x565&selectedindex=0&id=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.519f6879dec040303782b14014d91e78%3Frik%3DRDNQKnQ%252bNLITfw%26riu%3Dhttp%253a%252f%252fwww.infonet-biovision.org%252fsites%252fdefault%252ffiles%252fplant_health%252fpestsdiseasesweeds%252f1881_0.jpeg%26ehk%3DGuWd9dI0RZxhQdOOh5fVc%252b5Kqgug3lEycHCAV1%252bcplM%253d%26risl%3D%26pid%3DImgRaw%26r%3D0&mediaurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.519f6879dec040303782b14014d91e78%3Frik%3DRDNQKnQ%252bNLITfw%26riu%3Dhttp%253a%252f%252fwww.infonet-biovision.org%252fsites%252fdefault%252ffiles%252fplant_health%252fpestsdiseasesweeds%252f1881_0.jpeg%26ehk%3DGuWd9dI0RZxhQdOOh5fVc%252b5Kqgug3lEycHCAV1%252bcplM%253d%26risl%3D%26pid%3DImgRaw%26r%3D0&exph=591&expw=418&vt=2&thid=OIP.UZ9oed7AQDA3grFAFNkeeAAAAA&sim=11"

# Send an HTTP GET request to the URL 
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200: 
    # Parse the HTML content of the page  
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all image tags on the page (based on the html structure)
    img_tags = soup.find_all("img")

    # Extract the src attribute (image URL) from each image tag 
    img_urls = [img['src'] for img in img_tags if "src" in img.attrs]

    # print the list of image URLs 
    for img_url in img_urls: 
        print(img_urls)
else:
    print(f"Failed to fetch data from {url}")
