from locust import HttpUser, task

class BookingAppUser(HttpUser):
    host = "http://localhost:5000"

    @task
    def index(self):
        """Test the homepage."""
        self.client.get("/")

    @task
    def valid_show_summary(self):
        """Test the showSummary route with valid data."""
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def valid_book_competition(self):
        """Test the book route."""
        self.client.get("/book/TEST/Simply%20Lift")

    @task
    def valid_purchase_places(self):
        """Test the purchasePlaces route."""
        self.client.post("/purchasePlaces", data={
            "competition": "TEST",
            "club": "Simply Lift",
            "places": 2
        })

    @task
    def points_board(self):
        """Test the pointsBoard route."""
        self.client.get("/pointsBoard")

    @task
    def logout(self):
        """Test the logout route."""
        self.client.get("/logout")