import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Disneyland_reviews.csv", encoding="ISO-8859-1")

def visualise_data_menu():
    while True:
        print("\nVisualise Data Menu")
        print("[A] Pie chart of number of reviews per park")
        print("[B] Bar chart of average review scores per park")
        print("[C] Top 10 locations with highest average rating for a selected park")
        print("[D] Average rating per month for a selected park")
        print("[X] Return to main menu")
        choice = input("Please enter your choice: ").upper()

        if choice == 'A':
            pie_chart_reviews_per_park()
        elif choice == 'B':
            bar_chart_average_scores()
        elif choice == 'C':
            top_10_locations_by_park()
        elif choice == 'D':
            average_rating_by_month()
        elif choice == 'X':
            break
        else:
            print("Invalid choice, please try again.")

def pie_chart_reviews_per_park():
    counts = df['Branch'].value_counts()
    counts.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Number of Reviews per Park")
    plt.ylabel("")
    plt.show()

def bar_chart_average_scores():
    means = df.groupby("Branch")["Rating"].mean()
    means.plot.bar()
    plt.title("Average Review Scores per Park")
    plt.xlabel("Park")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.show()

def top_10_locations_by_park():
    park = input("Enter the name of the park (e.g., Disneyland_HK): ")
    filtered = df[df["Branch"] == park]
    top_locations = filtered.groupby("Reviewer_Location")["Rating"].mean().sort_values(ascending=False).head(10)
    top_locations.plot.bar()
    plt.title(f"Top 10 Locations with Highest Average Rating for {park}")
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.show()

def average_rating_by_month():
    park = input("Enter the name of the park (e.g., Disneyland_HK): ")
    filtered = df[df["Branch"] == park].copy()

    filtered['Year_Month'] = pd.to_datetime(filtered['Year_Month'], errors='coerce')
    filtered = filtered.dropna(subset=['Year_Month'])

    filtered['Month'] = filtered['Year_Month'].dt.month

    month_avg = filtered.groupby("Month")["Rating"].mean().reindex(range(1, 13))

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.bar(month_names, month_avg)
    plt.title(f"Average Rating per Month for {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.show()
