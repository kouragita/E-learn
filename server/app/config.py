class Config:
    DEBUG = True 
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///e-learn.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://crowdsourceddb_user:Vs9zYCGoE353F8r70QBCJTlakGqkuqrt@dpg-cvj3f424d50c73c73pdg-a.oregon-postgres.render.com/crowdsourceddb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False