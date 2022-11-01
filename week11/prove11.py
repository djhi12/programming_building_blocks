print()
# Entity, Code, Year, Life expectancy
# Variables
year = None
i = 0

with open("life-expectancy.csv") as life_expectancies:
    for life in life_expectancies:
        i += 1
        life_details = life.strip()
        life_detail_clean = life_details.split(",")
        # print(life_details_clean)

        # for i in range(len(life_details)):
        #     print(i)
        
        # entity
        entity = life_detail_clean[0]
        print(entity)

        # code
        code = life_detail_clean[1]

        # year
        year = life_detail_clean[2]

        # life expectancy
        life_expectancy = life_detail_clean[3]
        


       




