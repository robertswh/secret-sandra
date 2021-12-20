import pandas as pd

def match_names(df):
    shuffled = df.sample(frac=1).reset_index(drop=True)

    shuffled['buy_for_index'] = shuffled.index + 1
    shuffled['buy_for_index'].replace(len(df), 0, inplace=True)

    return (
        shuffled[["email_address", "name"]].merge(
            shuffled[["buy_for_index", "name"]].set_index("buy_for_index"),
            left_index=True, 
            right_index=True)
        .rename(columns={"name_x":"name", "name_y":"buy_for"})
        .sort_index()
    )

if __name__ == "__main__":
    print("This aint a script")