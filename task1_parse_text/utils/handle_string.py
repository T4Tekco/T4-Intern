from utils import second_parts, shared_function, first_part, special_elements, special_elements_2

import pandas as pd

def parse_text(raw_path, district_city_path):
    # Import data.
    real_estate_data, real_estate_information, real_estate_description = shared_function.split_raw_data(raw_path)
    district_city_df = shared_function.import_district_city_data(district_city_path)
    
    id_series = real_estate_data.iloc[:, 0]
    per_square_meter = real_estate_data.iloc[:, 2]
    array_2d = []
    for idx, row in real_estate_information.items():

        district = shared_function.split_district_city(row, district_city_df)[0]
        city = shared_function.split_district_city(row, district_city_df)[1]
        real_estate_id = [id_series[idx]]
        price_per_square_meter = [per_square_meter[idx]]

        # Count number of commars in each rows,
        if row.count(',') <= 5:
            
            
            components_list = row.split(', ')
            # components_list = [item for item in components_list if item.strip() != ""]

            first_part_list = components_list[0].split(' ')
            second_part_list = components_list[1:]

            first_elements = first_part.identify_elements_of_first_part(first_part_list)
            second_elements = second_parts.identify_final_elements_list(second_part_list)

            real_estate_data = real_estate_id  + first_elements + second_elements + [district] + [city] + price_per_square_meter
            array_2d.append(real_estate_data)
        else:

            components_list = row.split(' ')
            first_p = special_elements.identify_elememts_commas(components_list)
            second_p = special_elements_2.identify_final_elements_list_2(components_list)

            real_estate_data = real_estate_id  + first_p + second_p + [district] + [city] + price_per_square_meter
            array_2d.append(real_estate_data)






            

            
    names_column = ['id','address', 'area', 'num_floors', 'num_rooms', 'price', 'unit', 'position','name_hd', 'nphn','phone', 'commission', 'source', 'range', 'dc', 'district','city','per_square_meter']
    df = pd.DataFrame(array_2d, columns=names_column)
    df = df.reindex(columns=['id', 'address', 'district','city','num_floors', 'num_rooms','area','price', 'unit', 'per_square_meter', 'nphn', 'name_hd', 'position', 'phone', 'commission','source', 'range', 'dc'])
    return df

