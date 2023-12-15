def car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car_toyota = car('toyota', 'corola',  
                color = 'black', 
                production_year = 2018)

print(car_toyota)
    