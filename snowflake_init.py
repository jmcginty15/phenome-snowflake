import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
with open("./rsa_key.txt", "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password='phcore'.encode(),
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

ctx = snowflake.connector.connect(
    user='PHENOME',
    account='qw95234.east-us-2.azure',
    private_key=pkb
)

cs = ctx.cursor()
