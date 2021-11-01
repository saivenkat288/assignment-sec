import json
from errors.traceback_exceptions import traceException

def jsonReader(file_loc):
    '''
    This function takes file location as an input and returns you the
    contents present inside json file
    '''
    try:
        with open(file_loc) as f:
            config = json.load(f)
    except Exception as e:
        traceException(e)
    return config