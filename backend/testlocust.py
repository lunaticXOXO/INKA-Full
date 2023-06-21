from locust import HttpUser,task,between


wait_time = between(2,5)
@task

class testLocust(HttpUser):
    def get_process(self):
        self.client.get(url = '/proses/get_listprocess')
        
    @task
    def get_operator(self):
        self.client.get(url='/operator/get_operator')

    @task
    def get_proyek(self):
        self.client.get(url='/proyek/get_allproyek')
        
    @task
    def get_rproyek(self):
        self.client.get(url ='/rproyek/show_rproyek')

    @task
    def get_product(self):
        self.client.get(url = '/product/get_product')
        
    
