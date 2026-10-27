import sympy as sp
import matplotlib.pyplot as plt

# X and y.

X = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20]

y = [52, 61, 67, 72, 78, 83, 86, 89, 92, 93]

# current slope and intercept.

slope = 0
intercept = 0

iterations = 0

step_size_intercept = 0
step_size_slope = 0

learning_rate = 0.006

cumulative_derivative_intercept = 0
cumulative_derivative_slope = 0

y_symbol = sp.symbols("y_symbol")
m = sp.symbols("m")
x = sp.symbols("x")
b = sp.symbols("b")

f = (y_symbol-(m*x+b))**2
df_db = sp.diff(f, b)
df_dm = sp.diff(f, m)

max_steps = 1000; min_step_size = 0.001

predicted_y = []

def predict_values():
    for t in range(0, len(X), 1):
        predicted_y.append(slope * X[t] + intercept)

predict_values()

def plot_graph(v, t):

    plt.plot(v, t, marker='o', color='red', linestyle='-', linewidth=0.4)
    plt.xlabel('hours studied')
    plt.ylabel('marks gotten')
    plt.title("hours studied vs marks gotten")
    plt.scatter(X, y)
    plt.show()

plot_graph(X, predicted_y)

while iterations < max_steps:

    for i in range(0, len(y), 1): # intercept part.

        print("df/db = ", end="")
        df_current_intercept = df_db.subs({

            y_symbol: y[i],
            m: slope,
            x: X[i],
            b: intercept

        })

        print(df_current_intercept, end=" ")

        cumulative_derivative_intercept += df_current_intercept

        print("df/dm = ", end="")
        df_current_slope = df_dm.subs({

            y_symbol: y[i],
            m: slope,
            x: X[i],
            b: intercept

        })

        print(df_current_slope, end=" | ")

        cumulative_derivative_slope += df_current_slope

    cumulative_derivative_intercept /= len(X)
    cumulative_derivative_slope /= len(X)

    print("\nCUMULATIVE INTERCEPT DERIVATIVE -> ", cumulative_derivative_intercept)
    print("\nCUMULATIVE SLOPE DERIVATIVE -> ", cumulative_derivative_slope)

    # find the new intercept.

    step_size_intercept = cumulative_derivative_intercept * learning_rate # INTERCEPT

    step_size_slope = cumulative_derivative_slope * learning_rate # SLOPE

    print("\nSTEP SIZE INTERCEPT->", step_size_intercept)
    print("\nSTEP SIZE SLOPE->", step_size_slope)

    if abs(step_size_intercept) < min_step_size and abs(step_size_slope) < min_step_size:
        break

    intercept = intercept - step_size_intercept
    slope = slope - step_size_slope

    print("\nNEW INTERCEPT -> ", intercept)
    print("\nNEW SLOPE     -> ", slope)

    predicted_y = []

    predict_values()

    iterations += 1
    cumulative_derivative_intercept = 0
    cumulative_derivative_slope = 0

print("\n\n-----------------------")
print("\n\nFINAL INTERCEPT ->", intercept) # after leaving while loop
print("\n\nFINAL SLOPE ->", slope) # after leaving while loop
print("\n\nNUMBER OF ITERATIONS -> ", iterations)
print("\n\n-----------------------")

plot_graph(X, predicted_y)

input_x = float(input("\n\nEnter hours studied  : "))

def predict_input(input_x_value):

    result_y = slope * input_x_value + intercept

    return result_y

print(predict_input(input_x), "marks!")
