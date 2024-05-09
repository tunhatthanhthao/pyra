import mysql.connector
import csv

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ed&11281999',
        database='csvConnection'
    )

    cursor = connection.cursor()

    data = [
        (3, 13, 2, 7, 2, 10, 8, 16),
        (20, 24, 9, 17, 11, 18, 23, 33),
        (25, 33, 22, 26, 28, 30, 39, 40),
        (34, 35, 35, 36, 37, 41, 47, 48),
        (44, 48, 44, 52, 50, 54, 54, 58),
        (52, 60, 57, 58, 61, 70, 60, 63),
        (65, 67, 64, 73, 77, 86, 67, 72),
        (72, 82, 81, 90, 93, 103, 73, 81),
        (86, 93, 97, 100, 109, 118, 87, 89),
        (101, 110, 102, 105, 127, 134, 95, 103),
        (111, 119, 106, 111, 144, 154, 113, 120),
        (122, 125, 120, 124, 155, 159, 129, 138),
        (129, 136, 133, 139, 169, 175, 146, 151),
        (145, 155, 140, 147, 184, 187, 160, 169),
        (159, 166, 148, 156, 193, 203, 178, 182),
        (175, 182, 164, 170, 210, 216, 183, 192),
        (191, 201, 180, 186, 224, 234, 193, 197),
        (204, 213, 196, 199, 236, 245, 202, 203),
        (215, 217, 200, 208, 246, 251, 207, 212),
        (219, 229, 211, 217, 256, 258, 215, 218),
        (234, 243, 220, 225, 263, 271, 224, 232),
        (251, 253, 226, 231, 278, 284, 239, 243),
        (258, 260, 236, 245, 288, 298, 250, 251),
        (264, 265, 252, 255, 299, 302, 259, 268),
        (272, 281, 259, 268, 310, 314, 277, 278),
        (288, 298, 274, 281, 315, 320, 281, 285),
        (299, 304, 283, 285, 325, 330, 288, 295),
        (314, 319, 288, 289, 339, 340, 305, 309),
        (329, 337, 292, 302, 349, 350, 316, 320),
        (343, 345, 306, 316, 357, 367, 324, 332),
        (347, 354, 321, 330, 375, 376, 338, 348),
        (361, 366, 331, 334, 380, 386, 358, 361),
        (372, 379, 338, 343, 388, 395, 370, 376),
        (388, 396, 352, 356, 397, 398, 378, 381),
        (399, 402, 365, 369, 403, 409, 391, 400),
        (407, 413, 375, 381, 411, 416, 404, 414),
        (421, 424, 391, 400, 418, 424, 415, 422),
        (426, 433, 403, 406, 430, 432, 432, 442),
        (440, 442, 416, 425, 436, 446, 444, 449),
        (448, 453, 435, 444, 448, 456, 454, 456),
        (454, 459, 445, 455, 457, 459, 463, 465),
        (460, 464, 459, 469, 466, 469, 467, 475),
        (467, 471, 472, 474, 476, 483, 484, 489),
        (480, 485, 482, 488, 485, 489, 495, 496),
        (486, 487, 493, 503, 495, 503, 503, 509),
        (494, 496, 505, 511, 513, 521, 511, 516),
        (500, 510, 520, 528, 527, 532, 519, 528),
        (514, 519, 532, 536, 538, 540, 533, 535),
        (527, 529, 546, 552, 544, 551, 540, 541),
        (535, 538, 558, 568, 556, 560, 547, 549),
        (547, 557, 578, 588, 562, 566, 553, 554),
        (561, 568, 590, 595, 575, 577, 556, 557),
        (569, 574, 601, 609, 585, 588, 559, 568),
        (580, 582, 618, 621, 591, 594, 571, 577),
        (587, 589, 630, 640, 599, 602, 581, 584),
        (598, 599, 646, 656, 611, 615, 587, 592),
        (606, 615, 659, 660, 619, 624, 594, 602),
        (622, 631, 665, 674, 632, 641, 610, 611),
        (638, 644, 677, 682, 649, 650, 618, 628),
        (645, 646, 688, 698, 653, 663, 631, 634),
        (651, 656, 705, 715, 670, 673, 644, 646),
        (660, 668, 716, 719, 682, 688, 655, 663),
        (672, 676, 725, 733, 696, 700, 670, 676),
        (685, 695, 738, 742, 701, 703, 685, 691),
        (698, 707, 746, 751, 708, 713, 700, 706),
        (710, 718, 761, 763, 715, 725, 715, 725),
        (725, 728, 766, 771, 732, 736, 735, 736),
        (736, 743, 777, 784, 745, 748, 745, 746),
        (752, 754, 789, 791, 753, 755, 749, 759),
        (756, 764, 795, 802, 762, 769, 762, 768),
        (772, 775, 812, 820, 773, 775, 775, 785),
        (784, 791, 822, 827, 780, 784, 792, 801),
        (792, 796, 836, 844, 794, 795, 802, 812),
        (800, 805, 848, 851, 800, 803, 821, 825),
        (810, 815, 861, 866, 811, 814, 834, 840),
        (823, 830, 868, 872, 824, 831, 844, 849),
        (832, 833, 874, 884, 832, 841, 854, 857),
        (835, 844, 890, 900, 846, 853, 866, 872),
        (853, 859, 901, 903, 861, 869, 878, 883),
        (868, 875, 909, 919, 877, 879, 890, 897),
        (879, 888, 920, 925, 889, 898, 901, 909),
        (898, 907, 932, 937, 901, 909, 919, 928),
        (911, 917, 946, 947, 916, 926, 935, 942),
        (923, 933, 957, 959, 934, 938, 947, 948),
        (940, 943, 966, 971, 941, 943, 958, 959),
        (949, 954, 978, 987, 948, 951, 967, 972),
        (962, 965, 995, 1004, 952, 957, 981, 983),
        (975, 982, 1006, 1012, 959, 967, 984, 987),
        (991, 994, 1014, 1021, 972, 982, 992, 996),
        (1026, 1032, 1026, 1033, 1026, 1034, 1026, 1035),
        (1040, 1045, 1073, 1079, 1013, 1018, 1041, 1045),
        (1046, 1056, 1086, 1092, 1025, 1029, 1050, 1054),
        (1058, 1061, 1102, 1110, 1039, 1042, 1064, 1069),
        (1069, 1078, 1113, 1116, 1045, 1053, 1075, 1080),
        (1085, 1089, 1118, 1122, 1058, 1060, 1082, 1086),
        (1096, 1102, 1130, 1132, 1063, 1064, 1087, 1097),
        (1103, 1107, 1133, 1141, 1073, 1083, None, None),
        (1112, 1114, 1151, 1154, 1085, 1089, None, None)
    ]

    sql_query = "INSERT INTO consolidated_intervals (col1_start, col1_end, col2_start, col2_end, col3_start, col3_end, col4_start, col4_end) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.executemany(sql_query, data)

    connection.commit()

    # Exporting data to CSV file
    file_path = "C:/Users/Thanh/OneDrive/Documents/Ucare Research/data.csv"
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['col1_start', 'col1_end', 'col2_start', 'col2_end', 'col3_start', 'col3_end', 'col4_start', 'col4_end'])
        writer.writerows(data)

    print("Data inserted and exported successfully!")

except Exception as e:
    print("An error occurred:", e)

finally:
    cursor.close()
    connection.close()