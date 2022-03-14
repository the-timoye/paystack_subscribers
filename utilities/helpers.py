def rename_columns(name_changes, df):
    """
    rename columns in a dataframe.
    @params:
        name_changes: a dictionary of old names (keys) and new names (values)
        df: the spark dataframe to be manipulated
    """
    for key, value in name_changes.items():
        df = df.withColumnRenamed(key, value)

    return df
