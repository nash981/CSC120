def too_many_aliases():
    end_alias_1 = [11, 22]
    end_alias_2 = [33, 44]
    intermediate_alias_1 = [end_alias_1, end_alias_2]
    intermediate_alias_2 = [end_alias_1, end_alias_2]
    base_alias = \
        [intermediate_alias_1, intermediate_alias_2, intermediate_alias_1, intermediate_alias_2]
    return base_alias
