from transformers import ViTImageProcessor, ViTModel
import streamlit as st
import torch
import pandas as pd
import numpy as np
import psycopg2 as pg
from PIL import Image
import io
np.set_printoptions(suppress=True)


st.sidebar.image("gp_icon.png")


# st.sidebar.header("About")
st.sidebar.markdown("""
    <div style="font-size: medium; font-style: italic">
    This is a  <b>Skin Cancer Image Search Application</b> leveraging <font color="green"> VMware Greenplum</font> as a Vector Database thanks to and <font color="blue"> pgvector extension </font> for AI-powered Search.<br><br> It demonstrates how to use semantic search for accurate skin cancer image comparison. <br><br><br>
    </div>
    """, unsafe_allow_html=True)
def semantic_search(emb, limit):
    query = """
          SELECT *, 1-(embeddings <=> '{emb}') score
          FROM skin_dataset 
          ORDER BY score DESC
          LIMIT {limit}
          """.format(emb=emb, limit=limit)
    df = pd.read_sql_query(query, engine)
    return df


engine = pg.connect("dbname='demo' user='gpadmin' host='localhost' port='5432' password='passwd'")

st.title("Skin Cancer Image Search Engine")
st.markdown(
    "Upload images with different skin conditions and you'll get the most similar ones from our database of images.")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = ViTImageProcessor.from_pretrained('facebook/dino-vits16')
model = ViTModel.from_pretrained('facebook/dino-vits16').to(device)

search_top_k = st.sidebar.slider('How many search results do you want to retrieve?', 1, 40, 5)
image_file = st.file_uploader(label="📷 Skin Condition Image file 🔍")

if image_file:
    st.image(image_file)
    inputs = processor(images=Image.open(image_file), return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs).last_hidden_state.mean(dim=1).cpu().numpy()

    st.subheader("Semantic Search Results", divider='rainbow')
    results = semantic_search(emb=list(outputs[0]), limit=search_top_k)

    for i in range(search_top_k):
        st.markdown(f"*Decease*: **{results.iloc[i]['dx']}**")
        st.caption(f"**Similarity Score**: {results.iloc[i]['score']}")
        st.caption(f"**Location**: {results.iloc[i]['localization']}")
        st.caption(f"**Gender**: {results.iloc[i]['sex']}")
        st.caption(f"**Age**: {results.iloc[i]['age']}")
        st.image(Image.open(io.BytesIO(results.iloc[i]['image'])))
        st.divider()

