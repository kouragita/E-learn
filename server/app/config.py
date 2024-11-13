class Config:
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///e-learn.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://elearndb_user:ynYdjBgjF34gfqDJgmVGHKVvDNHu2XlU@dpg-csm7n0lumphs73ck0jj0-a.oregon-postgres.render.com/elearndb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False