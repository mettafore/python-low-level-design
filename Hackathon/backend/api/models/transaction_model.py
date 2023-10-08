"""Classes representing a transaction."""
from enum import Enum

class TransactionStatus(Enum):
    """
    Enum class representing the status of a transaction.
    """
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    DISPUTED = "DISPUTED"
    RESOLVED = "RESOLVED"
    CANCELLED = "CANCELLED"
