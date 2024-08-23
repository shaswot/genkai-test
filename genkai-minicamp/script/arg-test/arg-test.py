import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', default="genkai", type=str)
parser.add_argument('--location', default="kyushu", type=str)
parser.add_argument('--tel', default="1234", type=int)
parser.add_argument('--zipcode', default="810000", type=int)

args= parser.parse_args()
name = args.name
location = args.location
tel = args.tel
zipcode = args.zipcode

print(f"Name: {name}")
print(f"Location: {location}")
print(f"Telephone: {tel}")
print(f"Zipcode: {zipcode}")
print("End of Program")
