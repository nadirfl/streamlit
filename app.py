import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Daten laden
iris = sns.load_dataset('iris')

# Streamlit App
def main():
    st.title('Iris-Datenset Visualisierung')

    # Radio-Button zur Auswahl der Visualisierung
    view_mode = st.radio("Wählen Sie die Visualisierungsart", ('Tabelle anzeigen', 'Pairplot', 'Histogramm'))

    if view_mode == 'Tabelle anzeigen':
        st.write(iris)
    elif view_mode == 'Pairplot':
        st.subheader('Pairplot der Iris-Daten')
        pairplot_fig = sns.pairplot(iris, hue='species')
        st.pyplot(pairplot_fig)
    else:
        st.subheader('Histogramm der Merkmale')
        feature = st.selectbox('Wählen Sie das Feature', options=iris.columns[:-1])
        hist_fig, ax = plt.subplots()
        sns.histplot(iris[feature], kde=True, ax=ax)
        st.pyplot(hist_fig)

if __name__ == "__main__":
    main()
