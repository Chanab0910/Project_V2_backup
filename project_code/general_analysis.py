from project_code.analyse_results import Analyse


class GeneralAnalysis:
    def __init__(self):
        self.order_place_list = []
        self.highest = ['', 0]
        self.analyse = Analyse()
        self.dict_of_countries_place_came = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0, 'Brazil': 0,
                                             'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                             'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0,
                                             'Columbia': 0,
                                             'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                             'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0, 'Australia': 0,
                                             'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0, 'Nigeria': 0,
                                             'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}

        self.dict_of_countries_average_goals_scored = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0,
                                                       'Brazil': 0,
                                                       'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                                       'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0,
                                                       'Columbia': 0,
                                                       'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                                       'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0,
                                                       'Australia': 0,
                                                       'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0,
                                                       'Nigeria': 0,
                                                       'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}

        self.dict_of_countries_average_goals_conceded = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0,
                                                         'Brazil': 0,
                                                         'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                                         'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0,
                                                         'Columbia': 0,
                                                         'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                                         'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0,
                                                         'Australia': 0,
                                                         'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0,
                                                         'Nigeria': 0,
                                                         'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}

        self.second_dict_of_countries_place_came = {'Argentina': 0, 'France': 0, 'England': 0, 'Belgium': 0,
                                                    'Brazil': 0,
                                                    'Netherlands': 0, 'Portugal': 0, 'Spain': 0,
                                                    'Italy': 0, 'Croatia': 0, 'Uruguay': 0, 'Morocco': 0, 'USA': 0,
                                                    'Columbia': 0,
                                                    'Mexico': 0, 'Germany': 0, 'Senegal': 0, 'Japan': 0,
                                                    'Switzerland': 0, 'Iran': 0, 'Denmark': 0, 'Korea': 0,
                                                    'Australia': 0,
                                                    'Ukraine': 0, 'Austria': 0, 'Sweden': 0, 'Hungary': 0, 'Nigeria': 0,
                                                    'Wales': 0, 'Poland': 0, 'Equador': 0, 'Serbia': 0}

    def get_stats(self):
        """
        calls all the relevant methods to get all the stats
        Returns
        -------
        self.order_place_list: This is the order that the countries came when taking all simulations into account
        self.dict_of_countries_average_goals_scored: This is the average goals scored by each country
        self.dict_of_countries_average_goals_conceded: This is the average goals conceded by each country
        """
        self.get_average_goals()
        self.get_average_goals_conceded()
        self.get_dict_with_data()
        self.get_order_of_overall(self.dict_of_countries_place_came)
        return self.order_place_list, self.dict_of_countries_average_goals_scored, self.dict_of_countries_average_goals_conceded

    def get_dict_with_data(self):
        """
        This goes through each country and calls 'furthest_got_and_average_place'. It then appends this data to a
        dictionary to make a dictionary with all the countries data

        Returns
        -------
        None
        """
        for country in self.dict_of_countries_place_came:
            self.dict_place = self.analyse.furthest_got_and_average_place(country)
            group_num = self.dict_place['Group']
            R16_num = self.dict_place['Round of 16']
            quarter_num = self.dict_place['Quarter-final']
            semi_num = self.dict_place['Semi-final']
            final_num = self.dict_place['Final']
            win_num = self.dict_place['Win']
            places = [group_num, R16_num, quarter_num, semi_num, final_num, win_num]
            self.dict_of_countries_place_came[country] = places
            self.second_dict_of_countries_place_came[country] = places

    def get_order_of_overall(self, dict):
        """
        This uses recursion to get the country that did the best overall in the dict, add it to a list, pop it from the
        dict and then call itself again

        Parameters
        ----------
        dict: This is the dict of countries data

        Returns
        -------
        NOne
        """
        if len(dict) == 0:
            return self.order_place_list
        highest = self.get_highest_country(dict)
        self.order_place_list.append(highest[0])
        dict.pop(highest[0])
        self.get_order_of_overall(dict)

    def get_highest_country(self, dict):
        """
        This gets the country that did the best overall in the dict
        Parameters
        ----------
        dict: This is the dict of countries data

        Returns
        -------
        highest: This is the country tht did the best
        """
        highest = ['', -1]
        for country in dict:

            if dict[country][-1] > highest[1]:
                highest = [country, dict[country][-1]]
            elif dict[country][-1] == highest[1]:
                highest_dict = self.second_dict_of_countries_place_came[highest[0]]
                if dict[country][-2] > highest_dict[-2]:
                    highest = [country, dict[country][-1]]
                elif dict[country][-2] == highest_dict[-2]:
                    if dict[country][-3] > highest_dict[-3]:
                        highest = [country, dict[country][-1]]
                    elif dict[country][-3] == highest_dict[-3]:
                        if dict[country][-4] > highest_dict[-4]:
                            highest = [country, dict[country][-1]]
                        elif dict[country][-4] == highest_dict[-4]:
                            if dict[country][-5] > highest_dict[-5]:
                                highest = [country, dict[country][-1]]
        return highest

    def get_average_goals(self):
        """
        This gets the average goals that a country scored per game overall
        Returns
        -------
        None
        """
        self.average_goals_scored_list = []
        for country in self.dict_of_countries_average_goals_scored:
            average = self.analyse.get_all_goals_and_games_played(country)
            self.dict_of_countries_average_goals_scored[country] = f'{average:.5f}'
            self.average_goals_scored_list.append([country, self.dict_of_countries_average_goals_scored[country]])

    def get_average_goals_conceded(self):
        """
        This gets the average goals that a country conceded per game overall
        Returns
        -------
        None
        """
        self.average_goals_conceded_list = []
        for country in self.dict_of_countries_average_goals_conceded:
            average = self.analyse.get_all_goals_and_games_played(country)
            self.dict_of_countries_average_goals_conceded[country] = f'{average:.5f}'
            self.average_goals_conceded_list.append([country, self.dict_of_countries_average_goals_conceded[country]])


if __name__ == '__main__':
    g = GeneralAnalysis()
    g.get_stats()
