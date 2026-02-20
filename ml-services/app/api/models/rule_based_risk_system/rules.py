
from datetime import datetime


def route_deviation(actual_deviation_meters):
    if actual_deviation_meters > 1500:
        return 100
    elif 900 < actual_deviation_meters <= 1500:
        return 70
    elif 500 < actual_deviation_meters <= 900:
        return 40
    else:
        return 10



def risky_zones(current_zone, review):
    review_rating = {
        "Good": 4,
        "Moderate": 3,
        "Bad": 2
    }

    zone_types = {
        "Safe": 10,
        "Moderate": 40,
        "High": 70,
        "Restricted": 90
    }

    base_risk = zone_types.get(current_zone, 25)
    review_score = review_rating.get(review, 3)

    # Lower review → higher risk
    review_impact = (5 - review_score) * 8

    final_risk = base_risk + review_impact
    return min(final_risk, 100)



def time_risk(curfew_hrs):
    hour = datetime.now().hour

    if hour >= 21 or hour <= 5:
        return 40
    elif curfew_hrs > 0:
        return 50
    else:
        return 10



def inactivity_risk(time_gap_hours):
    if 0 < time_gap_hours <= 0.5:
        return 10
    elif 0.5 < time_gap_hours <= 1:
        return 25
    elif 1 < time_gap_hours <= 3:
        return 35
    else:
        return 50



def acceleration_risk(acc):
    acc = abs(acc)

    if acc <= 30:
        return 20
    elif acc <= 50:
        return 40
    else:
        return 70


def speed_risk(speed, zone_type):
    speed = max(speed, 0)

    # Suspicious slow movement
    if zone_type in ["High", "Restricted"] and speed < 5:
        return 60

    # Overspeed
    if speed > 80:
        return 70

    return 20



def gps_signal_risk(signal_lost_seconds):
    if signal_lost_seconds > 120:
        return 80
    elif signal_lost_seconds > 30:
        return 50
    else:
        return 10



def device_risk(battery_percent, network_status):
    risk = 10

    if battery_percent < 10:
        risk += 50

    if not network_status:
        risk += 70

    return min(risk, 100)



def zone_duration_risk(minutes_in_zone):
    if minutes_in_zone > 30:
        return 80
    elif minutes_in_zone > 10:
        return 40
    return 10



def anomaly_risk(anomaly_score):
    anomaly_score = max(0, min(anomaly_score, 1))
    return anomaly_score * 100



def direction_change_risk(turn_count_per_min):
    if turn_count_per_min > 10:
        return 70
    elif turn_count_per_min > 5:
        return 40
    return 10



def weather_risk(condition):
    weather_map = {
        "Clear": 10,
        "Rain": 40,
        "Storm": 70,
        "Fog": 60
    }
    return weather_map.get(condition, 20)



def final_risk_score(params):
    score = (
        0.12 * params["route"] +
        0.12 * params["zone"] +
        0.08 * params["time"] +
        0.08 * params["inactivity"] +
        0.08 * params["acceleration"] +
        0.08 * params["speed"] +
        0.08 * params["gps"] +
        0.06 * params["device"] +
        0.08 * params["zone_duration"] +
        0.10 * params["anomaly"] +
        0.06 * params["direction"] +
        0.06 * params["weather"]
    )

    return round(score, 2)


def classify_risk(score):
    if score < 30:
        return "SAFE"
    elif score < 60:
        return "MEDIUM"
    elif score < 80:
        return "HIGH"
    else:
        return "CRITICAL"