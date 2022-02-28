from ast import Str
from tokenize import String
from unicodedata import name
from fastapi import FastAPI, Path
from pydantic import BaseModel 

#create a fastapi object rfjhbrf 

app = FastAPI()


class Product(BaseModel):
    name:str
    price:float

#products dictionary contain list of products

products = {
    1:{
        "name":"Milk",
        "price":1.35
    },
    2:{
        "name":"Laptop",
        "price":1450
    },
    3:{
        "name":"Chocolate",
        "price":12
    }
}

#setup the root
#the method should return a dictionary
@app.get("/")
def home():
    return {'Name':'Aymen','LastName':'Moulehi'}



#get product name and price from id 
#gt and lt for max and min value for the id 
@app.get("/product/id={product_id}")
def product(product_id:int = Path(None,description="The value of the product id",gt=0)):
    return products[product_id]


#query parameter
@app.get("/product/get-by-name")
def product(product_name:str = None):
    for product_id in products:
        if products[product_id]["name"] == product_name:
            return products[product_id]
    return {"Data":"Not Found"}


#add product with post method
@app.post("/add-product/{product_id}")
def add_product(product_id:int,product:Product):
    if product_id in products:
        return{"Error":"Id product alreday exist"}
    products[product_id]={"name":product.name,"price":product.price}
    

