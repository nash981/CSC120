#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



whos_on_first_comp = [
      'Abbott: Well Cost',
        (8, 3),
      "o, I'm going to New York with you.",
        (15, 3),
      "u know Bucky Harris, the Yankee's manager, gave me a job as coach for",
        (13, 4),
      'long',
        (8, 3),
        (88, 4),
      "'re on",
        (70, 5),
      'team.\n\n',
        (146, 8),
      ': Look ',
        (174, 6),
      ', if',
        (47, 8),
        (44, 3),
        (79, 6),
      ',',
        (18, 4),
      ' must',
        (153, 6),
      'all',
        (29, 5),
      'players',
        (76, 3),
        (235, 8),
      'I certainly do',
        (101, 13),
        (262, 5),
      'y',
        (220, 8),
      "I'",
        (184, 3),
      'never',
        (190, 3),
      't',
        (78, 5),
      'guys. So',
        (127, 5),
        (44, 3),
      'h',
        (219, 3),
        (291, 4),
      't',
        (57, 4),
      'm',
        (143, 5),
      'ir name',
        (270, 3),
      'and',
        (17, 4),
      'n I',
        (43, 3),
        (83, 6),
      "who's",
        (148, 5),
        (348, 3),
        (236, 15),
        (160, 8),
      'Oh,',
        (50, 6),
      't',
        (142, 7),
        (86, 14),
      'but',
        (163, 10),
      'it seems',
        (132, 3),
        (127, 7),
      'y giv',
        (10, 5),
      'se b',
        (262, 3),
        (258, 8),
      ' ',
        (48, 3),
      '-a-days ',
        (211, 3),
      'y peculia',
        (89, 7),
        (264, 13),
      'Y',
        (331, 4),
      'ean funny',
        (33, 6),
      '?',
        (162, 10),
      'Strange',
        (146, 8),
      'pet',
        (68, 7),
      '..like Dizzy D',
        (65, 3),
      '..',
        (88, 13),
      'His broth',
        (339, 3),
      'Daffy',
        (247, 11),
        (16, 4),
        (53, 21),
      'And',
        (258, 7),
      'French',
        (496, 3),
      'usin',
        (59, 11),
        (24, 6),
      '?',
        (53, 12),
      'Goofe',
        (35, 11),
        (16, 5),
        (94, 6),
        (486, 5),
      ", let's",
        (318, 4),
      ', we',
        (457, 4),
        (636, 9),
      'bag',
        (214, 3),
      'W',
        (427, 5),
      'o',
        (260, 3),
      'irst',
        (16, 4),
      'at',
        (17, 6),
      'second,',
        (585, 3),
      "Don't K",
        (394, 5),
      's',
        (63, 6),
      'ird',
        (192, 15),
      'T',
        (57, 6),
      'w',
        (7, 3),
        (51, 3),
      'want',
        (430, 4),
      'fi',
        (215, 3),
      'out',
        (665, 13),
      'say',
        (120, 47),
      "'",
        (119, 10),
        (309, 14),
      're',
        (571, 8),
        (905, 8),
        (449, 11),
      'Y',
        (496, 19),
      'gonna b',
        (851, 11),
        (167, 3),
      'o',
        (53, 27),
        (408, 3),
        (99, 5),
      'd',
        (141, 3),
        (885, 7),
        (59, 4),
      'f',
        (30, 4),
      "ws'",
        (566, 17),
        (861, 5),
        (228, 3),
      'hould',
        (887, 18),
        (810, 5),
      'w',
        (253, 13),
        (125, 27),
      'I',
        (672, 5),
        (113, 11),
      "'s",
        (113, 4),
        (499, 12),
        (329, 3),
        (392, 15),
        (960, 5),
        (94, 9),
        (43, 31),
        (36, 5),
        (524, 3),
      'se',
        (320, 3),
        (87, 35),
        (981, 7),
      '..',
        (44, 14),
      ' i',
        (208, 10),
      '!',
        (194, 13),
      "'m",
        (1271, 3),
      'k',
        (1032, 4),
      'YOU',
        (250, 6),
        (156, 20),
        (575, 6),
        (457, 8),
        (231, 7),
        (609, 22),
      'o',
        (30, 7),
        (312, 27),
        (363, 5),
      'go ahead',
        (1186, 4),
        (1211, 8),
        (114, 18),
      'it',
        (102, 23),
        (95, 17),
      'PAUSE',
        (1453, 16),
        (1425, 6),
      'g',
        (39, 3),
      'a',
        (332, 14),
        (63, 11),
      'C',
        (1417, 8),
        (164, 14),
        (1317, 13),
        (522, 6),
        (158, 17),
      'right',
        (55, 15),
      'en',
        (116, 5),
      'pa',
        (485, 3),
      'ff t',
        (454, 16),
      ' e',
        (1273, 5),
      'month,',
        (202, 4),
      ' get',
        (347, 7),
      'oney',
        (102, 11),
      'E',
        (42, 5),
      'dollar',
        (77, 3),
        (269, 16),
      'All',
        (449, 5),
      'tr',
        (164, 4),
        (976, 12),
        (496, 3),
        (662, 18),
        (472, 3),
        (138, 10),
        (676, 36),
      't',
        (229, 3),
        (157, 5),
      '..',
        (409, 33),
      'W',
        (200, 17),
        (53, 13),
      'He',
        (199, 3),
        (1447, 4),
      'e',
        (211, 11),
        (1732, 4),
        (1748, 3),
      'i',
        (930, 3),
      ' his',
        (2010, 3),
      'f',
        (1013, 4),
        (15, 4),
      'down',
        (537, 5),
      'c',
        (42, 3),
      'ect',
        (112, 20),
      "'",
        (50, 6),
        (521, 24),
        (222, 10),
        (563, 6),
      'r',
        (2019, 3),
        (2109, 6),
        (216, 4),
      '?',
        (554, 18),
        (1703, 3),
        (1307, 6),
        (1154, 3),
      'k',
        (1358, 7),
      'w',
        (463, 8),
      'sign up',
        (463, 18),
      ', how',
        (221, 5),
      ' he',
        (39, 6),
      'hi',
        (770, 7),
        (355, 33),
        (389, 27),
      'H',
        (86, 15),
        (388, 20),
        (122, 3),
        (31, 8),
        (289, 18),
        (803, 24),
        (578, 42),
      'w',
        (1013, 10),
        (172, 3),
        (582, 32),
      'No.',
        (364, 5),
      ' i',
        (1576, 11),
        (37, 6),
        (1138, 16),
      'not',
        (1142, 8),
        (348, 3),
        (772, 4),
        (1628, 12),
        (277, 12),
        (1168, 16),
        (72, 10),
      'One',
        (93, 5),
      ' at',
        (2516, 3),
        (581, 4),
      '!',
        (1510, 14),
      ',',
        (1556, 7),
      'ch',
        (2087, 4),
        (2439, 12),
      ' around',
        (151, 21),
        (46, 5),
        (153, 4),
      'nobody!',
        (372, 11),
      'ake',
        (2283, 4),
      'easy',
        (2305, 4),
      'ddy',
        (66, 17),
      'o',
        (1094, 3),
        (218, 11),
      ',',
        (219, 7),
      't',
        (1525, 15),
        (185, 5),
        (1102, 36),
      'Ok',
        (269, 11),
        (429, 3),
        (35, 6),
        (458, 20),
      'W',
        (428, 34),
      '?',
        (428, 31),
        (423, 85),
      'I',
        (1946, 11),
        (1040, 13),
        (2100, 11),
        (2300, 4),
        (2887, 3),
        (112, 5),
      'tal',
        (113, 5),
      'ab',
        (645, 4),
      'hi',
        (2944, 14),
      'Now',
        (879, 6),
      'id I',
        (1136, 4),
        (68, 9),
        (226, 16),
      'Why',
        (2956, 6),
      'enti',
        (1167, 3),
      'd',
        (76, 3),
        (1718, 19),
      'If I',
        (36, 11),
        (319, 3),
        (79, 11),
        (1770, 10),
        (1448, 6),
        (118, 3),
        (2335, 7),
      'i',
        (1562, 10),
        (47, 5),
        (347, 14),
        (1596, 20),
      '.',
        (429, 16),
        (2146, 22),
        (2408, 16),
        (332, 49),
        (1126, 16),
      're',
        (297, 4),
      'o,',
        (209, 3),
      'ck',
        (302, 10),
      'ag',
        (1778, 3),
      '!',
        (584, 20),
        (2328, 3),
        (2386, 6),
      'j',
        (3270, 4),
      'stay',
        (356, 14),
        (1430, 4),
        (136, 7),
      'go',
        (1762, 5),
      'it',
        (677, 20),
      ',',
        (2668, 6),
      'd',
        (3238, 5),
        (2673, 9),
        (187, 4),
      '?',
        (466, 13),
        (3216, 16),
        (463, 26),
        (75, 7),
      'insis',
        (505, 5),
      'putt',
        (50, 3),
        (367, 4),
        (520, 17),
        (365, 14),
      ' am I',
        (48, 8),
        (300, 10),
        (785, 44),
      'Y',
        (2661, 9),
        (204, 5),
        (180, 3),
        (41, 10),
      '?',
        (2413, 15),
        (780, 44),
      ' &',
        (3826, 9),
      ' Toge',
        (3223, 4),
      ':T',
        (203, 9),
      '!',
        (2265, 35),
        (810, 3),
      'field',
        (3357, 12),
      'ure',
        (1649, 17),
      'left ',
        (42, 5),
      "er'",
        (1699, 19),
      'y',
        (174, 15),
        (514, 5),
      't',
        (2858, 3),
        (463, 3),
        (1041, 3),
      'd',
        (1037, 4),
        (3962, 5),
        (1385, 15),
        (43, 20),
        (3639, 6),
      'a',
        (132, 16),
      'n',
        (2538, 8),
        (501, 15),
        (155, 9),
        (405, 11),
        (839, 33),
        (1188, 7),
        (1818, 3),
        (680, 7),
      'u',
        (535, 3),
        (2418, 6),
      'in',
        (77, 5),
      '! I',
        (635, 13),
        (1747, 23),
      'in',
        (129, 6),
        (326, 16),
      'No,',
        (1319, 90),
      '!',
        (539, 54),
      ' ',
        (540, 18),
        (488, 62),
      'Becau',
        (77, 3),
        (4092, 14),
      'h',
        (1109, 4),
      'c',
        (1305, 3),
      'er',
        (74, 5),
        (2913, 26),
      'Y',
        (648, 9),
      'pitc',
        (163, 3),
        (864, 7),
      's',
        (4179, 5),
        (660, 32),
        (52, 5),
        (167, 20),
      'Tomorrow',
        (901, 28),
        (4340, 12),
      'oda',
        (2875, 12),
        (409, 3),
        (28, 5),
        (406, 8),
        (344, 3),
        (652, 18),
        (3203, 8),
      '.',
        (119, 18),
      '!',
        (1091, 17),
        (2147, 4),
        (1450, 15),
        (20, 5),
        (596, 5),
      '?',
        (47, 21),
      ' t',
        (78, 7),
      ' a',
        (3850, 4),
        (3808, 8),
        (772, 16),
        (259, 4),
        (168, 3),
        (633, 13),
      'w li',
        (80, 3),
      'n.',
        (1106, 8),
        (614, 3),
        (42, 9),
        (643, 15),
      'll',
        (4304, 3),
      'ea',
        (924, 5),
      'r',
        (107, 3),
      'm,',
        (2739, 6),
      'ay',
        (3537, 15),
        (783, 28),
        (393, 14),
        (1683, 28),
        (696, 85),
      'G',
        (578, 5),
      'a ca',
        (135, 5),
        (3487, 33),
      'T',
        (4128, 4),
      'a',
        (572, 25),
      'da',
        (47, 15),
        (18, 4),
        (4877, 5),
        (404, 9),
        (378, 11),
      '.',
        (378, 14),
        (4951, 4),
      've',
        (725, 4),
        (3442, 20),
      'w',
        (26, 7),
        (2631, 3),
        (4613, 4),
      'ple',
        (1141, 4),
        (4818, 4),
        (4939, 12),
        (816, 20),
      'Y',
        (5076, 10),
      'm',
        (235, 10),
        (4321, 4),
      '.',
        (806, 11),
      'o',
        (4929, 5),
        (548, 6),
        (2222, 16),
        (2291, 5),
      'beh',
        (2981, 3),
        (2769, 8),
      't',
        (5115, 5),
        (1820, 3),
      'som',
        (3227, 3),
      'ancy',
        (90, 3),
        (216, 6),
      ', T',
        (237, 18),
        (166, 4),
      'my',
        (165, 5),
        (272, 5),
      'a ',
        (771, 3),
      'vy',
        (2336, 3),
      't',
        (1005, 3),
        (3525, 6),
      'up. N',
        (4427, 6),
        (30, 14),
      'bunts',
        (4768, 7),
      'll.',
        (3823, 6),
      'he',
        (24, 15),
      ', ',
        (2355, 4),
      'be',
        (2505, 5),
        (302, 3),
      'od',
        (237, 8),
        (5589, 5),
        (774, 8),
      'h',
        (153, 3),
        (2844, 10),
      'ut',
        (3019, 3),
        (3163, 12),
        (267, 3),
        (1973, 4),
      'ick',
        (144, 3),
        (92, 9),
        (180, 4),
        (59, 7),
      'i',
        (713, 5),
        (739, 3),
        (826, 15),
      't',
        (690, 5),
        (3499, 11),
      't',
        (248, 4),
        (471, 8),
      'said',
        (2211, 5),
        (1949, 22),
        (3745, 3),
      'n',
        (797, 10),
        (175, 4),
        (2708, 14),
        (701, 8),
        (3006, 17),
      'a',
        (5416, 6),
        (5518, 8),
        (5590, 16),
      'I',
        (5407, 4),
        (244, 11),
      'b',
        (5660, 5),
      'o',
        (3404, 22),
        (3503, 3),
      '!',
        (2342, 22),
        (661, 6),
        (241, 12),
      'atur',
        (76, 3),
      'y',
        (1442, 26),
      'i',
        (2789, 3),
        (122, 29),
      ',',
        (573, 5),
        (3312, 4),
      "'s",
        (1484, 7),
      'ge',
        (765, 5),
        (122, 8),
        (214, 3),
      's',
        (120, 26),
        (3702, 13),
        (36, 33),
        (22, 9),
        (42, 33),
        (513, 26),
      'I',
        (515, 13),
        (62, 9),
        (969, 13),
        (5144, 10),
        (1296, 5),
        (258, 19),
        (174, 3),
        (154, 22),
        (3947, 18),
      'differ',
        (1808, 3),
        (5462, 27),
        (602, 4),
        (453, 12),
      'ou',
        (3286, 8),
      's',
        (2243, 6),
      'it',
        (5526, 14),
        (407, 17),
        (205, 24),
        (75, 3),
        (241, 9),
        (185, 47),
      'i',
        (178, 32),
      '!',
        (103, 14),
        (2532, 4),
      'me',
        (166, 33),
      'w',
        (489, 36),
        (1356, 4),
        (83, 6),
        (5084, 14),
      'Y',
        (398, 24),
      '?',
        (213, 54),
      'S',
        (1535, 3),
        (6590, 7),
      '!',
        (13, 9),
        (5328, 3),
      '!',
        (187, 24),
        (1878, 5),
        (6484, 5),
      'i',
        (1482, 5),
      'drops',
        (1123, 16),
        (1176, 6),
      'run',
        (954, 4),
        (1789, 8),
        (57, 4),
        (659, 5),
      's',
        (1173, 22),
      's',
        (418, 9),
      'at',
        (3155, 6),
        (24, 14),
        (5943, 12),
      '.',
        (6077, 14),
        (40, 10),
        (3500, 5),
      'to',
        (1470, 9),
        (1480, 3),
      'ripl',
        (4289, 6),
      '.',
        (5876, 3),
        (6333, 6),
        (159, 3),
        (1455, 8),
        (129, 5),
        (1444, 3),
        (1159, 3),
        (6860, 6),
      'fly',
        (241, 9),
        (2530, 7),
      '.',
        (2555, 4),
      '?',
        (1971, 13),
      '!',
        (3645, 14),
        (70, 4),
        (32, 9),
        (6594, 5),
      'a',
        (1753, 3),
      'rn',
        (4442, 12),
        (2285, 16),
        (581, 5),
        (54, 32),
        (2642, 3),
        (1430, 8),
        (2211, 3),
        (6014, 4),
      'rtstop',
        (454, 3),
      '-',
        (1, 3),
      '\nS',
        (22, 3),
      'ce: http://www.',
        (1176, 4),
        (193, 4),
      '-al',
        (6203, 4),
      'c.',
        (5145, 3),
      '/hu',
        (273, 3),
      '4.shtml'
     ]


one_test(whos_on_first_comp)



print()
print("TESTCASE COMPLETED")
