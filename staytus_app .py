import streamlit as st
import random
import time

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Status AI - SKZ Manager Simulator",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS FOR STATUS AI / INSTAGRAM / TWITTER DARK AESTHETIC
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Global Styling */
    .stApp {
        background-color: #0b0e14;
        color: #e6e8ec;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Header Gradient */
    .app-title {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #a855f7 0%, #ec4899 50%, #f43f5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    .app-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }

    /* Story Circles at Top */
    .stories-container {
        display: flex;
        gap: 16px;
        overflow-x: auto;
        padding: 12px 0px;
        margin-bottom: 20px;
        border-bottom: 1px solid #1e293b;
    }
    .story-ring {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        padding: 3px;
        background: linear-gradient(45deg, #f09433, #dc2743, #bc1888);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
    }
    .story-avatar {
        width: 58px;
        height: 58px;
        border-radius: 50%;
        background-color: #1e293b;
        color: #f8fafc;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.2rem;
        border: 2px solid #0b0e14;
    }
    .story-label {
        font-size: 0.75rem;
        color: #cbd5e1;
        text-align: center;
        margin-top: 6px;
        font-weight: 500;
    }

    /* Post Card */
    .post-card {
        background-color: #151c28;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 22px;
        border: 1px solid #1e293b;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    .post-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }
    .post-avatar-circle {
        width: 46px;
        height: 46px;
        border-radius: 50%;
        background: linear-gradient(135deg, #a855f7, #ec4899);
        color: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.1rem;
        border: 2px solid #7e22ce;
    }
    .post-author-name {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f8fafc;
        margin: 0;
    }
    .post-author-handle {
        font-size: 0.85rem;
        color: #94a3b8;
        margin: 0;
    }
    .post-content {
        font-size: 1.05rem;
        line-height: 1.5;
        color: #f1f5f9;
        margin: 12px 0;
    }

    /* Comment Box */
    .comment-container {
        background-color: #0f172a;
        border-left: 3px solid #ec4899;
        border-radius: 10px;
        padding: 10px 14px;
        margin-top: 8px;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }
    .comment-avatar-circle {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background-color: #3b82f6;
        color: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 0.85rem;
        flex-shrink: 0;
    }
    .comment-text {
        font-size: 0.9rem;
        color: #e2e8f0;
    }

    /* Sidebar Badge */
    .manager-card {
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
        border: 1px solid #7e22ce;
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BOT PROFILES DATABASE
# ---------------------------------------------------------
BOTS = {
    "bangchan": {
        "name": "Bang Chan 🐺",
        "handle": "@gnabnahc",
        "initials": "BC",
        "color": "#3b82f6",
        "templates": [
            "Thank you @gaerwenill! We will work hard for STAY! ❤️",
            "Late night in studio... please bring iced americano @gaerwenill! ☕",
            "STAYs are going to love this update! 👍✨",
            "Chanie's Room tonight? I need to tell STAY how awesome @gaerwenill is!"
        ]
    },
    "leeknow": {
        "name": "Lee Know 🐱",
        "handle": "@t.leeknowsaurus",
        "initials": "LK",
        "color": "#10b981",
        "templates": [
            "Did Sooni, Doongi, and Dori approve this post @gaerwenill? 🐱",
            "Manager @gaerwenill, where is my pudding?",
            "Dancing 8 hours today. My legs are fine, my patience is not. 😏",
            "Nice post @gaerwenill. Now buy us meat. 🥩"
        ]
    },
    "changbin": {
        "name": "Changbin 🐷🐰",
        "handle": "@jutdwae",
        "initials": "CB",
        "color": "#f59e0b",
        "templates": [
            "JUTDAE! We do things with conviction! 💪🔥",
            "Did you see my bicep gains in the new photoshoot @gaerwenill?!",
            "3RACHA in the house! 🎵",
            "Protein shake break over, back to recording!"
        ]
    },
    "hyunjin": {
        "name": "Hyunjin 🥟",
        "handle": "@hynjinnnn",
        "initials": "HJ",
        "color": "#ec4899",
        "templates": [
            "The aesthetic of this schedule is amazing @gaerwenill! 🎨✨",
            "KAMI BIT MY SOCK AGAIN 😭 @gaerwenill help me!",
            "Dramatic? Me?! I am simply expressing my artistic soul! 🎭"
        ]
    },
    "han": {
        "name": "Han Jisung 🐿️",
        "handle": "@_doolsetnet",
        "initials": "HN",
        "color": "#8b5cf6",
        "templates": [
            "I wrote 3 songs in my sleep last night! You're welcome @gaerwenill! 🎵",
            "Can we order cheesecake for lunch? For lyrical inspiration obviously.",
            "STAY!! I missed you guys so much!"
        ]
    },
    "felix": {
        "name": "Felix 🐥",
        "handle": "@yong.lixx",
        "initials": "FL",
        "color": "#eab308",
        "templates": [
            "Baked homemade brownies for @gaerwenill & the boys! 🍪",
            "Hope everyone stays warm today! ☀️❤️",
            "Deep voice practice done! Ready to shake the stage! 🔊",
            "Manager @gaerwenill is the best! Thank you for taking care of us!"
        ]
    },
    "seungmin": {
        "name": "Seungmin 🐶",
        "handle": "@miniverse.___",
        "initials": "SM",
        "color": "#06b6d4",
        "templates": [
            "Vocal practice finished! Ready for comeback @gaerwenill. 🐶",
            "@gaerwenill, Changbin hyung is being noisy during my nap.",
            "Day 1290 of teasing Changbin hyung. Going great."
        ]
    },
    "in": {
        "name": "I.N 🦊",
        "handle": "@i.2.n.8",
        "initials": "IN",
        "color": "#f97316",
        "templates": [
            "Look at my OOTD for today's schedule @gaerwenill! 😎👔",
            "The hyungs bought me dinner again. Maknae wins! 🥖",
            "Maknae energy loaded! ⚡"
        ]
    },
    "dispatch": {
        "name": "Dispatch Official 🚨",
        "handle": "@kpop_dispatch",
        "initials": "DP",
        "color": "#ef4444",
        "templates": [
            "🚨 BREAKING: SKZ Head Manager @gaerwenill spotted at JYPE building! Comeback imminent?",
            "EXCLUSIVE: Photos from Stray Kids latest stadium rehearsal with Manager @gaerwenill!"
        ]
    },
    "stay_world": {
        "name": "STAY Global News 🌐",
        "handle": "@stay_updates",
        "initials": "ST",
        "color": "#a855f7",
        "templates": [
            "WE LOVE YOU @gaerwenill! THANK YOU FOR PROTECTING OUR BOYS! 😭💖",
            "TRENDING #1 WORLDWIDE: #ManagerGaerwenill #StrayKidsNextEra!"
        ]
    }
}

# ---------------------------------------------------------
# INITIAL SESSION STATE
# ---------------------------------------------------------
if "stories" not in st.session_state:
    st.session_state.stories = [
        {"user": "Bang Chan", "initials": "BC", "color": "#3b82f6", "caption": "Late night in 3RACHA studio... 🎧 New beats for STAY!"},
        {"user": "Felix", "initials": "FL", "color": "#eab308", "caption": "Fresh homemade brownies for @gaerwenill and staff! 🍪❤️"},
        {"user": "Lee Know", "initials": "LK", "color": "#10b981", "caption": "Sooni, Doongi & Dori controlling my couch today 🐱"},
        {"user": "Hyunjin", "initials": "HJ", "color": "#ec4899", "caption": "New canvas painting finished in my room 🎨✨"},
        {"user": "Dispatch", "initials": "DP", "color": "#ef4444", "caption": "🚨 Stadium rehearsal spotted! SKZ world tour preparing!"}
    ]

if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "author": "Bang Chan 🐺",
            "handle": "@gnabnahc",
            "initials": "BC",
            "color": "#3b82f6",
            "time": "15m ago",
            "content": "Huge thanks to our Head Manager @gaerwenill for arranging tonight's studio sessions and dinner! STAY, we are cooking something insane for you guys! 🔥🥠",
            "likes": 248900,
            "comments": [
                {"author": "Lee Know", "handle": "@t.leeknowsaurus", "initials": "LK", "color": "#10b981", "text": "@gaerwenill better have bought pudding too! 🍮"},
                {"author": "Gaerwenill", "handle": "@gaerwenill", "initials": "G", "color": "#a855f7", "text": "Pudding is already in the studio fridge @t.leeknowsaurus! Get back to practice! 😉"},
                {"author": "Felix", "handle": "@yong.lixx", "initials": "FL", "color": "#eab308", "text": "Thank you Manager @gaerwenill! Best manager ever! ❤️"}
            ]
        },
        {
            "id": 2,
            "author": "Dispatch Official 🚨",
            "handle": "@kpop_dispatch",
            "initials": "DP",
            "color": "#ef4444",
            "time": "1h ago",
            "content": "🚨 [EXCLUSIVE REPORT] Stray Kids and Manager @gaerwenill seen leaving JYP Entertainment building at 2 AM after 12-hour rehearsal. World tour announcement expected next week!",
            "likes": 182400,
            "comments": [
                {"author": "STAY Global News", "handle": "@stay_updates", "initials": "ST", "color": "#a855f7", "text": "PROTECT MANAGER @gaerwenill AND THE BOYS! LET THEM SLEEP!! 😭🙏"}
            ]
        },
        {
            "id": 3,
            "author": "Felix 🐥",
            "handle": "@yong.lixx",
            "initials": "FL",
            "color": "#eab308",
            "time": "3h ago",
            "content": "Baking day with @gaerwenill! Made double chocolate brownies for all 8 members and staff! Hope it gives everyone energy! 🍪✨☀️",
            "likes": 310500,
            "comments": [
                {"author": "Changbin", "handle": "@jutdwae", "initials": "CB", "color": "#f59e0b", "text": "Are these macro-friendly for my biceps bro?!"},
                {"author": "Hyunjin", "handle": "@hynjinnnn", "initials": "HJ", "color": "#ec4899", "text": "I ate 4 already. Sorry guys 🥟"}
            ]
        }
    ]

if "messages" not in st.session_state:
    st.session_state.messages = {
        "Bang Chan (@gnabnahc)": [
            {"sender": "Bang Chan", "text": "Hey @gaerwenill! Did JYP approve the tracklist for the new album?"},
            {"sender": "Gaerwenill", "text": "Yes Chan! All 10 tracks approved! 3RACHA did amazing work!"},
            {"sender": "Bang Chan", "text": "LETS GOOO!! STAY is going to lose their minds! Thank you @gaerwenill! ❤️"}
        ],
        "Felix (@yong.lixx)": [
            {"sender": "Felix", "text": "Manager @gaerwenill! What time is airport pickup tomorrow?"},
            {"sender": "Gaerwenill", "text": "Van arrives at 6:00 AM sharp Felix! Rest well tonight!"}
        ]
    }

# ---------------------------------------------------------
# UI HEADER
# ---------------------------------------------------------
st.markdown('<div class="app-title">🔮 Status AI</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Sims but Social Media • Stray Kids Universe • Powered by AI</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR MANAGER PROFILE & TRENDS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="manager-card">
        <div style="width:64px; height:64px; border-radius:50%; background:linear-gradient(135deg, #a855f7, #ec4899); color:#fff; display:flex; align-items:center; justify-content:center; font-size:1.6rem; font-weight:bold; margin:0 auto 10px auto; border:3px solid #ec4899;">G</div>
        <h3 style="margin:0; color:#fff;">@gaerwenill <span style="color:#38bdf8;">☑️</span></h3>
        <p style="color:#a855f7; margin:2px 0; font-size:0.9rem; font-weight:bold;">Head Manager of Stray Kids</p>
        <p style="color:#94a3b8; font-size:0.8rem; margin:0;">JYP Entertainment Official</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ Status Energy")
    st.progress(100)
    st.caption("✨ **UNLIMITED ENERGY (STATUS VIP)** • No Ads • No Cooldowns")

    st.markdown("---")
    st.markdown("### 🔥 Trending Worldwide")
    st.markdown("""
    1. 🎵 **#SKZNextComeback** — *452K posts*
    2. 🧭 **#ManagerGaerwenill** — *320K posts*
    3. 🎧 **#3RACHAInStudio** — *180K posts*
    4. 🐺 **#ChanniesRoom** — *145K posts*
    5. 🥟 **#HyunjinArt** — *98K posts*
    """)

# ---------------------------------------------------------
# STORIES BAR AT THE TOP
# ---------------------------------------------------------
st.markdown("### 📸 Active Stories")

cols = st.columns(len(st.session_state.stories) + 1)

with cols[0]:
    st.markdown("""
    <div class="story-ring">
        <div class="story-avatar" style="background:#7e22ce;">G</div>
    </div>
    <div class="story-label">+ You</div>
    """, unsafe_allow_html=True)

for idx, story in enumerate(st.session_state.stories):
    with cols[idx + 1]:
        st.markdown(f"""
        <div class="story-ring">
            <div class="story-avatar" style="background:{story['color']};">{story['initials']}</div>
        </div>
        <div class="story-label">{story['user']}</div>
        """, unsafe_allow_html=True)
        if st.button("View", key=f"s_btn_{idx}"):
            st.info(f"📖 **Story from {story['user']}:** {story['caption']}")

st.markdown("---")

# ---------------------------------------------------------
# MAIN TABS (FEED, CREATE POST, DMS, NOTIFICATIONS)
# ---------------------------------------------------------
tab_feed, tab_create, tab_dms, tab_notifs = st.tabs(["📱 Live Feed", "✍️ Create Post", "💬 Direct Messages", "🔔 Notifications"])

# TAB 1: LIVE FEED
with tab_feed:
    for post in st.session_state.posts:
        st.markdown(f"""
        <div class="post-card">
            <div class="post-header">
                <div class="post-avatar-circle" style="background:{post['color']};">{post['initials']}</div>
                <div>
                    <p class="post-author-name">{post['author']} <span style="color:#a855f7; font-size:0.85rem;">☑️</span></p>
                    <p class="post-author-handle">{post['handle']} • {post['time']}</p>
                </div>
            </div>
            <div class="post-content">{post['content']}</div>
            <div style="color:#94a3b8; font-size:0.9rem; margin-top:8px;">
                ❤️ <b>{post['likes']:,}</b> Likes &nbsp;&nbsp;&nbsp; 💬 <b>{len(post['comments'])}</b> Comments
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Comments Section
        with st.expander(f"💬 View Comments ({len(post['comments'])})", expanded=True):
            for comment in post["comments"]:
                st.markdown(f"""
                <div class="comment-container">
                    <div class="comment-avatar-circle" style="background:{comment.get('color', '#3b82f6')};">{comment.get('initials', 'K')}</div>
                    <div>
                        <b style="color:#f8fafc;">{comment['author']}</b> <span style="color:#94a3b8; font-size:0.8rem;">{comment['handle']}</span><br>
                        <span class="comment-text">{comment['text']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Reply box for @gaerwenill
            reply_text = st.text_input("Reply to thread as @gaerwenill...", key=f"input_reply_{post['id']}")
            if st.button("Send Comment", key=f"btn_reply_{post['id']}"):
                if reply_text:
                    post["comments"].append({
                        "author": "Gaerwenill",
                        "handle": "@gaerwenill",
                        "initials": "G",
                        "color": "#a855f7",
                        "text": reply_text
                    })
                    # Trigger random reaction from one of the members
                    random_bot_key = random.choice(list(BOTS.keys()))
                    bot = BOTS[random_bot_key]
                    post["comments"].append({
                        "author": bot["name"],
                        "handle": bot["handle"],
                        "initials": bot["initials"],
                        "color": bot["color"],
                        "text": random.choice(bot["templates"])
                    })
                    st.rerun()

# TAB 2: CREATE POST
with tab_create:
    st.subheader("✍️ Publish to Status AI Feed")
    post_text = st.text_area("What is happening at JYP / Stray Kids schedule?", placeholder="e.g. Official update: Stray Kids comeback photo shooting completed! STAY get ready! 📸✨")
    
    if st.button("🚀 Publish Post as @gaerwenill"):
        if post_text:
            # Generate instant fan and bot comments
            initial_comments = []
            selected_bots = random.sample(list(BOTS.keys()), 4)
            for b_key in selected_bots:
                bot = BOTS[b_key]
                initial_comments.append({
                    "author": bot["name"],
                    "handle": bot["handle"],
                    "initials": bot["initials"],
                    "color": bot["color"],
                    "text": random.choice(bot["templates"])
                })
            
            new_post = {
                "id": len(st.session_state.posts) + 10,
                "author": "Gaerwenill",
                "handle": "@gaerwenill",
                "initials": "G",
                "color": "#a855f7",
                "time": "Just now",
                "content": post_text,
                "likes": random.randint(15000, 89000),
                "comments": initial_comments
            }
            st.session_state.posts.insert(0, new_post)
            st.balloons()
            st.success("Post published! SKZ members and STAYs are commenting now!")
            time.sleep(1)
            st.rerun()

# TAB 3: DIRECT MESSAGES
with tab_dms:
    st.subheader("💬 Direct Messages with Stray Kids")
    selected_member = st.selectbox(
        "Select Conversation:",
        ["Bang Chan (@gnabnahc)", "Felix (@yong.lixx)", "Lee Know (@t.leeknowsaurus)", "Changbin (@jutdwae)", "Hyunjin (@hynjinnnn)", "Han (@_doolsetnet)", "Seungmin (@miniverse.___)", "I.N (@i.2.n.8)"]
    )

    if selected_member not in st.session_state.messages:
        st.session_state.messages[selected_member] = []

    chat_history = st.session_state.messages[selected_member]

    for msg in chat_history:
        if msg["sender"] == "Gaerwenill":
            st.markdown(f"<div style='text-align:right; background-color:#7e22ce; color:#fff; padding:10px 14px; border-radius:14px; margin:5px 0; display:inline-block; float:right; clear:both;'><b>@gaerwenill:</b> {msg['text']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:left; background-color:#1e293b; color:#f8fafc; padding:10px 14px; border-radius:14px; margin:5px 0; display:inline-block; float:left; clear:both;'><b>{msg['sender']}:</b> {msg['text']}</div>", unsafe_allow_html=True)

    st.markdown("<br style='clear:both;'>", unsafe_allow_html=True)
    dm_input = st.text_input(f"Message {selected_member}...", key="dm_input_field")
    if st.button("Send Direct Message"):
        if dm_input:
            chat_history.append({"sender": "Gaerwenill", "text": dm_input})
            # Generate instant reply from member
            member_key_map = {
                "Bang Chan (@gnabnahc)": "bangchan",
                "Felix (@yong.lixx)": "felix",
                "Lee Know (@t.leeknowsaurus)": "leeknow",
                "Changbin (@jutdwae)": "changbin",
                "Hyunjin (@hynjinnnn)": "hyunjin",
                "Han (@_doolsetnet)": "han",
                "Seungmin (@miniverse.___)": "seungmin",
                "I.N (@i.2.n.8)": "in"
            }
            b_key = member_key_map.get(selected_member, "bangchan")
            bot = BOTS[b_key]
            reply_reply = random.choice(bot["templates"])
            chat_history.append({"sender": bot["name"], "text": reply_reply})
            st.rerun()

# TAB 4: NOTIFICATIONS
with tab_notifs:
    st.subheader("🔔 Status AI Notifications")
    st.info("❤️ **Bang Chan (@gnabnahc)** and 12,400 others liked your post!")
    st.info("💬 **Felix (@yong.lixx)** mentioned you in a comment: 'Manager @gaerwenill is the best!'")
    st.info("🚨 **Dispatch Official (@kpop_dispatch)** tagged you in a post.")
    st.info("⭐ **STAY World Updates (@stay_updates)** started following you.")
