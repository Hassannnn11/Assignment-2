"""
Invoice Class 
This module contains definition of the Invoice class 
"""


class Invoice:
    """
    Represents an invoice generated for a booking.
    """

    def __init__(self, invoice_id: int, amount: float, payment_method: str, discount_applied: float = 0.0):
        """
        Initializes an Invoice object.

        : invoice_id: Unique ID of the invoice
        : amount: Total amount of the invoice
        : payment_method: Payment method used
        : discount_applied: Discount applied (default 0.0)
        """
        self._invoice_id = invoice_id
        self._amount = amount
        self._payment_method = payment_method
        self._discount_applied = discount_applied

    # Getters and Setters
    def get_invoice_id(self) -> int:
        return self._invoice_id

    def get_amount(self) -> float:
        return self._amount

    def get_payment_method(self) -> str:
        return self._payment_method

    def get_discount_applied(self) -> float:
        return self._discount_applied

    def __str__(self):
        """
        String representation of Invoice.
        """
        return f"Invoice ID: {self._invoice_id}, Amount: {self._amount}, Payment Method: {self._payment_method}, Discount: {self._discount_applied}"
