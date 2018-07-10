#!/usr/bin/env python3
import csv
import collections

file_name = "emails.csv"

with open(file_name) as emailsCsvFiles:
    readCSV: object = csv.reader(emailsCsvFiles)
    emails = []
    domains = []

    # Skip header
    next(readCSV)

    for row in readCSV:
        domain = row[0].split('@')[1]
        email = row[0]

        emails.append(email)
        domains.append(domain)
    # print(emails)
    # print(domains)

    for rowDomain in emails:
        domain = rowDomain.split('@')[1]

c = counter = collections.Counter(domains)

# Show the first 10
for domain, frequency in c.most_common(10):
    print(f"{domain}: {frequency}")  # "{}: {}".format(item,count) for lower 3.6
