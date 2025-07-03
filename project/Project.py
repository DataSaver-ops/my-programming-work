import sys
import docx

def read_data(file_name):
    data = []
    try:
        doc = docx.Document(file_name)
        for para in doc.paragraphs:
            line = para.text.strip()
            parts = line.split(',')
            if len(parts) == 3:
                location, speed, storm = parts
                data.append((location, int(speed), storm))
            else:
                print(f"Skipping line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    return data

def calculate_statistics(data):
    highest_speed = max(data, key=lambda x: x[1])[1]
    locations_with_highest_speed = [x[0] for x in data if x[1] == highest_speed]
    average_speeds = {}
    storm_speeds = {}

    for location, speed, storm in data:
        if location not in average_speeds:
            average_speeds[location] = []
        average_speeds[location].append(speed)

        if storm not in storm_speeds:
            storm_speeds[storm] = []
        storm_speeds[storm].append(speed)

    average_speeds = {k: sum(v) / len(v) for k, v in average_speeds.items()}
    highest_average_storm = max(storm_speeds.items(), key=lambda x: sum(x[1]) / len(x[1]))[0]

    return highest_speed, locations_with_highest_speed, average_speeds, highest_average_storm

def display_results(highest_speed, locations_with_highest_speed, average_speeds, highest_average_storm):
    print(f"Highest wind speed: {highest_speed} mph")
    print(f"Locations with highest wind speed: {', '.join(locations_with_highest_speed)}")
    print("Average wind speeds by location:")
    for location, avg_speed in average_speeds.items():
        print(f"{location}: {avg_speed:.2f} mph")
    print(f"Storm with highest average wind speed: {highest_average_storm}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python project.py <data_file>")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_data(file_name)
    highest_speed, locations_with_highest_speed, average_speeds, highest_average_storm = calculate_statistics(data)
    display_results(highest_speed, locations_with_highest_speed, average_speeds, highest_average_storm)

if __name__ == "__main__":
    main()



