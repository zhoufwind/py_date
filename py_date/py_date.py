# print('Hello World')

# Print date via user's imputing
months=['JAN.', 'FEB.', 'MAR.', 'APR.', 'MAY', 'JUN.', 'JUL.', 'AUG.', 'SEP.', 'OCT.', 'NOV.', 'DEC.']
# end with number endings
endings=['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

year=raw_input('Year: ')
month=raw_input('Month (1-12): ')
day=raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# noticing the index value
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + ', ' + year
