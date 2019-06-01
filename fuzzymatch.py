def check_match(left_df, right_df, left_index=None, right_index=None):

    if not left_index:
        left_index = left_df.index
    if not right_index:
        right_index = right_df.index

    only_left = left_index[~left_index.isin(right_index)]
    only_right = right_index[~right_index.isin(left_index)]

    return only_left, only_right
