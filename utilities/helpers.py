def rename_columns(name_changes, df):
    
    for key, value in name_changes.items():
        df = df.withColumnRenamed(key, value)

    return df