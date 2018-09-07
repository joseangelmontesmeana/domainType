# -*- coding: utf-8 -*-
from app.domains import Domains
import argparse


DOMAINS_FILE = "files/input/domains_for_scan.txt"
domains = Domains(DOMAINS_FILE)


parser = argparse.ArgumentParser()
parser.add_argument("run_type", help="select run type]", choices=["view", "scan", "train", "predict"])
args = parser.parse_args()

if args.run_type == "view":
    print(domains.get_head(2))
    print(domains.get_range(0, 3))

elif args.run_type == "scan":
    domains.scan()
    print("scan")

elif args.run_type == "train":
    print("train")

elif args.run_type == "predict":
    print("predict")


