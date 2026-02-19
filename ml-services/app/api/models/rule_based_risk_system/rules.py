from datetime import datetime
def Route_Deviation(planned_route,threshold):
    #threshold is the metres deviated from planned route
    deviation=planned_route-threshold
    if(deviation>1500):
        return 100
    elif(deviation>900 and deviation<1500):
        return 70
    elif(deviation>500 and deviation<900):
        return 40
    else:
        return 10


def risky_zones(current_zone,review):
    review_rating={"Good":4,
                   "Moderate":3,
                   "Bad":2}
    zone_types={"Safe":10,
                "Moderate":40,
                "High":70,
                "Restricted":90}
    base_risk=zone_types.get(current_zone,25)
    base_review_value=review_rating.get(review,3)
    review_impact=(base_review_value/5)*30
    final_risk=base_risk+review_impact
    return min(final_risk,100)

def Time_gap(curfew_hrs):
    present=datetime.now()
    t=present.strftime("%H:%M:%S")
    if present.hour >= 21 and present.hour <=5:
        return 40
    elif curfew_hrs >0:
        return 50
    else:
        return 10

def inactivity_risk(time_gap):
    if time_gap > 0 and time_gap < 0.5:
        return 10
    elif time_gap >0.5 and time_gap <1:
        return 25
    elif time_gap >1 and time_gap <3:
        return 35
    else:
        return 50

def acceleration(acc):
    if acc > 0 and acc <= 30:
        return 20
    elif acc > 30 and acc <= 50:
        return 40
    else:
        return 50
    






