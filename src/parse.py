import pandas as pd


def parse_from_restaurants_csv(filename: str):
    df = pd.read_csv(filename)
    if df.shape[1] != 24:
        raise ValueError('Wrong shape for input CSV for restaurants')

    return df


def parse_from_hospital_requests_csv(filename: str):
    df = pd.read_csv(filename)
    if df.shape[1] != 26:
        raise ValueError('Wrong shape for input CSV for hospital requests')

    return df


def parse_from_results_csv(filename: str):
    df = pd.read_csv(filename)
    if df.shape[1] != 26:
        raise ValueError('Wrong shape for input CSV for results file')

    return df


# def parse_restaurants_csv(filename: str) -> Restaurants:
#     restaurants = Restaurants
#     with open(filename, 'r') as f:
#         csv_reader = csv.reader(f)
#
#         # skip header row
#         next(csv_reader)
#
#         for row in csv_reader:
#             restaurants.append(Restaurant(*row))
#
#     return restaurants
#
#
# def parse_hospital_requests_csv(filename: str) -> Hospitals:
#     hospitals = Hospitals
#     with open(filename, 'r') as f:
#         csv_reader = csv.reader(f)
#
#         # skip header row
#         next(csv_reader)
#
#         for row in csv_reader:
#             hospitals.append(Hospital(
#                 row[0],
#                 row[1],
#                 row[2],
#                 row[3],
#                 row[4],
#                 row[5:],
#             ))
#
#     return hospitals
#
#
# def parse_results_file(filename: str) -> Results:
#     results = Results
#     with open(filename, 'r') as f:
#         csv_reader = csv.reader(f)
#
#         # skip header row
#         next(csv_reader)
#
#         for row in csv_reader:
#             it = iter(row[5:])
#             pairs = [(i, next(i)) for i in it]
#
#             results.append(HospitalAssignment(
#                 row[0],
#                 row[1],
#                 row[2],
#                 row[3],
#                 row[4],
#                 pairs,
#             ))
#
#     return results
