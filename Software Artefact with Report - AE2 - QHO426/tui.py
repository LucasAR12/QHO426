from Process import (
    count_reviews_by_park_and_location,
    get_reviews_by_park,
    average_rating_by_park_and_year,
    average_rating_by_park_and_location
)

def show_data_menu(data):
    while True:
        print("\nPlease enter one of the following options:\n")
        print("[A] Most Reviewed Parks")
        print("[B] Average Scores")
        print("[C] Park Ranking by Nationality")
        print("[D] Most Popular Month by Park")
        print("[BACK] Return to Main Menu")

        choice = input("Your selection: ").strip().upper()

        if choice == 'A':
            park = input("Enter park name: ").strip()
            reviews = get_reviews_by_park(data, park)
            print(f"\nReviews for park '{park.lower()}':")
            if reviews:
                for r in reviews[:10]:  # show max 10 reviews to avoid flooding
                    print(f"Review_ID: {r[0]}, Rating: {r[1]}, Year_Month: {r[2]}, Location: {r[3]}, Branch: {r[4]}")
                if len(reviews) > 10:
                    print(f"... and {len(reviews) - 10} more reviews.")
            else:
                print("No reviews found.")
        elif choice == 'B':
            park = input("Enter park name: ").strip()
            averages = average_rating_by_park_and_year(data, park)
            if averages:
                print(f"Average rating by year for park '{park.lower()}':")
                for year, avg in sorted(averages.items()):
                    print(f"  {year}: {avg:.2f}")
            else:
                print("No data found.")
        elif choice == 'C':
            park = input("Enter park name: ").strip()
            location = input("Enter reviewer location: ").strip()
            total = count_reviews_by_park_and_location(data, park, location)
            print(f"Total reviews from {location.lower()} for park {park.lower()}: {total}")
        elif choice == 'D':
            park = input("Enter park name: ").strip()
            averages = average_rating_by_park_and_location(data, park)
            if averages:
                print(f"Average rating by reviewer location for park '{park.lower()}':")
                for loc, avg in sorted(averages.items()):
                    print(f"  {loc}: {avg:.2f}")
            else:
                print("No data found.")
        elif choice == 'BACK':
            break
        else:
            print("Invalid option, try again.")
