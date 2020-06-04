from ZODB import FileStorage, DB 
import transaction 
from BTrees.OOBTree import BTree
from persistent import Persistent 
import getpass


class app_db(object): 
    def __init__(self, path='./Data.fs'): 
        self.storage = FileStorage.FileStorage(path) 
        self.db = DB(self.storage) 
        self.connection = self.db.open() 
        self.dbroot = self.connection.root() 
        
    def close(self): 
        self.connection.close() 
        self.db.close() 

db = app_db() 
dbroot = db.dbroot 
dbroot['User']=BTree() 
dbroot['Customer']=BTree()
dbroot['Admin']=BTree() 
dbroot['Shopping_Cart']=BTree() 
dbroot['Order']=BTree() 
dbroot['Shipping_Info']=BTree() 
dbroot['Product']=BTree()  
transaction.commit() 


class User(Persistent): 
    def __init__(self, userid, usertype, password,loginstatus,registration_date): 
        self.userid = userid 
        self.usertype = usertype 
        self.password = password
        self.loginstatus=loginstatus
        self.registration_date=registration_date

    def verifyLogin(self,user):
        if self.userid in user and self.password in user:
            return True
        else:
            print('Invalid user name and password combination entered. Please re-enter.')



class Customer(Persistent,User): 
    def __init__(self, CFName,CLName,address,CEmail,phoneno,CCNo, shippingAddress): 
        self.CFName = CFName 
        self.CLName = CLName
        self.address=address
        self.CEmail=CEmail
        self.phoneno=phoneno
        self.CCNo=CCNo
    
    def register(self,Customer):
        self.userid.append(Customer)
        self.password.append(Customer)
        self.usertype.append(Customer)
        self.CFName.append(Customer)
        self.CLName.append(Customer)
        self.CEmail.append(Customer)
        self.address.append(Customer)
        self.phoneno.append(Customer)
        self.registration_date.append(Customer)
        self._p_changed=1
    
    def login(self,Customer):
        userid=getpass.getpass('UserID:')
        password=getpass.getpass('Password:')
        if userid in Customer and password in Customer:
            Customer.loginstatus=True
            return 'Login Successful!'
        else:
            return 'Login Failed. Please retry!'
    
    def updateProfile(self,Customer):
        if Customer.loginstatus==True and Customer.userid in Customer:
            Customer.userid=self.userid
            Customer.CFName=self.CFName
            Customer.CLName=self.CLName
            Customer.CEmail=self.CEmail
            Customer.address=self.address
            Customer.phoneno=self.phoneno
        else:
            return 'Profile updation unsuccessful. Re-login to update profile'



class Admin(Persistent,User): 
    def __init__(self, adminName,email,phonenum,adminpwd,adminrole): 
        self.adminName = adminName 
        self.email = email
        self.phonenum=phonenum
        self.adminpwd=adminpwd
        self.adminrole=adminrole

    def updateCatelog(self,Admin):
        email=getpass.getpass('EmailID:')
        password=getpass.getpass('Password:')
        if email in Admin.email and password in Admin.password and Admin.adminrole=='Administrator':
            return 'Catalog updation accepted.'
        else:
            return 'You should be an administrator to update catalog'

class Product(Persistent): 
    def __init__(self, productId,productName,productCategory,cost,productQty): 
        self.productId = productId 
        self.productName = productName
        self.productCategory=productCategory
        self.cost=cost
        self.productQty=productQty
    
    def Product_details(self,Product):
        self.productId.append(Product)
        self.productName.append(Product)
        self.productQty.append(Product)
        self.cost.append(Product)
        self._p_changed=1



class Shopping_Cart(Persistent,Customer): 
    def __init__(self, cartId,category,quantity,dateAdded):
        self.cartId = cartId 
        self.category = category
        self.quantity=quantity
        self.dateAdded=dateAdded
    
    def addCartItem(self,Shopping_Cart):
        self.Shopping_Cart.append(Shopping_Cart)
        self._p_changed=1
    
    def updateQuantity(self,Shopping_Cart):
        self.quantity.append(Shopping_Cart)
        self._p_changed=1
    
    def viewCartDetails(self,Shopping_Cart):
        self.cartId.append(Shopping_Cart)
        self.category.append(Shopping_Cart)
        self.dateAdded.append(Shopping_Cart)
        self._p_changed=1
    
    def checkout(self,Shopping_Cart):
        if Shopping_Cart.viewCartDetails==True:
            return True
        else:
            'Cart missing items. Add items and retry checkout.'
        

class Order(Persistent,Customer): 
    def __init__(self, orderID,customerId,customerName,dateOfOrder,orderStatus,subTotal): 
        self.orderID = orderID 
        self.customerId = customerId
        self.customerName=customerName
        self.dateOfOrder=dateOfOrder
        self.orderStatus=orderStatus
        self.subTotal=subTotal
    
    def placeOrder(self,Order):
        if self.orderStatus=='Ordered':
            self.orderID.append(Order)
            self.customerId.append(Order)
            self.customerName.append(Order)
            self.dateOfOrder.append(Order)
            self.subTotal.append(Order)
            self._p_changed=1

