from enum import Enum

class ReservationStatus(Enum):
    SCHEDULED = 'SCHEDULED'
    INPROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

# Example usage:
# reservation_status = ReservationStatus.SCHEDULED
