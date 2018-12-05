from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcBo5-ZlZyY-TEiJjxlEBpnMUlPy_qeAwQDjkZGJqbmXBL9SzR9qc9WX-wyQ8_ULJfemRgJtoS5lmvX-DknVV34JV3AoKEJTdKhombm2sCS8547rPyRNQ2ImbO-SWCpi-tkIpjZC9qqI3ewynoRkeFVUN6Or97SxYbj9NeufbGk-j73tvPwSWibX6EFGFKDDD4-vUc'

def main():
    print("""""")
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()



