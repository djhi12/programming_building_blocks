print()

# Variables
year = None


with open("life-expectancy.csv") as life_expectancies:
    for life in life_expectancies:
        life_details = life.strip()
        life_details_clean = life_details.split(",")
        # print(life_details_clean)
        # for i in range(len(life_details)):
        #     print(i)
        
        # entity
        entity = life_details_clean[0]
        # print(entity)

        # code
        code = life_details_clean[1]

        # year
        year = life_details_clean[2]
        year_num = float(year)
        print(type(year_num))

        # life expectancy
        life_expectancy = life_details_clean[3]
        # print(type(life_expectancy))
        # life_expectancy_num = float(life_expectancy)
        
        # # type
        # print(type(life_expectancy_num))




