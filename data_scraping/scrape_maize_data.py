import requests
from bs4 import BeautifulSoup
import os

# visualize the image
import matplotlib.pyplot as plt
from PIL import Image

# #URLs to scrape
# urls = [
#         "https://www.bing.com/images/search?view=detailv2&form=SBIHVR&lightschemeovr=1&iss=sbi&q=imgurl:https%3A%2F%2Finfonet-biovision.org%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Ffull_image_popup%2Fpublic%2Fplant_health%2Fpestsdiseasesweeds%2F1881_0.jpeg%3Fitok%3DRUN6bgC8&pageurl=https%3A%2F%2Finfonet-biovision.org%2FPlantHealth%2FPests%2Fafrican-maize-stalkborer%23expanded&pagetl=African+maize+stalkborer+%7C+Infonet+Biovision+Home.&imgalt=%3Cb%3EStemborer+damage+%3C%2Fb%3Eto+a+maize+plant.Note+the+caterpillar+and+its+frass+inside+the+split+stem&imgsz=753x565&selectedindex=0&id=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.519f6879dec040303782b14014d91e78%3Frik%3DRDNQKnQ%252bNLITfw%26riu%3Dhttp%253a%252f%252fwww.infonet-biovision.org%252fsites%252fdefault%252ffiles%252fplant_health%252fpestsdiseasesweeds%252f1881_0.jpeg%26ehk%3DGuWd9dI0RZxhQdOOh5fVc%252b5Kqgug3lEycHCAV1%252bcplM%253d%26risl%3D%26pid%3DImgRaw%26r%3D0&mediaurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.519f6879dec040303782b14014d91e78%3Frik%3DRDNQKnQ%252bNLITfw%26riu%3Dhttp%253a%252f%252fwww.infonet-biovision.org%252fsites%252fdefault%252ffiles%252fplant_health%252fpestsdiseasesweeds%252f1881_0.jpeg%26ehk%3DGuWd9dI0RZxhQdOOh5fVc%252b5Kqgug3lEycHCAV1%252bcplM%253d%26risl%3D%26pid%3DImgRaw%26r%3D0",
#     "https://www.bing.com/images/search?view=detailv2&form=SBIHVR&lightschemeovr=1&iss=sbi&q=imgurl:https%3A%2F%2Finfonet-biovision.org%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Ffull_image_popup%2Fpublic%2Fplant_health%2Fpestsdiseasesweeds%2F1881_0.jpeg%3Fitok%3DRUN6bgC8&pageurl=https%3A%2F%2Finfonet-biovision.org%2FPlantHealth%2FPests%2Fafrican-maize-stalkborer%23expanded&pagetl=African+maize+stalkborer+%7C+Infonet+Biovision+Home.&imgalt=%3Cb%3EStemborer+damage+%3C%2Fb%3Eto+a+maize+plant.Note+the+caterpillar+and+its+frass+inside+the+split+stem&imgsz=753x565&selectedindex=15&id=943624FCC1984C5FE8965DC8E2F55B6333BD6FF0&mediaurl=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FBoukria-Dawoud%2Fpublication%2F348714298%2Ffigure%2Fdownload%2Ffig3%2FAS%3A983171193663499%401611417687632%2FEuropean-corn-borer-pests-of-corn.png&exph=600&expw=800&vt=2&thid=OIP.-BvqG8MaJbB-84N2jTEOdQHaFj&sim=11&ccid=%2BBvqG8Ma&simid=608017355077081613&ck=05C941BC6DF81721B827D2CB47BFA9CA&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.f81bea1bc31a25b07ef383768d310e75%3Frik%3D8G%252b9M2Nb9eLIXQ%26pid%3DImgRaw%26r%3D0",
#     "https://www.bing.com/images/search?view=detailv2&form=SBIHVR&lightschemeovr=1&iss=sbi&q=imgurl:https%3A%2F%2Finfonet-biovision.org%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Ffull_image_popup%2Fpublic%2Fplant_health%2Fpestsdiseasesweeds%2F1881_0.jpeg%3Fitok%3DRUN6bgC8&pageurl=https%3A%2F%2Finfonet-biovision.org%2FPlantHealth%2FPests%2Fafrican-maize-stalkborer%23expanded&pagetl=African+maize+stalkborer+%7C+Infonet+Biovision+Home.&imgalt=%3Cb%3EStemborer+damage+%3C%2Fb%3Eto+a+maize+plant.Note+the+caterpillar+and+its+frass+inside+the+split+stem&imgsz=753x565&selectedindex=30&id=11E5487AE92A9E384CED01CF0B7A8FFD811ECDDB&mediaurl=https%3A%2F%2Fwww.kwayedza.co.zw%2Fwp-content%2Fuploads%2Fsites%2F28%2F2016%2F02%2Fchibage.jpg&exph=296&expw=474&vt=2&thid=OIP.W52ft7RdOOVgdzBQGLU87wAAAA&sim=11&ccid=W52ft7Rd&simid=608002906779839491&ck=C8F6F0EAAC7013CE1B6E4150CD518CBF&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.5b9d9fb7b45d38e56077305018b53cef%3Frik%3D280egf2PegvPAQ%26pid%3DImgRaw%26r%3D0",
# ]

# Read URLs from a text file 
with open("image_urls.csv", "r") as file: 
    urls = file.read().splitlines()

# Create a directory to save the images 
os.makedirs("images", exist_ok=True)

for url in urls: 
    response = requests.get(url)
    if response.status_code == 200:
        # parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the image element
        img_tag = soup.find("img")
        # get the image source url 
        img_url = img_tag.get("src")
        # download and save the image
        img_data = requests.get(img_url).content

        with open(f"images/{os.path.basename(img_url)}", "wb") as f:
            f.write(img_data)
        print(f"downloaded: {os.path.basename(img_url)}")
    else:
        print(f"Failed to fetch data from {url}")

print("Data scraping and image downloading completed.")


# #Load the image using PIL 
# image_path = "images/R.519f6879dec040303782b14014d91e78?rik=RDNQKnQ%2bNLITfw&riu=http%3a%2f%2fwww.infonet-biovision.org%2fsites%2fdefault%2ffiles%2fplant_health%2fpestsdiseasesweeds%2f1881_0.jpeg&ehk=GuWd9dI0RZxhQdOOh5fVc%2b5Kqgug3lEycHCAV1%2bcplM%3d&risl=&pid=ImgRaw&r=0"
# img = Image.open(image_path)

# # Display the image using Matplotlib
# plt.imshow(img)
# plt.axis('off')  #Hide the axis
# plt.show()