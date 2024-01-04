number_of_wins_dict = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                    'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                    'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0, 'Iceland': 0,
                                    'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                    'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                    'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                    'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

list_of_countries = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Canada', 'Croatia', 'Czech Republic',
                             'Denmark', 'England', 'Finland', 'France', 'Germany',
                             'Hungary', 'Iceland', 'Ireland', 'Italy', 'Mexico', 'Ghana', 'Netherlands', 'Morocco',
                             'Norway', 'Poland', 'Portugal', 'Romania', 'Scotland', 'Spain',
                             'Sweden', 'Ukraine', 'USA', 'Wales', 'Japan', 'China'
                             ]
percentage_list = []
for country in list_of_countries:
    number_won = number_of_wins_dict[country]
    print(number_won)