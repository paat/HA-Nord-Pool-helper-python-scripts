# set_low_price_status.py in <config>/python_scripts/

def device_should_be_on24(prices_by_h, price_current, price_low, hours, current_hour):
    """
    :param hours: number of hours device should be on
    :param prices_by_h: prices ordered by hour today+tomorrow
    :param price_current: current nordpool price
    :param price_low: low threshold (price when it is no point to optimize)
    :return: true if device should be turned on or false
    """
    if len(prices_by_h) <= hours:
        return True

    if len(prices_by_h) <= 24:
        prices_by_h_24 = prices_by_h
    else:
        # look in the scope of 24-hour window
        prices_by_h_24 = prices_by_h[max(0, current_hour - 12):min(current_hour + 12, len(prices_by_h) - 1)]

    prices_sorted = sorted(prices_by_h_24)
    prices_lowest = prices_sorted[:hours]
    if price_current <= prices_lowest[-1] or price_current < price_low:
        return True
    return False

# home assistant start executing here
try:
    _ = data
    _ = hass
except NameError:
    # this is needed for running unit tests
    data = []
    hass = []

if data and hass:
    # number of hours device should be turned on during 24-hour period
    number_of_hours = int(data.get('number_of_hours'))

    # low price threshold - device is always on if price is lower
    low_price = float(data.get('low_price'))

    # id of input_boolean for managing a device in Home assistant
    input_boolean_id = data.get('input_boolean_id')

    sensor_state = hass.states.get('sensor.nordpool')
    if sensor_state:
        today_prices = sensor_state.attributes.get('today')
        tomorrow_prices = sensor_state.attributes.get('tomorrow')
        prices_by_hour = today_prices + tomorrow_prices if tomorrow_prices else today_prices

        current_price = float(sensor_state.attributes.get('current_price'))

        now = datetime.now()
        current_hour = now.hour

        result = device_should_be_on24(prices_by_hour, current_price, low_price, number_of_hours, current_hour)
        hass.states.set(input_boolean_id, 'on' if result else 'off')
