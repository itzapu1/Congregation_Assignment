from FileReader import Reader
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime


class Deliver:
    """This class is set to only deliver the message to the target"""

    def __init__(self):
        read = Reader()
        self.data = read.read_spreadsheet()
        self.assignments = []

        pass

    def daily_assignment(self):
        # now = datetime.datetime.now() '%A, %B %d, %Y'
        today = date.today()
        day = today + timedelta(days=2)

        i = 0
        while i < 12:

            scheduled_row = self.data[i+1][0]
            row_data = self.data[i+1]
            i += 1
            scheduled_day = datetime.strptime(scheduled_row, '%A, %B %d, %Y').date()
            print(scheduled_day)
            if day == scheduled_day:
                break

        self.assignments = row_data
        pass

    def preferred_delivery_method(self):
        """capture data from the brothers"""


trial = Deliver()
trial.daily_assignment()
