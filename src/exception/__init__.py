import logging
import sys
from typing import Any


def error_message_detail(error: Exception, error_details: Any) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """
    # extract traceback details (exception information)
    _, _, exec_tb = error_details.exc_info()
    # Get the file name where exception occurred
    file_name = exec_tb.tb_frame.f_code.co_filename

    # create a formatted error message string
    error_message = f"Error occurred in python script name [{file_name}] line number [{exec_tb.tb_lineno}] error message [{str(error)}]"
    # Log the error for better tracking
    logging.error(error_message)
    return error_message


class MyException(Exception):
    """
    Custom exception class for handling errors in the US visa application.
    """

    def __init__(self, error_message: Exception, error_detail: Any):
        """
        Initializes the USvisaException with a detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback details.
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message
