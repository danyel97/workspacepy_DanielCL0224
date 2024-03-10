import pandas as pd
import os
import sqlite3
from migrations.init import getPathWithFileOrDir,quitar_extension

def loadData(dir):
    ruta=getPathWithFileOrDir(dir)
    print(ruta)
    files=os.listdir(ruta)
    print(files)
    for file in files:
        namefile=quitar_extension(file)
        ruta_to_csv=f"{ruta}/{file}"
        df=pd.read_csv(ruta_to_csv,sep=',')
        with sqlite3.connect('./database.db') as conn:
            df.to_sql(f'{namefile}',con=conn, index=False, if_exists='replace')
            print(f'data carga {namefile}')
    return 'se cargaron la data en la bd'