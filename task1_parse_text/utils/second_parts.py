# Get phone number
def identify_phone_number(final_elements):
    """ The function determines the phone number in a string with the condition that the string is all numbers and the string length is greater than or equal to 11.
    Args:
        final_elements (list): List of last elements after first comma separator

    Returns:
        phone_number: Real estate seller phone number
    """
    phone_number = None
    for value in final_elements:
        value = value.replace(',', '')
        if value.isdigit() and len(value) >= 10 and len(value) <= 11:
            phone_number = value
            break
    return phone_number

# Get commission
def identify_commission(final_elements):
    commission = None
    for value in final_elements:
        value = value.replace(',', '')
        if value.startswith('X') and value[1:].isdigit():
            commission = value


            
    return commission

# Get source
def identify_source(final_elements):
    source = None
    for value in final_elements:
        if value.startswith('nguồn'):
            source = value
            break      
    return source

# Get Dc
def identify_dc(final_elements):
    return final_elements[-1]


# Final list
def identify_final_elements_list(final_elements):

    # Components
    phone_number = identify_phone_number(final_elements)
    commission = identify_commission(final_elements)
    source = identify_source(final_elements)
    dc = identify_dc(final_elements)
    negotiable_range = None

    keyword_range = ['nhỏ','đến','trên', 'nho']

    for word in final_elements:
        word_split = word.strip().split(' ')

        for keyword in keyword_range:
            if keyword in word_split:
                if keyword == 'nhỏ' or keyword =='trên':
                    negotiable_range = keyword + " " + word_split[word_split.index(keyword) + 1]
                else:
                    negotiable_range = word_split[word_split.index(keyword) - 1] + " " + keyword + " " + word_split[word_split.index(keyword) + 1]


    if source is not None:
        source = source.replace('nguồn', '')

    return [phone_number, commission, source, negotiable_range, dc]
