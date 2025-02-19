from locust import HttpUser, task, between

class BookingAppUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 3)
    
    def on_start(self):
        self.client.post("/showSummary", data={'email': 'test@test.co'})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def valid_show_summary(self):
        """Test the showSummary route with valid data."""
        self.client.post("/showSummary", data={"email": "test@test.co"})

    @task
    def valid_book_competition(self):
        """Test the book route."""
        self.client.get("/book/TEST/test")

    @task
    def valid_purchase_places(self):
        """Test the purchasePlaces route."""
        self.client.post("/purchasePlaces", data={
            "competition": "TEST",
            "club": "test",
            "places": 2
        })

    @task
    def points_board(self):
        """Test the pointsBoard route."""
        self.client.get("/pointsBoard")
