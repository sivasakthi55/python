import requests
def get_live_train_status(trainno):
    base_url="https://rappid.in/apis/train.php?train_no={}".format(trainno)
    response=requests.get(base_url)
    data=response.json()
    return data

train_number=22658
train_status=get_live_train_status(train_number)

print("-------------------")
print("\t\ttrain name:",train_status["train_name"])
print("------------------------")
for station_info in train_status["data"]:
    if station_info["is_current_station"]:
        print("now station \t\t:",station_info["station_name"])
        print("distance from the starting\t:",station_info["distance"])
        print("timing\t\t\t:",station_info["timing"])
        print("delay\t\t:",station_info["delay"])
        print("platform no\t\t:",station_info["platform"])
        print("halt timimg\t\t:",station_info["halt"])
    else:
        print(station_info["station_name"])

print("-----------------------")
print("\t\tmessage\t\t:",train_status["message"])
print("\t\tmessage updated:",train_status["updated_time"])
print("-------------------------") 
    
   


