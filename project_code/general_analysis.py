from project_code.analyse_results import Analyse


class GeneralAnalysis:
    def __init__(self):
        self.order_place_list = []
        self.highest = ['', 0]
        self.analyse = Analyse()
        self.dict_of_countries_place_came = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                             'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                             'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0,
                                             'Iceland': 0,
                                             'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                             'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                             'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                             'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

        self.dict_of_countries_average_goals_scored = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0,
                                                       'Canada': 0,
                                                       'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                                       'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0,
                                                       'Hungary': 0,
                                                       'Iceland': 0,
                                                       'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                                       'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0,
                                                       'Portugal': 0,
                                                       'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0,
                                                       'Ukraine': 0,
                                                       'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

        self.dict_of_countries_average_goals_conceded = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0,
                                                         'Canada': 0,
                                                         'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                                         'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0,
                                                         'Hungary': 0, 'Iceland': 0,
                                                         'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                                         'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0,
                                                         'Portugal': 0,
                                                         'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0,
                                                         'Ukraine': 0,
                                                         'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

        self.second_dict_of_countries_place_came = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0,
                                                    'Canada': 0,
                                                    'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                                    'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0,
                                                    'Iceland': 0,
                                                    'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                                    'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0,
                                                    'Portugal': 0,
                                                    'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                                    'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

    def get_stats(self):
        self.get_average_goals()
        self.get_average_goals_conceded()
        self.get_dict_with_data()
        self.order_place_dict()
        print('hello')
        return self.order_place_list,self.dict_of_countries_average_goals_scored, self.dict_of_countries_average_goals_conceded

    def get_dict_with_data(self):
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

    def order_place_dict(self):
        for i in range(len(self.dict_of_countries_place_came)):
            highest = self.get_highest_country()
            self.dict_of_countries_place_came.pop(highest[0])
            self.order_place_list.append(highest[0])

    def get_highest_country(self):
        highest = ['', -1]
        for country in self.dict_of_countries_place_came:

            if self.dict_of_countries_place_came[country][-1] > highest[1]:
                highest = [country, self.dict_of_countries_place_came[country][-1]]
            elif self.dict_of_countries_place_came[country][-1] ==highest[1]:
                highest_dict = self.second_dict_of_countries_place_came[highest[0]]
                if self.dict_of_countries_place_came[country][-2] > highest_dict[-2]:
                    highest = [country, self.dict_of_countries_place_came[country][-1]]
                elif self.dict_of_countries_place_came[country][-2] == highest_dict[-2]:
                    if self.dict_of_countries_place_came[country][-3] > highest_dict[-3]:
                        highest = [country, self.dict_of_countries_place_came[country][-1]]
                    elif self.dict_of_countries_place_came[country][-3] == highest_dict[-3]:
                        if self.dict_of_countries_place_came[country][-4] > highest_dict[-4]:
                            highest = [country, self.dict_of_countries_place_came[country][-1]]
                        elif self.dict_of_countries_place_came[country][-4] == highest_dict[-4]:
                            if self.dict_of_countries_place_came[country][-5] > highest_dict[-5]:
                                highest = [country, self.dict_of_countries_place_came[country][-1]]
        return highest

    def get_average_goals(self):
        for country in self.dict_of_countries_average_goals_scored:
            average = self.analyse.get_all_goals_and_games_played(country)
            self.dict_of_countries_average_goals_scored[country] = average
        self.dict_of_countries_average_goals_scored = sorted(self.dict_of_countries_average_goals_scored)

    def get_average_goals_conceded(self):
        for country in self.dict_of_countries_average_goals_conceded:
            average = self.analyse.get_all_goals_and_games_played(country)
            self.dict_of_countries_average_goals_conceded[country] = average
        self.dict_of_countries_average_goals_conceded = sorted(self.dict_of_countries_average_goals_conceded)


if __name__ == '__main__':
    g = GeneralAnalysis()
    g.get_stats()
