import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="STAYtus - SKZ Manager Simulator", page_icon="⭐", layout="wide")

# Estilos visuales modo oscuro tipo X/Instagram
st.markdown("""
<style>
    .stApp { background-color: #0f1419; color: #e7e9ea; }
    .main-header { font-size: 2.8rem; font-weight: 900; background: linear-gradient(135deg, #7928CA 0%, #FF0080 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .post-card { background-color: #161e27; border-radius: 16px; padding: 20px; margin-bottom: 20px; border: 1px solid #2f3336; }
    .comment-box { background-color: #1e2732; border-left: 4px solid #7928CA; border-radius: 8px; padding: 10px 15px; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# Base de datos de Bots con sus usuarios reales de Instagram y respuestas en inglés
BOTS = {
    "bangchan": {"name": "Bang Chan", "handle": "@gnabnahc", "templates": ["Thank you @gaerwenill! We will work hard for STAY! ❤️", "Late night in studio... please bring iced americano @gaerwenill! ☕", "STAYs are going to love this update! 👍✨", "Chanie's Room tonight? I need to tell STAY how awesome @gaerwenill is!"]},
    "leeknow": {"name": "Lee Know", "handle": "@t.leeknowsaurus", "templates": ["Did Sooni, Doongi, and Dori approve this post @gaerwenill? 🐱", "Manager @gaerwenill, where is my pudding?", "Dancing 8 hours today. My legs are fine, my patience is not. 😏", "Nice post @gaerwenill. Now buy us meat. 🥩"]},
    "changbin": {"name": "Changbin", "handle": "@jutdwae", "templates": ["JUTDAE! We do things with conviction! 💪🔥", "Did you see my bicep gains in the new photoshoot @gaerwenill?!", "3RACHA in the house! 🎵", "Protein shake break over, back to recording!"]},
    "hyunjin": {"name": "Hyunjin", "handle": "@hynjinnnn", "templates": ["The aesthetic of this schedule is amazing @gaerwenill! 🎨✨", "KAMI BIT MY SOCK AGAIN 😭 @gaerwenill help me!", "Dramatic? Me?! I am simply expressing my artistic soul! 🎭"]},
    "han": {"name": "Han Jisung", "handle": "@_doolsetnet", "templates": ["I wrote 3 songs in my sleep last night! You're welcome @gaerwenill! 🎵", "Can we order cheesecake for lunch? For lyrical inspiration obviously.", "STAY!! I missed you guys so much!"]},
    "felix": {"name": "Felix", "handle": "@yong.lixx", "templates": ["Baked homemade brownies for @gaerwenill & the boys! 🍪", "Hope everyone stays warm today! ☀️❤️", "Deep voice practice done! Ready to shake the stage! 🔊", "Manager @gaerwenill is the best! Thank you for taking care of us!"]},
    "seungmin": {"name": "Seungmin", "handle": "@miniverse.___", "templates": ["Vocal practice finished! Ready for comeback @gaerwenill. 🐶", "@gaerwenill, Changbin hyung is being noisy during my nap.", "Day 1290 of teasing Changbin hyung. Going great."]},
    "in": {"name": "I.N", "handle": "@i.2.n.8", "templates": ["Look at my OOTD for today's schedule @gaerwenill! 😎👔", "The hyungs bought me dinner again. Maknae wins! 🥖", "Maknae energy loaded! ⚡"]},
    "dispatch": {"name": "Dispatch Official", "handle": "@kpop_dispatch", "templates": ["🚨 BREAKING: SKZ Manager @gaerwenill spotted at JYPE! Comeback imminent?", "EXCLUSIVE: Photos from Stray Kids latest rehearsal with Manager @gaerwenill!"]},
    "stay_world": {"name": "STAY World News", "handle": "@stay_updates", "templates": ["WE LOVE YOU @gaerwenill! THANK YOU FOR PROTECTING OUR BOYS! 😭💖", "TRENDING #1 WORLDWIDE: #ManagerGaerwenill #StrayKidsNextEra!"]}
}

# Estado de la sesión
if "posts" not in st.session_state:
    st.session_state.posts = [{
        "id": 1, "author": "Gaerwenill", "handle": "@gaerwenill", "time": "10 mins ago",
        "content": "Official Announcement: Stray Kids is preparing something huge for STAYs! Stay tuned! 🧭✨ #StrayKids #JYPE",
        "likes": 18400, "comments": [
            {"author": "Bang Chan", "handle": "@gnabnahc", "text": "Let's go @gaerwenill! STAY get ready!! 🔥🔥"},
            {"author": "Felix", "handle": "@yong.lixx", "text": "So excited!! Made brownies for @gaerwenill today! ❤️"}
        ]
    }]

if "stories" not in st.session_state:
    st.session_state.stories = [
        {"author": "Bang Chan (@gnabnahc)", "caption": "Late night producing in the studio... 🎧"},
        {"author": "Felix (@yong.lixx)", "caption": "Fresh cookies for @gaerwenill! 🍪"},
        {"author": "Lee Know (@t.leeknowsaurus)", "caption": "Sooni says hi! 🐱"},
        {"author": "Hyunjin (@hynjinnnn)", "caption": "New painting finished 🎨"}
    ]

# Header principal
st.markdown('<div class="main-header">⭐ STAYtus</div>', unsafe_allow_html=True)
st.caption("<p style='text-align:center;'>Stray Kids Manager Simulator • Unlimited Energy • Zero Ads</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🧭 Manager Profile")
st.sidebar.write("**User:** @gaerwenill")
st.sidebar.write("**Role:** Head Manager of Stray Kids")
st.sidebar.write("**Agency:** JYP Entertainment")
st.sidebar.write("**Energy:** ⚡ UNLIMITED (100%)")
st.sidebar.write("**Reputation:** 99/100 (Worldwide Trend #1)")

# Pestañas
tab1, tab2, tab3, tab4 = st.tabs(["📱 Live Feed", "📸 Stories", "✍️ New Post", "💬 Direct Messages"])

with tab1:
    st.subheader("📱 Live Feed")
    for post in st.session_state.posts:
        st.markdown(f"""
        <div class="post-card">
            <strong>{post['author']}</strong> <span style="color:#71767b;">{post['handle']} • {post['time']}</span>
            <p style="margin-top:10px; font-size:1.1rem;">{post['content']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.write(f"❤️ Likes: {post['likes']:,}")
        st.write("💬 **Comments:**")
        for comment in post['comments']:
            st.markdown(f"""
            <div class="comment-box">
                <strong>{comment['author']}</strong> ({comment['handle']}): {comment['text']}
            </div>
            """, unsafe_allow_html=True)
            
        reply_input = st.text_input("Reply as @gaerwenill...", key=f"r_{post['id']}")
        if st.button("Send Reply", key=f"btn_{post['id']}"):
            if reply_input:
                post['comments'].append({"author": "Gaerwenill", "handle": "@gaerwenill", "text": reply_input})
                bot_key = random.choice(list(BOTS.keys()))
                bot = BOTS[bot_key]
                post['comments'].append({"author": bot["name"], "handle": bot["handle"], "text": random.choice(bot["templates"])})
                st.rerun()

with tab2:
    st.subheader("📸 Recent Stories")
    for s in st.session_state.stories:
        st.info(f"📸 **{s['author']}**: {s['caption']}")
    
    st.subheader("➕ Publish Story as @gaerwenill")
    s_cap = st.text_input("Story caption (English):")
    if st.button("Publish Story"):
        if s_cap:
            st.session_state.stories.insert(0, {"author": "Gaerwenill (@gaerwenill)", "caption": s_cap})
            st.success("Story published!")
            st.rerun()

with tab3:
    st.subheader("✍️ Create Post as @gaerwenill")
    new_text = st.text_area("Write post content in English:", placeholder="e.g. Stray Kids just finished rehearsal! Ready for comeback stage! 🔥")
    if st.button("🚀 Publish Post"):
        if new_text:
            comments = []
            for b_key in random.sample(list(BOTS.keys()), 4):
                bot = BOTS[b_key]
                comments.append({"author": bot["name"], "handle": bot["handle"], "text": random.choice(bot["templates"])})
            st.session_state.posts.insert(0, {
                "id": len(st.session_state.posts) + 1,
                "author": "Gaerwenill",
                "handle": "@gaerwenill",
                "time": "Just now",
                "content": new_text,
                "likes": random.randint(8000, 45000),
                "comments": comments
            })
            st.balloons()
            st.success("Published! Bots reacted in English!")

with tab4:
    st.subheader("💬 Direct Messages with SKZ")
    member = st.selectbox("Choose member:", ["Bang Chan (@gnabnahc) 🐺", "Lee Know (@t.leeknowsaurus) 🐱", "Changbin (@jutdwae) 🐷🐰", "Hyunjin (@hynjinnnn) 🥟", "Han (@_doolsetnet) 🦘", "Felix (@yong.lixx) 🐥", "Seungmin (@miniverse.___) 🐶", "I.N (@i.2.n.8) 🦊"])
    msg = st.text_input(f"Send message to {member}:")
    if st.button("Send DM"):
        if msg:
            st.write(f"**@gaerwenill:** {msg}")
            bot_key = random.choice(["bangchan", "felix", "leeknow", "changbin", "hyunjin", "han", "seungmin", "in"])
            st.write(f"**{member}:** {random.choice(BOTS[bot_key]['templates'])}")
