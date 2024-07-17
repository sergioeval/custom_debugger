import logging
from datetime import datetime
import os


class Logging_Configuration:
    """
    to configure my owne logger
    logg_path parameter must end with /
    """

    def __init__(self, logg_path="./"):
        self.logg_path = logg_path
        self.run_time_stamp = datetime.now()
        self.string_timestamp = self.run_time_stamp.strftime("%Y%m%d_%H%M%S")
        self.logg_file_name = f"{self.logg_path}logg_data_{
            self.string_timestamp}.log"

    def conf(self):
        if not os.path.exists(self.logg_path):
            os.makedirs(self.logg_path)
        logging.basicConfig(filename=self.logg_file_name,
                            filemode='w',
                            level=logging.INFO,
                            format='%(asctime)s\n################################## %(levelname)s-START ################################\n%(message)s\n################################## %(levelname)s-END ##################################\n\n')
