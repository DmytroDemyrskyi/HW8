import time


def log_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        execution_time = time.time() - start_time

        # Зберігаємо параметри в текстовий файл
        with open("log.txt", "a") as log_file:
            log_file.write(
                f"Path: {request.path}, Method: {request.method}, Execution time: {execution_time}\n"
            )

        return response

    return middleware
