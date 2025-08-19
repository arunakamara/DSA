def get_temperatures(days):


    temperatures = []
    for i in range(days):
        temp = int(input(f"Enter Day{i+1} high temperature: "))
        temperatures.append(temp)
    
    return temperatures

def get_days_above_avg(temp_list, avg):
    days_above_avg = [ temp_list.index(temp)+1 for temp in temp_list if temp > avg ]
    return days_above_avg

def main():
    days = int(input("Enter the number of days: "))
    temp_list = get_temperatures(days)    
    avg = sum(temp_list) / days

    days_above_avg = get_days_above_avg(temp_list, avg)
    print("Average:",avg)
    for day in days_above_avg:
        print(f"Day {day} is greater than average")

if __name__ == "__main__":
    main()