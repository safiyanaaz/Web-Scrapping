from bs4 import BeautifulSoup as soup
import requests

my_url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

response=requests.get(my_url)

'''
uClient = uReq(my_url)                  #Establishing connection with server
page_html=uClient.read()                #loading complete html page in variable
uClient.close()                         #closing the connection
'''
#soup function will return all the htmlcontent of the page
page_soup=soup(response.content,features="html.parser")

containers= page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})
#print(len(containers))                          #finding no of products on the page

#print(soup.prettify(containers[3]))              #first product html content

#for only first product

container=containers[3]
#print(container.div.img["alt"])

price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})       #price class
#print(price[0].text)                                               #only price not tags thats'why .text

ratings=container.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)

features=container.findAll("div",{"class":"_3ULzGw"})
#print(features[0].text)

filename="products.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings,Features\n"

f.write(headers)

#for all the products

for container in containers[3:27]:

    product=container.div.img["alt"]

    price_container= container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text

    features_container = container.findAll("div", {"class": "_3ULzGw"})
    features=features_container[0].text.strip()


    print("product_name:"+product)
    print("price:" +price)
    print("ratings:" +rating)
    print("Features:" +features)

    trim_price=''.join(price.split(','))
    rm_rupee=trim_price.split("₹")
    add_rs_price="Rs." +rm_rupee[1]
    split_price=add_rs_price.split('E')
    final_price=split_price[0]

    split_rating=rating.split(",")
    final_rating=split_rating[0]

    print(product.replace(",","|")+","+final_price+","+final_rating+"," +features+ "\n")
    f.write(product.replace(",","|")+","+final_price+","+final_rating+","+features+"\n")

f.close()


