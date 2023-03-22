import sys
import logging

def error_message_detail(error,error_detail:sys):
    ##error details will be present inside the sys
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    ##exc_tb give information regarding file name and line number where error as occured
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


# if __name__=="__main__":
#     try:
#         a=1/v
#     except Exception as e:
#         logging.info("DIVIDE be zero")
#         raise CustomException(e,sys)