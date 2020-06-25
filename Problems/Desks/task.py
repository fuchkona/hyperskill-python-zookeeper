first_group_population = int(input())
second_group_population = int(input())
third_group_population = int(input())


def get_desks_count(population):
    desks_count = population // 2
    remainder = population % 2
    return desks_count + remainder


needed_desks = get_desks_count(first_group_population) + get_desks_count(second_group_population) + get_desks_count(
    third_group_population)

print(needed_desks)
