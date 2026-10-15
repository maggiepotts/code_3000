import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """

    results = []

    for age, zip3, gender, id in zip(anon_df["age"], anon_df["zip3"], anon_df["gender"], anon_df["anon_id"]):
            
        matched = aux_df[(aux_df["age"] == age) & (aux_df["zip3"] == zip3) & (aux_df["gender"] == gender)]

        if len(matched) == 1:
            results.append({"anon_id": id, "matched_name": matched.iloc[0]["name"]})

    list = pd.DataFrame(results, columns=["anon_id", "matched_name"])

    return list


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return (len(matches_df) / len(anon_df))