class Shipping_Info(Persistent,Order): 
    def __init__(self, cartId,category,quantity,dateAdded): 
        self.cartId = cartId 
        self.category = category
        self.quantity=quantity
        self.dateAdded=dateAdded
    
    def updateShippingInfo(self,Shipping_Info):
        self.address.append(Shipping_Info)
        self.CCNo.append(Shipping_Info)
        self.dateOfOrder.append(Shipping_Info)
        self.customerId.append(Shipping_Info)
        self.customerName.append(Shipping_Info)
        self.CFName.append(Shipping_Info)
        self.CLName.append(Shipping_Info)
    


db = app_db() 
user = db.dbroot['User'] 
customer = db.dbroot['Customer']
admin=db.dbroot['Admin']
shopping_cart = db.dbroot['Shopping_Cart'] 
order = db.dbroot['Order']
shipping_info=db.dbroot['Shipping_Info']
product=db.dbroot['Product']

customer['1234']=customer('Yashaswi','Kavadapu','1467 Docksreet Rd','yashu.icy@gmail.com','737842','377448','1467 Dockstreet Rd')
customer['3435']=customer('Nikhil','Chowdary','124 Detroit','nikhil.gnc@gmail.com','73747','477474','Detroit')
customer['5634']=customer('Rama','Devi','1256 Detroit','rama.devi@gmail.com','23452','54632','36434','Detroit MI')
customer['167']=customer('Abhishek','Yengaldas','2727 Pleasantdale','aby.167@gmail.','35643','25632','','Detroit')
customer['2682']=customer('Shravanti','Reddy','12983 Proit','sreddy@gmail.com','283848','219485','Detroit')

admin['2354']=admin('Yashu Kavadapu','yashu@gmail.com','828839','nxdhnxhn','administrator')

product['483']=product('483','Table','Home and furniture','$235','2')
product['243']=product('243','Chocolate','Grocery','$5','20')
product['534']=product('534','Chair','Home and furniture','$120','6')
product['538']=product('538','Nike slides','Footwear','$25','2')
product['848']=product('848','T-shirt','Clothing and apparel','$35','3')


shopping_cart['928']=shopping_cart('928','Home accessories','10','28-01-2018')
shopping_cart['839']=shopping_cart('839','Grocery needs','20','18-01-2018')
shopping_cart['474']=shopping_cart('474','Clothing and apparel','5','03-02-2018')
shopping_cart['193']=shopping_cart('193','Home accessories','3','26-12-2017')
shopping_cart['182']=shopping_cart('182','Clothing and apparel','8','28-01-2018')


order['23']=order('23','1234','Yashaswi','23-01-2018','Ordered','$230')
order['25']=order('25','167','Abhishek','28-09-2017','Shipped','$290')
order['182']=order('182','3435','Nikhil','23-01-2018','Received','$130')
order['273']=order('273','2682','Shravanti','23-01-2018','Ordered','$129')
order['121']=order('121','5634','Rama','03-11-2017','Delivered','$200')

shipping_info['38']=shipping_info('38','Online-order','5','23-02-2018')
shipping_info['12']=shipping_info('12','Instore','3','18-02-2018')
shipping_info['19']=shipping_info('19','Store-pickup','1','17-02-2018')
shipping_info['11']=shipping_info('11','Instore','7','08-02-2018')
shipping_info['67']=shipping_info('67','Online-order','2','23-02-2018')

customer.register(customer)
customer.login(customer)
customer.updateProfile(customer)

user.verifyLogin(customer)

admin.updateCatelog(admin)

shopping_cart.addCartItem(shopping_cart)
shopping_cart.updateQuantity(shopping_cart)
shopping_cart.viewCartDetails(shopping_cart)
shopping_cart.checkout(shopping_cart)

product.Product_details(product)

order.placeOrder(order)

shipping_info.updateShippingInfo(shipping_info)


                                    #### OQL Queries ####

# Find the last name of customer whose customer id is '1234'

for i in db.dbroot.Customer['userid'].values():
    if(i=='1234'):
        print(Customer['CLName'])


# Find the total amount in the shopping cart under 'Home and furniture' category

sum=0

for i in db.dbroot.Product:
    if (i['ProductCategory']=='Home and furniture'):
        sum=sum+i['cost']
print(sum)


# Find order status of the customer whose user id is '167'

for i in db.dbroot.Customer['userid'].values():
    for j in db.dbroot.order['customerid'].values():
        if i==j==167:
            print(db.dbroot.order['orderstatus'])


# Find and verify the login for customer with customer id '3435'

user_name=input("Enter username:")
password=input("Enter password:")

for i in db.dbroot.User['userid'].values():
    if i==user_name and User['password']==password:
        print('Customer login credentials match!')
    else:
        print('Invalid login credentials.')


# Find the total 'online orders' from the shipping information

count=0

for i in db.dbroot.Shipping_Info.values():
    if i['OrderType']=='Online-order':
        count+=1
print(count)


# Find the Product name whose product id is 243

for i in db.dbroot.product['productid'].values():
    if i==243:
        print(product['productname'])

        
db.close()