print()
# Entity, Code, Year, Life expectancy
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

        # life expectancy
        life_expectancy = life_details_clean[3]
        life_expectancy_split = life_expectancy.split()
        life_expectancy_strip = life_expectancy.strip(",")
        # print(life_expectancy, end="")
        print(life_expectancy_split, end="")
        # print(life_expectancy_strip, end="")


       




