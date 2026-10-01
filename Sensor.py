# Sensor Dataset Quality and Outlier Profiler

def get_sensor_data():
    # Gets input from the user until they type 'done'
    raw_inputs = []
    valid_data = []
    
    print("Enter sensor readings (type 'done' to stop):")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break

        raw_inputs.append(user_input)

        try:
            value = float(user_input)
            valid_data.append(value)
        except:
            print("Invalid input, recorded as non-numeric.")

    return raw_inputs, valid_data


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


def get_status(raw_inputs, valid_data, outliers):
    # Determines the dataset status based on data quality and outliers
    if len(valid_data) == 0:
        return "NO VALID DATA"
    
    completeness = (len(valid_data) / len(raw_inputs)) * 100
    
    if completeness == 100 and len(outliers) == 0:
        return "READY"
    else:
        return "NEEDS REVIEW"


def print_report(raw_inputs, data, mean, median, std_dev, outliers, status):
    # Prints the final results
    completeness = (len(data) / len(raw_inputs)) * 100

    print("\n==================================================")
    print(" SENSOR DATASET REPORT")
    print("==================================================")
    print(f"Total Entries: {len(raw_inputs)}")
    print(f"Valid Readings: {len(data)} ({completeness:.2f}% completeness)")
    print(f"Dataset: {data}")

    print("--------------------------------------------------")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

    print("--------------------------------------------------")
    if len(outliers) == 0:
        print("Outliers: None detected.")
    else:
        print(f"Warning: {len(outliers)} outlier(s) found!")
        print(f"Outliers: {outliers}")

    print("--------------------------------------------------")
    print(f"Status: {status}")
    print("==================================================")


def main():
    print("==================================================")
    print(" SENSOR DATA ENTRY")
    print("==================================================")

    raw_inputs, dataset = get_sensor_data()

    # Checks if dataset has valid numbers before doing math
    if len(dataset) == 0:
        print("\nNo valid numeric observations. Program cannot calculate required statistics.")
        print("Status: NO VALID DATA")
        return

    # Calculates everything using our functions
    mean_val = calc_mean(dataset)# Sensor Dataset Quality and Outlier Profiler

def get_sensor_data():
    # Gets input from the user until they type 'done'
    raw_inputs = []
    valid_data = []
    
    print("Enter sensor readings (type 'done' to stop):")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break

        raw_inputs.append(user_input)

        try:
            value = float(user_input)
            valid_data.append(value)
        except:
            print("Invalid input, recorded as non-numeric.")

    return raw_inputs, valid_data


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


def get_status(raw_inputs, valid_data, outliers):
    # Determines the dataset status based on data quality and outliers
    if len(valid_data) == 0:
        return "NO VALID DATA"
    
    completeness = (len(valid_data) / len(raw_inputs)) * 100
    
    if completeness == 100 and len(outliers) == 0:
        return "READY"
    else:
        return "NEEDS REVIEW"


def print_report(raw_inputs, data, mean, median, std_dev, outliers, status):
    # Prints the final results
    completeness = (len(data) / len(raw_inputs)) * 100

    print("\n==================================================")
    print(" SENSOR DATASET REPORT")
    print("==================================================")
    print(f"Total Entries: {len(raw_inputs)}")
    print(f"Valid Readings: {len(data)} ({completeness:.2f}% completeness)")
    print(f"Dataset: {data}")

    print("--------------------------------------------------")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

    print("--------------------------------------------------")
    if len(outliers) == 0:
        print("Outliers: None detected.")
    else:
        print(f"Warning: {len(outliers)} outlier(s) found!")
        print(f"Outliers: {outliers}")

    print("--------------------------------------------------")
    print(f"Status: {status}")
    print("==================================================")


def main():
    print("==================================================")
    print(" SENSOR DATA ENTRY")
    print("==================================================")

    raw_inputs, dataset = get_sensor_data()

    # Checks if dataset has valid numbers before doing math
    if len(dataset) == 0:
        print("\nNo valid numeric observations. Program cannot calculate required statistics.")
        print("Status: NO VALID DATA")
        return

    # Calculates everything using our functions
    mean_val = calc_mean(dataset)
    median_val = calc_median(dataset)
    std_dev_val = calc_std_dev(dataset, mean_val)
    outliers = find_outliers(dataset, mean_val, std_dev_val)
    status = get_status(raw_inputs, dataset, outliers)

    # Shows the report
    print_report(raw_inputs, dataset, mean_val, median_val, std_dev_val, outliers, status)


main(
    median_val = calc_median(dataset)
    std_dev_val = calc_std_dev(dataset, mean_val)
    outliers = find_outliers(dataset, mean_val, std_dev_val)
    status = get_status(raw_inputs, dataset, outliers)

    # Shows the report
    print_report(raw_inputs, dataset, mean_val, median_val, std_dev_val, outliers, status)


main()
