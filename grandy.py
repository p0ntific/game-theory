def calculate_grundy(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 0
        return 0
    mex = set()
    for k in range(1, n // 2 + 1):
        if k != n - k:
            g1 = calculate_grundy(k, memo)
            g2 = calculate_grundy(n - k, memo)
            mex.add(g1 ^ g2)
    grundy_number = 0
    while grundy_number in mex:
        grundy_number += 1
    memo[n] = grundy_number
    return grundy_number

def calculate_nimber(heaps):
    nimber = 0
    for heap in heaps:
        nimber ^= calculate_grundy(heap)
    return nimber

def optimal_move(heaps):
    for i, heap in enumerate(heaps):
        original_grundy = calculate_grundy(heap)
        for k in range(1, heap // 2 + 1):
            if k
!= heap - k:
                new_heaps = heaps[:i] + [k, heap - k] + heaps[i+1:]
                new_nimber = calculate_nimber(new_heaps)
                if new_nimber == 0:
                    return i, k, heap - k
    return None  # Нет выигрышного хода

# Пример игры
heaps = [7]  # Начальное состояние

current_player = "Первый игрок"
while any(heap > 1 for heap in heaps):
    nimber = calculate_nimber(heaps)
    print(f"\nТекущее состояние куч: {heaps}")
    print(f"Текущее нимбер позиции: {nimber}")
    if nimber == 0:
        print(f"{current_player} находится в проигрышной позиции.")
    else:
        print(f"{current_player} может выиграть при правильной игре.")
    move = optimal_move(heaps)
    if move:
        index, part1, part2 = move
        print(f"{current_player} разделяет кучу размера {heaps[index]} на кучи {part1} и {part2}.")
        heaps = heaps[:index] + [part1, part2] + heaps[index+1:]
    else:
        # Если нет выигрышного хода, делаем любой допустимый ход
        index = next(i for i, heap in enumerate(heaps) if heap > 1)
        heap = heaps[index]
        # Разделяем на любые неравные части
        k = 1
        if heap - k != k:
            part1, part2 = k, heap - k
        else:
            k = 2
            part1, part2 = k, heap - k
        print(f"{current_player} разделяет кучу размера {heap} на кучи {part1} и {part2}.")
        heaps = heaps[:index] + [part1, part2] + heaps[index+1:]
    # Сменить игрока
    current_player = "Второй игрок" if current_player == "Первый игрок" else "Первый игрок"

print(f"\nИгра окончена. {current_player} не может сделать ход и проигрывает.")
