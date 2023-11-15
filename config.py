from dotenv import load_dotenv
import os

load_dotenv()

user = "modulo4"
password = "modulo4"
host = "137.184.120.127"
database = "sigcon"
server = "postgresql"

DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)