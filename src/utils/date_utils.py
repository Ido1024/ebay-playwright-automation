from datetime import datetime

class DateUtils:

    @staticmethod
    def get_current_date_time() -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")
