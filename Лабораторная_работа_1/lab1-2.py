disk_vol_mb = 1.44  # TODO Найдите количество книг, которое можно разместить на дискете
num_of_lists, num_of_str, num_of_sym = 100, 50, 25
vol_of_sym_b = 4
disk_vol_b = disk_vol_mb * 1024 ** 2
book_vol_b = num_of_lists * num_of_str * num_of_sym * vol_of_sym_b
print("Количество книг, помещающихся на дискету:", int(disk_vol_b // book_vol_b))
