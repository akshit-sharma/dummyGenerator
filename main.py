import pandas as pd

def writeBuffer(file, buffer):
    with open(file, "w") as f:
        f.write(buffer)
        f.write('\n')

def main():
    dummy_list = []
    dummy_list.append(["Adam", 16, 200.0, "USA"])
    dummy_list.append(["Bob", 17, 300.0, "USA"])
    dummy_list.append(["Cathy", 18, 400.0, "USA"])
    dummy_list.append(["David", 19, 500.0, "USA"])
    dummy_list.append(["Eve", 20, 600.0, "USA"])

    df = pd.DataFrame(dummy_list, columns=["Name", "Age", "Salary", "Country"])
    filename = "dummy.json"
    writeBuffer(filename, df.to_json(orient="table", index=False))
    filename = "dummy_index.json"
    writeBuffer(filename, df.to_json(orient="table"))

if __name__ == "__main__":
    main()
