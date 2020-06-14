def main():
    import os
    import pandas as pd

    filePath = "data\e-commerce"
    os.listdir(filePath)

    for i in os.listdir(filePath):
        filename = filePath + "\\" + i
        df = pd.read_csv(filename, index_col=None, encoding='utf-8')
        df.dropna(axis=0, how='any', inplace=True)
        df.to_csv(filename, encoding='utf-8', index=False)


if __name__ == "__main__":
    main()
