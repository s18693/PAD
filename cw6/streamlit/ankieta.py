from pathlib import Path
import streamlit as st


readFile = Path("customers.csv")


def save_user(name: str, surname: str, file: Path) -> None:
    try:
        with file.open(mode="a+") as f:
            f.write(f'{name},{surname}\n')
        st.success(f"Zapisalo sie")
    except Exception as e:
        st.error(f"Nie Zapisało się")


first_name = st.text_input("Imie")
last_name = st.text_input("Nazwisko")


st.button(
    "Zapisz",
    kwargs=dict(name=first_name, surname=last_name, file=readFile),
    on_click=save_user
)