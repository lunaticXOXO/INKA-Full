from locust import HttpUser,task,between

class SupplierTest(HttpUser):
    wait_time = between(2,5)

    @task
    def add_penghitung(self):
        response = self.client.post(url = '/supplier/add_admin_penghitung',
                    json={ 
                        "idPenghitung" : "PG02",
                        "namaPenghitung" : "aj",
                        "tglPenghitung" : "2023-06-23"

        })
        json_var = response.json()