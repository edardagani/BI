from norm import *
from clean_tables import *
from etl import *
from data_warehouse import *
from auto_prof import *
from dimensions import *

# In case you want to run a process separately, comment out the rest and run the process alone
# or run it on their perspective files
if __name__ == '__main__':
    etl()
    normalize_tables()
    profile_tables()
    clean_tables()
    data_warehouse()
    create_dimensions()
