from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)

    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes

class DailyTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    iata = db.Column(db.String(4))
    #time = db.Column(db.Time)
    temp = db.Column(db.Integer)

    def __init__(self, date, iata, temp):
        self.date = date
        self.iata = iata
        #self.time = time
        self.temp = temp

    def __repr__(self):
        return '<DailyTemp %r-%r-%r>' % self.iata, self.date, self.temp


class WeatherDelay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    iata = db.Column(db.String(4))
    delay = db.Column(db.String(6))
    reason = db.Column(db.String(64))
    temp = db.Column(db.String(64))
    visibility = db.Column(db.String(64))
    weather = db.Column(db.String(64))
    wind = db.Column(db.String(64))
    credit = db.Column(db.String(64))
    updated = db.Column(db.String(64))
    url = db.Column(db.String(64))

    def __init__(self, date, time, iata, delay, reason, temp, visibility, weather,
                 wind, credit, updated, url):
        self.date = date
        self.time = time
        self.iata = iata
        self.delay = delay
        self.reason = reason
        self.temp = temp
        self.visibility = visibility
        self.weather = weather
        self.wind = wind
        self.credit = credit
        self.updated = updated
        self.url = url

    def __repr__(self):
        return '<DailyWeatherTemp %r-%r-%r-%r>' % self.iata, self.date, self.temp, self.delay



