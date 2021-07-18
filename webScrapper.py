from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# the url of the website we are going to be scrapping
my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'

# Opening up connection, grabbing the page then closing the connection
uClient = uReq(my_url)
page_html = uClient.read()


# Does my html parsing
page_soup = soup(page_html, 'html.parser')

# Grabs each product
containers = page_soup.findAll('div',{'class':'item-container'})

# writes to a file you can change txt to csv for excel
filename = 'products.txt'
f = open(filename, 'w')

headers = 'product_name, shipping\n'

f.write(headers)

# for loop to check if the tags are in the html
for container in containers:
    # finds brand in scrapper
    #brand = container.div.div.a.img['title']


    # finds the product name or title as you can see on the website
    title_container = container.findAll('a', {'class':'item-title'})
    product_name = title_container[0].text

    # finds the shipping price in the html
    shipping_container = container.findAll('li', {'class': 'price-ship'})
    if shipping_container == "Free Shipping":
        shipping = "Free Shipping"
    else:
        shipping = "Not free shipping"


    # prints the product name and shipping with price of shipping
    #print('brand: ' + brand)
    print('product: ' + product_name)
    print('Shipping: ' + shipping)

    # actually writes it then replaces the commas with pipe bars
    f.write(product_name.replace(',', '|') + ',' + shipping + '\n')

# closes the write file
f.close()
# closes the client
uClient.close()
