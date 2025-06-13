def load_csv_data(filepath):
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        next(f)  # skip header
        for line in f:
            row = line.strip().split(',')
            if len(row) >= 5:
                data.append(row)
    return data

def count_reviews_by_park_and_location(data, park_substring, location_substring):
    count = 0
    park_substring = park_substring.lower()
    location_substring = location_substring.lower()
    for row in data:
        branch = row[4].lower()
        reviewer_location = row[3].lower()
        if park_substring in branch and location_substring in reviewer_location:
            count += 1
    return count

def get_reviews_by_park(data, park_substring):
    park_substring = park_substring.lower()
    reviews = []
    for row in data:
        branch = row[4].lower()
        if park_substring in branch:
            reviews.append(row)
    return reviews

def average_rating_by_park_and_year(data, park_substring):
    park_substring = park_substring.lower()
    ratings_by_year = {}
    counts_by_year = {}

    for row in data:
        branch = row[4].lower()
        if park_substring in branch:
            year_month = row[2]
            year = year_month.split('-')[0]
            rating = int(row[1])
            ratings_by_year[year] = ratings_by_year.get(year, 0) + rating
            counts_by_year[year] = counts_by_year.get(year, 0) + 1

    averages = {}
    for year in ratings_by_year:
        averages[year] = ratings_by_year[year] / counts_by_year[year]
    return averages

def average_rating_by_park_and_location(data, park_substring):
    park_substring = park_substring.lower()
    ratings_by_location = {}
    counts_by_location = {}

    for row in data:
        branch = row[4].lower()
        if park_substring in branch:
            location = row[3].lower()
            rating = int(row[1])
            ratings_by_location[location] = ratings_by_location.get(location, 0) + rating
            counts_by_location[location] = counts_by_location.get(location, 0) + 1

    averages = {}
    for loc in ratings_by_location:
        averages[loc] = ratings_by_location[loc] / counts_by_location[loc]
    return averages
