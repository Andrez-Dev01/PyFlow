from src.reader import load_csv


def main():
    data = load_csv("data/dragon_ball_z.csv")
    print(data)

if __name__ == "__main__":
    main()
