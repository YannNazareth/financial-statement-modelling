import pandas as pd


class FeatureExtractor:

    def __init__(self):
        # Pass configuration parameters here
        pass

    @staticmethod
    def extract_features(statement_df_dictionary: dict) -> dict:
        for statement_type, statement_df in statement_df_dictionary.items():
            if statement_type == "balance_sheet_df":
                statement_df_dictionary.update(
                    {statement_type, BalanceSheetExtractor(statement_df).extract_features()}
                )
            elif statement_type == "income_statement_df":
                statement_df_dictionary.update(
                    {statement_type, IncomeStatementExtractor(statement_df).extract_features()}
                )
            elif statement_type == "cash_flow_df":
                statement_df_dictionary.update(
                    {statement_type, CashFlowExtractor(statement_df).extract_features()}
                )
            else:
                print(f"Method: extract_features() does not recognise statement type: {statement_type}")

        return statement_df_dictionary


class BalanceSheetExtractor:

    def __init__(self, balance_sheet_df: pd.DataFrame):
        self.balance_sheet_df = balance_sheet_df
        self.features_df = pd.DataFrame()

    def extract_features(self) -> pd.DataFrame:
        return self.balance_sheet_df


class IncomeStatementExtractor:

    def __init__(self, income_statement_df: pd.DataFrame):
        self.income_statement_df = income_statement_df
        self.features_df = pd.DataFrame()

    def extract_features(self) -> pd.DataFrame:
        return self.income_statement_df


class CashFlowExtractor:

    def __init__(self, cash_flow_df: pd.DataFrame):
        self.cash_flow_df = cash_flow_df
        self.features_df = pd.DataFrame()

    def extract_features(self) -> pd.DataFrame:
        return self.cash_flow_df