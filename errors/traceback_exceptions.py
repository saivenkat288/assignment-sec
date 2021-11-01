import sys

def traceException(exception):
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    print("ERROR: Exception : ", exception_type, exception)
    print("ERROR: File name: ", filename)
    print("ERROR: Line number: ", line_number)