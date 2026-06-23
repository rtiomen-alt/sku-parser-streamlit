import streamlit as st
import pandas as pd

from parser.atomizer import split_rows
from parser.canonical import build_canonical
from parser.tnved import classify_tnved
from parser.flavor import extract_flavor

st.set_page_config(page_title="SKU Parser", layout="wide")

st.title("SKU Atomization & TN VED Parser")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:
    df = pd.read_excel(file)

    rows = []

    for _, r in df.iterrows():
        items = split_rows(r.get("Наименование (обозначение) продукции"))

        if not items:
            items = [r.get("Наименование (обозначение) продукции")]

        for item in items:
            rows.append({
                "SKU": item,
                "Canonical SKU": build_canonical(item),
                "Flavor": extract_flavor(item),
                "TN VED Group": classify_tnved(r.get("Код ТН ВЭД")),
                "TN VED Code": r.get("Код ТН ВЭД"),
                "Reg Number": r.get("Регистрационный номер"),
                "Action From": r.get("Действие с"),
                "Action To": r.get("Действие по"),
                "Applicant": r.get("Заявитель"),
            })

    out = pd.DataFrame(rows)

    st.dataframe(out, use_container_width=True)

    st.download_button(
        "Download CSV",
        out.to_csv(index=False).encode("utf-8"),
        "parsed.csv",
        "text/csv"
    )
