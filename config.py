from dotenv import load_dotenv
import os

load_dotenv()

user = "modulo4"
password = "modulo4"
host = os.environ["HOST"]
database = os.environ["DATABASE"]
server = os.environ["SERVER"]

DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)