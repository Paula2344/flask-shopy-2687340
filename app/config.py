class Config:
    #definir 'cadena de conexion'(connectionString)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin1234@localhost:3311/flask-shopy-2687340'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'fulvo'