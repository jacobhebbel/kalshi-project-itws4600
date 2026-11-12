from misc.env import load_env

def bootstrap():
    load_env()

if '__main__' == __name__: 
    load_env(debug=True)