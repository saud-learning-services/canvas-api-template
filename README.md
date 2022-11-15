
#### First Time

1. Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed (Python 3.9 version)
2. Clone **{PROJECT}** repository
3. Import environment (once): `$ conda env create -f environment.yml`
4. Create .env file and include:

```
API_KEY = ''
API_URL = 'https://ubc.instructure.com'
```

#### Every Time

1. Run:
   1. navigate to your directory `$ cd YOUR_PATH/{PROJECT-NAME}`
   1. activate the environment (see step 3 on first run) `$ conda activate do-stuff`
   1. run the script and follow prompts in terminal `$ python src/do-stuff.py`


# Jupyter
Allow access to python files in src

```
import os
import sys
module_path = os.path.abspath(os.path.join('src/'))
if module_path not in sys.path:
    sys.path.append(module_path)
import my_app
```
