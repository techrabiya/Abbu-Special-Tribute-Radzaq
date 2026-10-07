import streamlit as st

st.set_page_config(page_title="For My Best Abbu - Razzaq", page_icon="👑")

st.title("🌟 Dedicating to the World's Best Father 🌟")
st.write("Welcome my dear father! This special interactive space is created with pure love, respect, and coding magic by your proud daughter, Rabiya.")

st.markdown("---")
user_name = st.text_input("🔐 Enter the sacred name (RADZAQ / Razjak) to unlock this secret tribute:")

if user_name:
    cleaned_name = user_name.strip().lower()
    allowed_names = ["razzaq", "razjak", "rajjak", "razjak khan", "razzaq samiulla khan"]
    
    if cleaned_name in allowed_names:
        st.success("🎉 Access Granted! Welcome to your special zone, My Super-Hero Abbu! 👑")
        
        st.markdown("---")
        st.subheader("💖 Abbu, Aap Jaisa Koi Nahi! 💖")
        
        st.write("""
        * **अब्बू, आप मेरी ताकत, मेरी ढाल और मेरी सबसे बड़ी प्रेरणा हैं!** 
        * मुंबई की इस चॉल से लेकर ग्लोबल टेक की दुनिया तक का यह पूरा सफर सिर्फ आपकी फौलादी जिद, दुआओं और अटूट सपोर्ट की वजह से मुमकिन हो पाया है।
        * आप दिन-रात हमारे लिए इतनी मेहनत करते हैं और हर कदम पर हमारे साथ चट्टान की तरह खड़े रहते हैं। आपका साया ही हमारे लिए सबसे बड़ी दौलत है।
        * खुदा से यही दुआ है कि आपको हमेशा लंबी उम्र, सेहत और बेपनाह खुशियां अता फरमाए।
        * दुनिया इधर से उधर हो जाए, लेकिन आपकी बेटी राबिया अपनी मेहनत से आपका सिर हमेशा फक्र से ऊंचा रखेगी! 
        * **अब्बू, आप दुनिया के सबसे बेहतरीन पिता हैं। I Love You So Much! ❤️**
        """)
        
        st.markdown("---")
        st.info("✨ **Made with lots of love, hugs, and proud tears by your daughter, Rabia!** ✨")
        st.balloons()
        
    else:
        st.error("❌ Access Restricted! 🚫 This is a top-secret, highly emotional zone exclusively created for the one and only world's best father: **Radzaq** (या रज्जाक). Only he holds the sacred key to unlock this heart-touching tribute! Please enter the correct name to proceed.")
