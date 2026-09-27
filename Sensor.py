# Sensor Dataset Quality and Outlier Profiler

def get_sensor_data():
    # Gets input from the user until they type 'done'
    data = []
    print("Enter sensor readings (type 'done' to stop):")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break

        try:
            value = float(user_input)
            data.append(value)
        except:
            print("Invalid input, please enter a number.")

    return data


def calc_mean(data):
    # Calculates average
    total = 0
    for num in data:
        total += num
    return total / len(data)


def calc_median(data):
    # Finds the middle number
    data = sorted(data)
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]


def calc_std_dev(data, mean):
    # Calculates standard deviation
    total_variance = 0
    for num in data:
        total_variance += (num - mean) ** 2

    variance = total_variance / len(data)
    return variance ** 0.5


def find_outliers(data, mean, std_dev):
    # Finds numbers that are more than 2 standard deviations away
    outliers = []

    if std_dev == 0:
        return outliers

    threshold = 2 * std_dev

    for num in data:
        distance = num - mean
        # Make distance positive
        if distance < 0:
            distance = -distance

        if distance > threshold:
            outliers.append(num)

    return outliers


def print_report(data, mean, median, std_dev, outliers):
    # Prints the final results
    print("\n==================================================")
    print(" SENSOR DATASET REPORT")
    print("==================================================")
    print(f"Total Readings: {len(data)}")
    print(f"Dataset: {data}")

    print("--------------------------------------------------")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

    print("--------------------------------------------------")
    if len(outliers) == 0:
        print("Status: CLEAN. No outliers detected.")
    else:
        print(f"Warning: {len(outliers)} outlier(s) found!")
        print(f"Outliers: {outliers}")
    print("==================================================")


def main():
    print("==================================================")
    print(" SENSOR DATA ENTRY")
    print("==================================================")

    dataset = get_sensor_data()

    # Checks if dataset is empty before doing math
    if len(dataset) == 0:
        print("No data entered. Exiting program.")
        return

    # Calculates everything using our functions
    mean_val = calc_mean(dataset)
    median_val = calc_median(dataset)
    std_dev_val = calc_std_dev(dataset, mean_val)
    outliers = find_outliers(dataset, mean_val, std_dev_val)

    # Shows the report
    print_report(dataset, mean_val, median_val, std_dev_val, outliers)

main()
