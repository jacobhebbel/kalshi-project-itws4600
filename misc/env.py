import dotenv
import os

def load_env(debug=False):
    path = dotenv.find_dotenv()
    dotenv.load_dotenv(path)
    
    if debug:
        env = dotenv.dotenv_values()
        keys = '\n'.join([f'{key}=*********' 
                        if value is not None 
                        else f'{key}= NO VALUE FOUND' 
                        for key, value in env.items()
                        ])
        print(keys)

def read_env(key: str) -> str:

    value = os.getenv(key)
    if value is None: raise ValueError(f'ERROR: environment variable {key} is not found')

    return value