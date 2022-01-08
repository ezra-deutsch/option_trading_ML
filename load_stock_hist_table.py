import config
import pandas as pd
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime, Integer, Numeric
from sqlalchemy.orm import sessionmaker

db_string = f"postgresql://postgres:{config.db_password}@127.0.0.1:5432/market_data"

db = create_engine(db_string)

Session = sessionmaker(db)  
session = Session()

Base = declarative_base()

class Stock_hist(Base):
    __tablename__ = 'stock_hist'
    
    id = Column(Integer, primary_key=True)
    date = Column('Date',DateTime)
    open = Column('Open',Numeric)
    high = Column('High',Numeric)
    low = Column('Low',Numeric)
    close = Column('Close',Numeric)
    volume = Column('Volume',Numeric)
    dividends = Column('Dividends',Numeric)
    stock_splits = Column('Stock Splits',Numeric)
    symbol =  Column(String)

    # def __repr__(self):
    #     return "<Stock_hist("date='%s')

Base.metadata.create_all(db)

tickers = ['AAPL','AMGN','AXP','BA','CAT','CRM','CSCO','CVX','DIS','DOW',
            'GS','HD','HON','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MRK','MSFT',
            'NKE','PG','TRV','UNH','V','VZ','WBA','WMT']

for ticker in tickers:
    file_name = f"Resources/stock_hist/{ticker}.csv"
    df = pd.read_csv(file_name)
    df.to_sql(name=Stock_hist.__tablename__, con=db, if_exists='append', index=False)


session = sessionmaker()
session.configure(bind=db)
s = session()

results = s.query(Stock_hist).all()
for r in results:
    print(r)


