def sum_weights(w1, w2):
    return w1 + w2

def calc_avg_weight(w1, w2):
    return sum_weights(w1, w2) / 2

def run():
    print("What is the weight of the person?")
    w1 = float(input())
    print("What is the weight of their inventory?")
    w2 = float(input())
    print("What would you like to calculate (sum or average)?")
    choice = input()
    if choice == "sum":
        print("The sum of weights is", sum_weights(w1, w2))
    elif choice == "average":
        print("The average weight is", calc_avg_weight(w1, w2))

run()
