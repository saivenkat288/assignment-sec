import yaml
from errors.traceback_exceptions import traceException

def yamlReader(file_loc):
    '''
    This function takes file location as an input and reads yaml file present
    in that location and returns you the contents present in yaml file in
    dictionary format
    '''
    try:
        with open(file_loc) as file:
            yaml_params = yaml.load(file, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print("ERROR:" ,exc)
        raise exc
    except Exception as e:
        traceException(e)

    return yaml_params