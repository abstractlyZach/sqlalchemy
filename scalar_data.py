from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

with engine.connect() as con:
    rs = con.execute('select 5')

    data = rs.fetchone()[0]
    print('Data: {}'.format(data))
