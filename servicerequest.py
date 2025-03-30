
"""
ServiceRequest Class 
This module contains the definition of the ServiceRequest class 
"""


class ServiceRequest:
    """
    Represents a service request made by a guest during their booking.
    """

    def __init__(self, request_id: int, service_type: str, request_date: str, status: str = "Pending"):
        """
        Initializes a ServiceRequest object.

        : request_id: Unique ID of the service request
        : service_type: Type of service requested
        : request_date: Date of the request
        : status: Status of request (default is 'Pending')
        """
        self._request_id = request_id
        self._service_type = service_type
        self._request_date = request_date
        self._status = status

    # Getters and Setters
    def get_request_id(self) -> int:
        return self._request_id

    def get_service_type(self) -> str:
        return self._service_type

    def get_request_date(self) -> str:
        return self._request_date

    def get_status(self) -> str:
        return self._status

    def update_status(self, status: str):
        """
        Updates the status of the service request.
        """
        self._status = status

    def __str__(self):
        """
        String representation of ServiceRequest.
        """
        return f"Request ID: {self._request_id}, Service: {self._service_type}, Date: {self._request_date}, Status: {self._status}"
