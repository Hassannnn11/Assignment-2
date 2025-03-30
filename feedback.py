"""
Feedback Class
This module contains  definition of the Feedback class 
for the Royal Stay Hotel Management System.
"""


class Feedback:
    """
    Represents feedback provided by a guest.
    """
    def __init__(self, feedback_id: int, rating: int, comments: str, date: str):
        """
        Initializes a Feedback object.

        : feedback_id: Unique ID of feedback
        : rating: Rating (1-5)
        : comments: Guest comments
        : date: Date of feedback
        """
        self._feedback_id = feedback_id
        self._rating = rating
        self._comments = comments
        self._date = date

    # Getters and Setters
    def get_feedback_id(self) -> int:
        return self._feedback_id

    def get_rating(self) -> int:
        return self._rating

    def get_comments(self) -> str:
        return self._comments

    def get_date(self) -> str:
        return self._date

    def __str__(self):
        """
        String representation of Feedback.
        """
        return f"Feedback ID: {self._feedback_id}, Rating: {self._rating}, Comments: {self._comments}, Date: {self._date}"
