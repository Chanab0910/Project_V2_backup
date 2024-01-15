from analyse_results import Analyse

class GeneralAnalysis:
    def __init__(self):
        self.analyse = Analyse()
        self.dict_of_countries = {'Argentina': 0, 'Australia': 0, 'Austria': 0, 'Belgium': 0, 'Canada': 0,
                                     'Croatia': 0, 'Czech Republic': 0, 'Denmark': 0,
                                     'England': 0, 'Finland': 0, 'France': 0, 'Germany': 0, 'Hungary': 0, 'Iceland': 0,
                                     'Ireland': 0, 'Italy': 0, 'Mexico': 0, 'Ghana': 0,
                                     'Netherlands': 0, 'Morocco': 0, 'Norway': 0, 'Poland': 0, 'Portugal': 0,
                                     'Romania': 0, 'Scotland': 0, 'Spain': 0, 'Sweden': 0, 'Ukraine': 0,
                                     'USA': 0, 'Wales': 0, 'Japan': 0, 'China': 0}

    def get_final_result(self):
        for country in self.dict_of_countries:
            final_num = self.analyse.furthest_got_and_average_place(country)
            self.dict_of_countries[country] = final_num
        print(self.mergeSort(self.dict_of_countries))

    def mergeSort(self,ar_list):
        if len(ar_list) > 1:
            mid = len(ar_list) // 2
        left = ar_list[:mid]
        right = ar_list[mid:]
        # Recursive call on each half
        self.mergeSort(left)
        self.mergeSort(right)
        # Two iterators for traversing the left and right half
        i = 0
        j = 0
        # Iterator for the main list
        k = 0


        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                ar_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                ar_list[k] = right[j]
                j += 1
                k += 1
                # For all the remaining values
            while i < len(left):
                ar_list[k] = left[i]
                i += 1
                k += 1
        while j < len(right):
            ar_list[k] = right[j]
            j += 1
            k += 1
        ar_list = [12, 7, 2, 9, 4, 15, 5]
        self.mergeSort(ar_list)
        print(ar_list)


if __name__ == '__main__':
    g = GeneralAnalysis()
    g.get_final_result()
