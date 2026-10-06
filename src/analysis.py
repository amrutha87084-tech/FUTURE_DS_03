import pandas as pd
import os

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("data/bank-additional-full.csv", sep=";")

print("===== DATASET OVERVIEW =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==========================================
# 2. OVERALL CONVERSION
# ==========================================

successful = (df["y"] == "yes").sum()
unsuccessful = (df["y"] == "no").sum()
conversion_rate = (successful / len(df)) * 100

print("\n===== OVERALL CONVERSION =====")
print("Successful conversions:", successful)
print("Unsuccessful conversions:", unsuccessful)
print("Conversion Rate: {:.2f}%".format(conversion_rate))


# ==========================================
# 3. JOB-WISE CONVERSION
# ==========================================

print("\n===== JOB-WISE CONVERSION =====")

job_conversion = pd.crosstab(
    df["job"],
    df["y"],
    normalize="index"
) * 100

print(job_conversion.round(2))


# ==========================================
# 4. CONTACT METHOD CONVERSION
# ==========================================

print("\n===== CONTACT METHOD CONVERSION =====")

contact_conversion = pd.crosstab(
    df["contact"],
    df["y"],
    normalize="index"
) * 100

print(contact_conversion.round(2))


# ==========================================
# 5. MONTH-WISE CONVERSION
# ==========================================

print("\n===== MONTH-WISE CONVERSION =====")

month_conversion = pd.crosstab(
    df["month"],
    df["y"],
    normalize="index"
) * 100

print(month_conversion.round(2))


# ==========================================
# 6. CAMPAIGN CONTACTS
# ==========================================

print("\n===== CAMPAIGN CONTACTS =====")

print(df["campaign"].describe())


# ==========================================
# 7. CONTACT FREQUENCY VS CONVERSION
# ==========================================

print("\n===== CONTACT FREQUENCY VS CONVERSION =====")

campaign_conversion = pd.crosstab(
    df["campaign"],
    df["y"],
    normalize="index"
) * 100

print(campaign_conversion.round(2))


# ==========================================
# 8. PREVIOUS CAMPAIGN OUTCOME
# ==========================================

print("\n===== PREVIOUS CAMPAIGN OUTCOME =====")

previous_conversion = pd.crosstab(
    df["poutcome"],
    df["y"],
    normalize="index"
) * 100

print(previous_conversion.round(2))


# ==========================================
# 9. CREATE POWER BI COLUMNS
# ==========================================

df["conversion"] = df["y"].map({
    "yes": 1,
    "no": 0
})

# Age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 45, 55, 65, 100],
    labels=[
        "Under 25",
        "25-34",
        "35-44",
        "45-54",
        "55-64",
        "65+"
    ]
)

# Campaign contact groups
df["campaign_group"] = pd.cut(
    df["campaign"],
    bins=[0, 1, 2, 3, 5, 10, 100],
    labels=[
        "1 contact",
        "2 contacts",
        "3 contacts",
        "4-5 contacts",
        "6-10 contacts",
        "10+ contacts"
    ]
)

# Whether customer was contacted in a previous campaign
df["previous_contact"] = df["previous"].apply(
    lambda x: "Yes" if x > 0 else "No"
)


# ==========================================
# 10. CREATE OUTPUT FOLDER AUTOMATICALLY
# ==========================================

output_folder = "output"

os.makedirs(output_folder, exist_ok=True)


# ==========================================
# 11. SAVE CLEANED DATASET
# ==========================================

output_path = os.path.join(
    output_folder,
    "marketing_campaign_cleaned.csv"
)

df.to_csv(
    output_path,
    index=False
)


# ==========================================
# 12. FINAL MESSAGE
# ==========================================

print("\n===== POWER BI DATASET CREATED =====")
print("Saved to:", output_path)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])