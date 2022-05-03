#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



data = [
      'This song ',
        (8, 3),
      'just six words l',
        (23, 3),
      '\n',
        (33, 99),
      "Couldn't think of any lyrics\nNo I never wrote",
        (37, 3),
      'e',
        (28, 8),
      'S',
        (28, 3),
      "'ll",
        (85, 8),
      'ng',
        (57, 5),
      'old',
        (33, 8),
      'That com',
        (54, 3),
      'o mind, child\nYou really',
        (92, 3),
      'ed',
        (142, 6),
      '\nWhole',
        (148, 3),
      'tta rhym',
        (82, 3),
        (26, 7),
        (48, 4),
      'g',
        (24, 9),
      'e s',
        (79, 3),
        (108, 3),
        (30, 6),
      ', mm-mm\nTo do it, t',
        (10, 27),
        (39, 19),
      ' right',
        (156, 8),
        (403, 132),
      'I know t',
        (320, 4),
      "you're probably",
        (56, 3),
      "re\n'Cause",
        (411, 3),
      'di',
        (443, 5),
      'write',
        (383, 5),
      'm',
        (31, 4),
      'I',
        (86, 5),
        (29, 8),
      'get',
        (236, 3),
        (393, 4),
      'plete',
        (261, 4),
      'So',
        (93, 5),
      "'s why I",
        (349, 8),
      'epeat',
        (32, 3),
        (162, 33),
      ' (',
        (16, 14),
      ')',
        (50, 51),
      'Oh I',
        (455, 3),
      'k',
        (184, 3),
        (501, 7),
      'money',
        (74, 3),
      'ey pa',
        (203, 3),
        (26, 4),
      'ton',
        (659, 3),
        (27, 11),
        (269, 5),
      "ayin'",
        (33, 4),
        (210, 3),
      'nty',
        (34, 11),
      'o',
        (650, 6),
      't',
        (143, 8),
        (471, 8),
        (228, 8),
      'fi',
        (690, 3),
      'time',
        (77, 3),
      'ree',
        (663, 4),
      'utes',
        (154, 4),
      'th',
        (72, 3),
        (28, 6),
      'Oh, h',
        (386, 3),
      'w',
        (46, 4),
      'I',
        (53, 6),
        (629, 4),
      'uch',
        (33, 5),
        (628, 8),
        (768, 5),
      'thr',
        (43, 3),
      'in a',
        (36, 3),
      'lo,',
        (8, 15),
      '\nA',
        (15, 13),
      ' here',
        (614, 133),
        (33, 9),
      "'s",
        (285, 4),
      ' no',
        (1026, 4),
      "'",
        (556, 4),
      'say\nBut',
        (992, 3),
      'm',
        (534, 3),
      'c',
        (52, 3),
      'i',
        (72, 4),
      't',
        (611, 4),
      'way',
        (673, 8),
      'if',
        (285, 3),
      'p',
        (40, 3),
      'my',
        (992, 5),
      ' t',
        (848, 4),
        (30, 8),
      'I c',
        (1115, 4),
      ' f',
        (26, 4),
      'a',
        (99, 3),
      'od',
        (960, 7),
        (259, 3),
        (356, 6),
      'y',
        (985, 9),
      'have-a',
        (354, 3),
      'sic',
        (1008, 4),
        (1049, 5),
        (1061, 8),
      'catchy',
        (29, 6),
        (216, 11),
      'ha',
        (185, 5),
        (517, 12),
        (34, 5),
        (186, 3),
        (241, 15),
        (518, 8),
      'A',
        (138, 3),
      's',
        (1207, 7),
        (552, 4),
      "' em o",
        (1246, 3),
        (26, 4),
        (9, 5),
      ' a',
        (9, 11),
        (27, 32),
        (519, 7),
        (61, 54),
      ' again\nS',
        (405, 13),
      ',',
        (421, 15),
        (31, 32),
    ]

one_test(data)



print()
print("TESTCASE COMPLETED")

