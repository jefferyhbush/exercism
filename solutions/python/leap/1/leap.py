def leap_year(year):
    divisible_by_four = year % 4 == 0
    divisible_by_hundred = year % 100 == 0
    divisible_by_4hundred = year % 400 == 0

    return (divisible_by_four and not divisible_by_hundred) or divisible_by_4hundred