import psutil

if __name__ == "__main__":
    print(f"Congratulations! You have {psutil.cpu_count()} cores.")