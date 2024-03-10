import pandas as pd
import sqlite3
from clases.models import *
def TransformationOrders():
    conn=sqlite3.connect('./database.db')
    # lista de tablas
    list_tables=['food','menu','orders','restaurant','users']
    dict_dfs={}
    ## agrupar las tablas
    for i in list_tables:
        try:
            query = f"SELECT * FROM {i};"
            df=pd.read_sql(query,con=conn)
            dict_dfs[i]=df
        except:
                print("error al agregarr data frame",i)
    #### llamar funcion que realiza la union de data y filtrado(pregunta a responder )
    return merge_and_filters_data(dict_dfs)


def merge_and_filters_data(dict):
    df_user=dict['users']
    df_orders=dict['orders']
    df_restaurant=dict['restaurant']
    df_orders_user = pd.merge(df_orders, df_user, on='user_id', how='left')
    merged_df = pd.merge(df_orders_user, df_restaurant, left_on='r_id', right_on='id', how='left')
    # agrupamos ordernes por usuarios
    # esta linea cambia el reporte 
    data=merged_df.groupby(['user_id','Age'])['sales_amount'].agg(['mean']).reset_index()
    return data 



""" 
{
     'users':dfuser
     'orders':dforders
     
} 
## 
query limit SELECT * FROM {I} LIMIT 1500

"""