import logging
from datetime import datetime

# Logging file configuration
# log_file_name = "loggFile.log"
# logging.basicConfig(filename=log_file_name, filemode='w',
#                     level=logging.INFO,
#                     format='%(asctime)s ################################## %(levelname)s ##################################\n%(message)s')


class Logging_Configuration:
    """
    to configure my owne logger
    """

    def __init__(self):
        self.run_time_stamp = datetime.now()
        self.string_timestamp = self.run_time_stamp.strftime("%Y%m%d_%H%M%S")
        self.logg_file_name = f"logg_data_{self.string_timestamp}.log"

    def conf(self):
        logging.basicConfig(filename=self.logg_file_name,
                            filemode='w',
                            level=logging.INFO,
                            format='%(asctime)s\n################################## %(levelname)s-START ################################\n%(message)s\n################################## %(levelname)s-END ##################################\n\n')
