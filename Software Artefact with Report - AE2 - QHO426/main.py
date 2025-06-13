from tui import show_data_menu
from process import load_csv_data
from visual import visualise_data_menu

def main():
    print("-" * 100)
    print("                    Disneyland Review Data Analysis Tool")
    print("-" * 100)

    data = load_csv_data("Disneyland_reviews.csv")
    print(f"\nDataset loaded successfully with {len(data)} records.\n")

    while True:
        print("\nPlease enter the letter which corresponds with your desired menu choice:")
        print("[A] View Data")
        print("[B] Visualise Data")
        print("[X] Exit")

        choice = input("Your selection: ").strip().upper()

        if choice == 'A':
            show_data_menu(data)
        elif choice == 'B':
            visualise_data_menu()
        elif choice == 'X':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
