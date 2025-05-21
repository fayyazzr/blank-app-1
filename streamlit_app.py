import streamlit as st

st.set_page_config(page_title="Profil Prabowo Subianto")

st.title("Profil Prabowo Subianto")

# Gambar dari URL (langsung ditampilkan)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/6/6f/Prabowo_Subianto_2014.jpg",
    caption="Prabowo Subianto",
    use_column_width=True
)

# Deskripsi singkat
st.markdown("""
**Prabowo Subianto Djojohadikusumo** adalah seorang tokoh militer dan politikus Indonesia.  
Ia menjabat sebagai **Menteri Pertahanan Republik Indonesia** sejak tahun 2019.  
Prabowo adalah ketua umum Partai Gerindra dan merupakan mantan Komandan Jenderal Kopassus.

### Fakta Singkat:
- **Lahir**: 17 Oktober 1951
- **Pendidikan**: Akademi Militer Magelang (1974)
- **Partai Politik**: Partai Gerakan Indonesia Raya (Gerindra)
- **Jabatan Saat Ini**: Menteri Pertahanan RI
""")
