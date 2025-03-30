
class LoyaltyAccount:
    """
    Represents a Loyalty Account associated with a Guest.
    """

    def __init__(self, points: int, membership_status: str):
        """
        Initializes a LoyaltyAccount object.

        : points: Loyalty points
        : membership_status: Membership status
        """
        self._points = points
        self._membership_status = membership_status

    # Getters and Setters
    def get_points(self) -> int:
        return self._points

    def set_points(self, points: int):
        self._points = points

    def get_membership_status(self) -> str:
        return self._membership_status

    def set_membership_status(self, status: str):
        self._membership_status = status

    # Functional methods
    def add_points(self, points: int):
        self._points += points

    def redeem_points(self, points: int):
        if points <= self._points:
            self._points -= points
        else:
            raise ValueError("Not enough points to redeem.")

    def __str__(self):
        return f"Loyalty Points: {self._points}, Status: {self._membership_status}"
