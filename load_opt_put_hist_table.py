import config
import pandas as pd
import glob
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, Numeric
from sqlalchemy.orm import sessionmaker

db_string = f"postgresql://postgres:{config.db_password}@127.0.0.1:5432/market_data"

db = create_engine(db_string)

Session = sessionmaker(db)  
session = Session()

Base = declarative_base()

class Opt_put_hist(Base):
    __tablename__ = 'opt_put_hist'
    
    id = Column(Integer, primary_key=True)
    contractSymbol = Column('contractSymbol',String)
    lastTradeDate = Column('lastTradeDate',DateTime)
    strike = Column('strike',Numeric)
    lastPrice = Column('lastPrice',Numeric)
    bid = Column('bid',Numeric)
    ask = Column('ask',Numeric)
    change = Column('change',Numeric)
    percentChange = Column('percentChange',Numeric)
    volume = Column('volume',Numeric)
    openInterest = Column('openInterest',Numeric)
    impliedVolatility = Column('impliedVolatility',Numeric)
    inTheMoney = Column('inTheMoney',Boolean)
    contractSize = Column('contractSize',String)
    currency = Column('currency',String)
    ticker = Column('ticker',String)
    call_put = Column('call_put',String)
    exp_date = Column('exp_date',DateTime)

    # def __repr__(self):
    #     return "<Stock_hist("date='%s')

Base.metadata.create_all(db)

filenames = glob.glob('Resources/opt_puts/*.csv')

for filename in filenames:
    file_name = f"{filename}"
    df = pd.read_csv(file_name)
    df.to_sql(name=Opt_put_hist.__tablename__, con=db, if_exists='append', index=False)


session = sessionmaker()
session.configure(bind=db)
s = session()

results = s.query(Opt_put_hist).all()
for r in results:
    print(r)

