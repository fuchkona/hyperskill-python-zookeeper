first_point_hour = int(input())
first_point_minute = int(input())
first_point_second = int(input())

second_point_hour = int(input())
second_point_minute = int(input())
second_point_second = int(input())

first_pint_timestamp = first_point_hour * 3600 + first_point_minute * 60 + first_point_second

second_pint_timestamp = second_point_hour * 3600 + second_point_minute * 60 + second_point_second

print(second_pint_timestamp - first_pint_timestamp)
