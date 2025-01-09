import random

def generate_ssn():
    area = str(random.randint(1, 899)).zfill(3)
    group = str(random.randint(1, 99)).zfill(2)
    serial = str(random.randint(1, 9999)).zfill(4)
    return f"{area}-{group}-{serial}"

if __name__ == "__main__":
    print(generate_ssn())