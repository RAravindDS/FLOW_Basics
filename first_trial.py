import mlflow 


def calculate_nth_power(x, n): 
    return x ** n 

if __name__ == '__main__':
    with mlflow.start_run(): 
        x, n = 2, 32
        y = calculate_nth_power(2, 5)
        mlflow.log_param("x", x)
        mlflow.log_param("n", n)
        mlflow.log_metric("y", y)

""" Commands: mlflow ui"""