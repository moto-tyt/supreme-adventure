from signum_function import signum

def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i]
    return signum(z)

def main():
    print("compute output:")
    print(compute_output([0.9, -0.6, -0.5], [1.0, 1.0, 1.0]))



if __name__ == "__main__":
    main()