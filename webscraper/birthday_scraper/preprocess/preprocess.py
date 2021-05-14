import pandas as pd


class PreProcess():
    csv_file = '../csv/birthdaycsv.csv'
    csv_with_index = '../csv/csv_with_index.csv'
    csv_with_ids_only = '../csv/csv_with_ids.csv'
    csv_df = None
    csv_with_index_df = None
    df_with_ids_only = None

    def load_csv(self):
        self.csv_df = pd.read_csv(self.csv_file)
        print(self.csv_df)

    def load_csv_with_index(self):
        self.csv_with_index_df = pd.read_csv(self.csv_with_index)

    def add_index(self):
        self.csv_df["id"] = self.csv_df.index
        ids = self.csv_df['id']
        self.csv_df.drop(labels=['id'], axis=1, inplace=True)
        self.csv_df.insert(0, 'id', ids)
        self.csv_df.to_csv(self.csv_with_index, sep=',', index=False)

    def set_ids(self):
        self.df_with_ids_only = self.csv_with_index_df[
            ['id', 'profile_url']].copy()

    def set_urls(self):
        self.df_with_ids_only['profile_url'] = self.df_with_ids_only[
            'profile_url'].str[17:]
        self.df_with_ids_only.to_csv(
            self.csv_with_ids_only, sep=',', index=False)

    def run(self):
        # self.load_csv()
        # self.add_index()
        # self.load_csv_with_index()
        # self.set_ids()
        # self.set_urls()
        pass


def main():
    PreProcess().run()


if __name__ == "__main__":
    main()
