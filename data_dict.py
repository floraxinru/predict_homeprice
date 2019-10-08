#make a dictionary of dictionaries to store data (convert to DF later using pd.DataFrame)
def make_data_dict(listing):
    '''
    Takes input string, listing, cleans it, and splices it so the unique MLS ID # is the key,
    and value is a dictionary of dictionaries so that feature category (ie Sqft) is the key,
    and the numerical or categorical value (ie 699) is the value.

    Example:
    listing = '$849,000 \n 2 Beds \n 1.5 Baths \n 958 Sq. Ft. \n 2770 Burrard St #207, Vancouver, BC V6J 3J8 \n Redfin \n MLS R2379412'
    >print(data_dict(listing)) 
    {R2379412:  {'Price': $849,000,  'Beds': 2,  'Baths': 1.5,  'Size_SqFt':958,  'Addr': '2770 Burrard St #207, Vancouver, BC V6J 3J8'}}

    3rd listing:
    R2410846: {'Price': '$1,299,000', 'Beds': '2 Beds', 'Baths': '1.5 Baths', 'Size_sqft': '1,184 Sq. Ft.', 'Addr': '2421 Trafalgar St, Vancouver, BC V6K 3T2'}
    (how to add on new listings? make this loop-friendly)
    '''
    #make a list of dictionaries to store scraped data

    cleaned = listing.strip(' ').split('\n') #split returns a list, so use other string methods before it
    #print(cleaned) 

    columns=["Price", "Beds", "Baths", "Size_sqft","Addr","Agent","MLS"] #keys for inside dicts; missing MLS id?
    feat_values = [i.strip() for i in cleaned] #values for inside dicts, list comprehension; 
    #decided not to skip first element (has open house time for the first 2 listings only) -- keep all in dict and clean in df later
    #print(columns, feat_values)

    #assign the two lists: columns and cleaned, into dictionary; zip()should be faster, can also use dict comprehension
    data_dict = dict(zip(columns, feat_values)) 
     
    #dictionaries are not ordered!
    #MLSids = cleaned[-1].strip().split() - don't need, used for dict of dict
    #data_dict[MLSids[1]] = inner_d #strip whitespace for that string in list
    
    #print(data_dict)
    return data_dict

#listing = '$849,000 \n 2 Beds \n 1.5 Baths \n 958 Sq. Ft. \n 2770 Burrard St #207, Vancouver, BC V6J 3J8 \n Redfin \n MLS R2379412'

#make_data_dict(listing)


