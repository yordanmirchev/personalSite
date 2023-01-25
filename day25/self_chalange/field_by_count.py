import pandas

def field_by_count(file_name, field):
    data = pandas.read_csv(file_name)
    fields_data = data[field]
    unique_fields = []
    for field_data in fields_data.dropna().unique():
        unique_fields.append(field_data)
    field_list = []
    field_count = []
    for unique_field in unique_fields:
        field_list.append(unique_field)
        field_count.append(fields_data[data[field] == unique_field].count())

    field_dict = {f"{field}": field_list, "count": field_count}

    field_frame = pandas.DataFrame.from_dict(field_dict)
    print(field_frame)
    new_file_name = field.replace(" ", "_")
    field_frame.to_csv(f"{new_file_name}_by_count.csv")



