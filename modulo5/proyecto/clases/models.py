class food:
    f_id:str
    item:str
    veg_or_non_veg:str
    def __init__(self):
        self.items_bd = list(self.__annotations__.keys())

class menu:
    menu_id:str
    r_id:str
    f_id:str
    cuisine:str
    price:str
    def __init__(self):
        self.items_bd = list(self.__annotations__.keys())

class orders:
    order_date:str
    sales_qty:str
    sales_amount:float
    currency:str
    user_id:str
    r_id:str
    def __init__(self):
        self.items_bd = list(self.__annotations__.keys())

class restaurant:
    id:int
    name:str
    city:str
    rating:float
    rating_count:str
    cost:str
    cuisine:str
    lic_no:str
    link:str
    address:str
    menu:str
    def __init__(self):
        self.items_bd = list(self.__annotations__.keys())

class user:
    user_id:int
    name:str
    email:str
    password:str
    Age:int
    Gender:str
    MaritalStatus:str
    Ocupation:str
    Monthly_Income:str
    Educational_Qualifications:str
    Family_Size:str
    def __init__(self):
        self.items_bd = list(self.__annotations__.keys())


