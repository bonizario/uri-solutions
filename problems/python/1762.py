def main():
    from math import ceil
    for _ in range(int(input())):
        presents = dict()
        for _ in range(int(input())):
            toy_name = input()
            toy_weight = float(input())
            presents[toy_name] = toy_weight
        sled_weight = float(input())
        total_weight = 0
        while True:
            toy_name = input()
            toy_quantity = int(input())
            if toy_name == '-' and toy_quantity == 0:
                break
            if toy_name not in presents:
                print(f'NAO LISTADO: {toy_name}')
                continue
            total_weight += (presents[toy_name] * toy_quantity)
        print(f'Peso total: {total_weight:.2f} kg')
        print(f'Numero de trenos: {ceil(total_weight / sled_weight)}\n')
main()
