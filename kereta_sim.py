import random

def berangkat():
    n = random.randint(1, 10)
    if 1 <= n <= 7:
        return 0
    elif 8 <= n <= 9:
        return 5
    elif 10 <= n <= 10:
        return 10

def tempuh():
    n = random.randint(-2, 2)
    return 30 + n 

def stasiun():
    n = random.randint(1, 10)
    if 1 <= n <= 3:
        return 28
    elif 4 <= n <= 7:
        return 30
    elif 8 <= n <= 9:
        return 32
    elif 10 <= n <= 10:
        return 34

def simulate():
    n_sims = 100000
    res_table = []
    for i in range(n_sims):
        res = stasiun() < (berangkat() + tempuh())
        res_table.append(1 if res else 0)
    print(f"Persentase Dapat Kereta: {sum(res_table) / n_sims}")

def main():
    simulate()

if __name__ == '__main__':
    main()
