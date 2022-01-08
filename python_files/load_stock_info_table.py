#8.2.1 Importing dependancies and setting directory
from sqlalchemy.util.langhelpers import symbol
import config
import pandas as pd
import numpy as np

#9.5.1 - Set Up the Database
#8.5.1 loading SQL Database
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.ext.automap import automap_base

#8.5.1 Create the Database Engine
db_string = f"postgresql://postgres:{config.db_password}@127.0.0.1:5432/market_data"
db = create_engine(db_string)

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Stock_info(Base):
    __tablename__ = 'stock_info'
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    company = Column(String)

    def __repr__(self):
        return "<Stock_info(symbol='%s', company='%s')>" % (self.symbol, self.company)

Base.metadata.create_all(db)

file_name = 'Resources/_DJIA.csv'

df = pd.read_csv(file_name)

df.to_sql(name=Stock_info.__tablename__, con=db, if_exists='append', index=False)

session = sessionmaker()
session.configure(bind=db)
s = session()

results = s.query(Stock_info).all()
for r in results:
    print(r)

#DB = 'market_data'

# Table 1 = 'stock_info'
# Symbol ---> String, Primary Key
# Company ---> String



# Table 3 = 'option_chains'
# ID ---> Primary Key

# Table 4 = 'interest_rates'
# ID ---> Primary Key
# Date ---> 

