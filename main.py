import argparse
from src.parse import parse_from_restaurants_csv, parse_from_hospital_requests_csv
parser = argparse.ArgumentParser(description='OTP Scheduler')

parser.add_argument('--capacity', '-c', required=True, help='Max global meal capacity for the week')
parser.add_argument('--max_dropoffs_per_run', type=int, default=4, help='Maximum dropoff points for any single run')
parser.add_argument('--min_meals_per_run', type=int, default=50, help='Minimum meals for any single run')
parser.add_argument('--restaurants', required=True, type=str, help='Restaurants CSV file')
parser.add_argument('--hospitals', required=True, type=str, help='Hospital Orders CSV file')
parser.add_argument('--vip_hospitals', type=str, help='VIP Hospital Orders CSV file')
parser.add_argument('--output_file', '-o', type=str, help='Location of file to write scheduler results to')

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    print(parse_from_restaurants_csv(args.restaurants))
    print(parse_from_hospital_requests_csv(args.hospitals))
