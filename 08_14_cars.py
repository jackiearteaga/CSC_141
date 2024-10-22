def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('toyota', 'rav4', color='black', tow_package=True)

# Print dictionary to see stored information
print(car)
