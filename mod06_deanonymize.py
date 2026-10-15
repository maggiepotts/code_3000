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

    results = pd.DataFrame(columns=["anon_id", "matched_name"])

    for age, zip3, gender, id in zip(anon_df["age"], anon_df["zip3"], anon_df["gender"], anon_df["anon_id"]):
        for a, z, g, name in zip(aux_df["age"], aux_df["zip3"], aux_df["gender"], aux_df["name"]):
            
            if ((age == a) and (zip3 == z) and (gender == g)):
            
                new_row = pd.DataFrame([{"anon_id": id, "matched_name": name}])
                results = pd.concat([results, new_row], ignore_index=True)

                break

    return results


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return (len(matches_df) / len(anon_df))