# class DailyDelays(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Date)
#     iata = db.Column(db.String(4))
#     delay = db.Column(db.Integer)
#     reason_airline_req = db.Column(db.Integer)
#     reason_airline_req_ = db.Column(db.Integer)
#     reason_dal_and_dal_subs_only = db.Column(db.Integer)
#     reason_dal_and_sub_s_only = db.Column(db.Integer)
#     reason_eq_faa = db.Column(db.Integer)
#     reason_equipment_outage = db.Column(db.Integer)
#     reason_equipment_outage__airline_computer_issue = db.Column(db.Integer)
#     reason_other_other = db.Column(db.Integer)
#     reason_other_staffing = db.Column(db.Integer)
#     reason_other_staffing_ = db.Column(db.Integer)
#     reason_other_fire = db.Column(db.Integer)
#     reason_other_wake_turb = db.Column(db.Integer)
#     reason_runway_construction = db.Column(db.Integer)
#     reason_rwy_construction = db.Column(db.Integer)
#     reason_rwy_multi_taxi = db.Column(db.Integer)
#     reason_rwy_noise_abatement = db.Column(db.Integer)
#     reason_rwy_obstruction = db.Column(db.Integer)
#     reason_rwy_rwy_change_operational_advantage = db.Column(db.Integer)
#     reason_rwy_rwy_change_operational_necessity = db.Column(db.Integer)
#     reason_tm_initiatives_other_havana = db.Column(db.Integer)
#     reason_tm_initiatives_esp__havana_restriction = db.Column(db.Integer)
#     reason_tm_initiatives_esp_vol = db.Column(db.Integer)
#     reason_tm_initiatives_minit_havana_airspace = db.Column(db.Integer)
#     reason_tm_initiatives_minit_vol = db.Column(db.Integer)
#     reason_tm_initiatives_mit_vol = db.Column(db.Integer)
#     reason_tm_initiatives_mit_wx = db.Column(db.Integer)
#     reason_tm_initiatives_metering_vol = db.Column(db.Integer)
#     reason_tm_initiatives_other_havana_ = db.Column(db.Integer)
#     reason_tm_initiatives_other_vol = db.Column(db.Integer)
#     reason_tm_initiatives_stop_wx = db.Column(db.Integer)
#     reason_tm_initiatives_swap_wx = db.Column(db.Integer)
#     reason_vol__dep_vol_arr_cro = db.Column(db.Integer)
#     reason_vol_compacted_demand = db.Column(db.Integer)
#     reason_vol_multi_taxi = db.Column(db.Integer)
#     reason_vol_volume = db.Column(db.Integer)
#     reason_volume_compacted_demand = db.Column(db.Integer)
#     reason_volume_multi_taxi = db.Column(db.Integer)
#     reason_volume_volume = db.Column(db.Integer)
#     reason_weather_fog = db.Column(db.Integer)
#     reason_weather_low_ceilings = db.Column(db.Integer)
#     reason_weather_low_visibility = db.Column(db.Integer)
#     reason_weather_snow_ice = db.Column(db.Integer)
#     reason_weather_thunderstorms = db.Column(db.Integer)
#     reason_weather_wind = db.Column(db.Integer)
#     reason_weather_thunderstorms_ = db.Column(db.Integer)
#     reason_wx_thunderstorms = db.Column(db.Integer)
#     reason_wx_config_chg = db.Column(db.Integer)
#     reason_wx_fog = db.Column(db.Integer)
#     reason_wx_low_ceilings = db.Column(db.Integer)
#     reason_wx_thunderstorms_ = db.Column(db.Integer)
#     reason_wx_wind = db.Column(db.Integer)
#     type_arrival = db.Column(db.Integer)
#     type_departure = db.Column(db.Integer)
#     type_ground_delay = db.Column(db.Integer)
#     type_ground_stop = db.Column(db.Integer)
#
#
#     def __init__(self, date, iata, temp):
#         self.date = date
#         self.iata = iata
#         self.delay = delay
#         self.reason_airline_req = reason_airline_req
#         self.reason_airline_req_ = reason_airline_req_
#         self.reason_dal_and_dal_subs_only = reason_dal_and_dal_subs_only
#         self.reason_dal_and_sub_s_only = reason_dal_and_sub_s_only
#         self.reason_eq_faa = reason_eq_faa
#         self.reason_equipment_outage = reason_equipment_outage
#         self.reason_equipment_outage__airline_computer_issue = reason_equipment_outage__airline_computer_issue
#         self.reason_other_other = reason_other_other
#         self.reason_other_staffing = reason_other_staffing
#         self.reason_other_staffing_ = reason_other_staffing_
#         self.reason_other_fire = reason_other_fire
#         self.reason_other_wake_turb = reason_other_wake_turb
#         self.reason_runway_construction = reason_runway_construction
#         self.reason_rwy_construction = reason_rwy_construction
#         self.reason_rwy_multi_taxi = reason_rwy_multi_taxi
#         self.reason_rwy_noise_abatement = reason_rwy_noise_abatement
#         self.reason_rwy_obstruction = reason_rwy_obstruction
#         self.reason_rwy_rwy_change_operational_advantage = reason_rwy_rwy_change_operational_advantage
#         self.reason_rwy_rwy_change_operational_necessity = reason_rwy_rwy_change_operational_necessity
#         self.reason_tm_initiatives_other_havana = reason_tm_initiatives_other_havana
#         self.reason_tm_initiatives_esp__havana_restriction = reason_tm_initiatives_esp__havana_restriction
#         self.reason_tm_initiatives_esp_vol = reason_tm_initiatives_esp_vol
#         self.reason_tm_initiatives_minit_havana_airspace = reason_tm_initiatives_minit_havana_airspace
#         self.reason_tm_initiatives_minit_vol = reason_tm_initiatives_minit_vol
#         self.reason_tm_initiatives_mit_vol = reason_tm_initiatives_mit_vol
#         self.reason_tm_initiatives_mit_wx = reason_tm_initiatives_mit_wx
#         self.reason_tm_initiatives_metering_vol = reason_tm_initiatives_metering_vol
#         self.reason_tm_initiatives_other_havana_ = reason_tm_initiatives_other_havana_
#         self.reason_tm_initiatives_other_vol = reason_tm_initiatives_other_vol
#         self.reason_tm_initiatives_stop_wx = reason_tm_initiatives_stop_wx
#         self.reason_tm_initiatives_swap_wx = reason_tm_initiatives_swap_wx
#         self.reason_vol__dep_vol_arr_cro = reason_vol__dep_vol_arr_cro
#         self.reason_vol_compacted_demand = reason_vol_compacted_demand
#         self.reason_vol_multi_taxi = reason_vol_multi_taxi
#         self.reason_vol_volume = reason_vol_volume
#         self.reason_volume_compacted_demand = reason_volume_compacted_demand
#         self.reason_volume_multi_taxi = reason_volume_multi_taxi
#         self.reason_volume_volume = reason_volume_volume
#         self.reason_weather_fog = reason_weather_fog
#         self.reason_weather_low_ceilings = reason_weather_low_ceilings
#         self.reason_weather_low_visibility = reason_weather_low_visibility
#         self.reason_weather_snow_ice = reason_weather_snow_ice
#         self.reason_weather_thunderstorms = reason_weather_thunderstorms
#         self.reason_weather_wind = reason_weather_wind
#         self.reason_weather_thunderstorms_ = reason_weather_thunderstorms_
#         self.reason_wx_thunderstorms = reason_wx_thunderstorms
#         self.reason_wx_config_chg = reason_wx_config_chg
#         self.reason_wx_fog = reason_wx_fog
#         self.reason_wx_low_ceilings = reason_wx_low_ceilings
#         self.reason_wx_thunderstorms_ = reason_wx_thunderstorms_
#         self.reason_wx_wind = reason_wx_wind
#         self.type_arrival = type_arrival
#         self.type_departure = type_departure
#         self.type_ground_delay = type_ground_delay
#         self.type_ground_stop = type_ground_stop
#
#     def __repr__(self):
#         return '<DailyDelay %r-%r-%r>' % self.iata, self.date, self.delay
