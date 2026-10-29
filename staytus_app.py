import streamlit as st
import random
import re

# Configuración de página
st.set_page_config(
    page_title="Status AI - SKZ Manager Simulator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual MODO OSCURO NEGRO PURO (Status AI Style)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #e7e9ea; }
    header, footer, #MainMenu { visibility: hidden; }
    
    .app-card {
        background-color: #0d0f12;
        border: 1px solid #1e2732;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 16px;
    }
    
    .member-badge {
        background: linear-gradient(90deg, #a855f7, #ec4899);
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: bold;
    }
    
    .comment-card {
        background-color: #161e27;
        border-left: 3px solid #a855f7;
        border-radius: 8px;
        padding: 10px 14px;
        margin-top: 8px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Generador SVG limpio
def make_svg_avatar(name_initials, bg_color="#a855f7"):
    return f"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='{bg_color}'/><text x='50%' y='55%' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-weight='900' font-size='36' fill='%23ffffff'>{name_initials}</text></svg>"

# MIEMBROS Y BOTS
MEMBERS = {
    "bangchan": {
        "name": "Bang Chan",
        "handle": "@gnabnahc",
        "role": "Líder & Productor (3RACHA)",
        "avatar": make_svg_avatar("BC", "%23a855f7"),
        "personality": "Liderazgo, trabaja hasta tarde en el estudio 3RACHA, protector con STAY."
    },
    "leeknow": {
        "name": "Lee Know",
        "handle": "@t.leeknowsaurus",
        "role": "Líder de Danza & Vocal",
        "avatar": make_svg_avatar("LK", "%233b82f6"),
        "personality": "Tsundere, bromista, habla de sus gatos Sooni, Doongi, Dori y pide pudin."
    },
    "changbin": {
        "name": "Changbin",
        "handle": "@jutdwae",
        "role": "Líder de Rap (3RACHA)",
        "avatar": make_svg_avatar("CB", "%23ef4444"),
        "personality": "Jutdae (convicción), gimnasio, batidos de proteína y raps potentes."
    },
    "hyunjin": {
        "name": "Hyunjin",
        "handle": "@hynjinnnn",
        "role": "Visual & Danza Principal",
        "avatar": make_svg_avatar("HJ", "%23ec4899"),
        "personality": "Artístico, dramático, enfocado en arte/pintura, moda y su perro Kami."
    },
    "han": {
        "name": "Han Jisung",
        "handle": "@_doolsetnet",
        "role": "Rapero & Productor (3RACHA)",
        "avatar": make_svg_avatar("HN", "%23f59e0b"),
        "personality": "Genio musical, ama la tarta de queso y escribir canciones en minutos."
    },
    "felix": {
        "name": "Felix",
        "handle": "@yong.lixx",
        "role": "Danza & Vocal (Voz Profunda)",
        "avatar": make_svg_avatar("FX", "%2310b981"),
        "personality": "Sunshine amable, hornea galletas y brownies, voz de bajo profundo."
    },
    "seungmin": {
        "name": "Seungmin",
        "handle": "@miniverse.___",
        "role": "Vocal Principal",
        "avatar": make_svg_avatar("SM", "%236366f1"),
        "personality": "Perrito disciplinado, practica vocal 24/7, le encanta trolear a Changbin."
    },
    "in": {
        "name": "I.N",
        "handle": "@i.2.n.8",
        "role": "Vocal & Maknae",
        "avatar": make_svg_avatar("IN", "%238b5cf6"),
        "personality": "Maknae mimado por todos sus hyungs, fotos de OOTD de moda."
    }
}

FAN_BOTS = {
    "felix_sunshine": {"name": "Lixxie_Sunshine_STAY", "handle": "@sunshine_lix97", "avatar": make_svg_avatar("ST", "%23ec4899")},
    "skz_world_5star": {"name": "STAY 5-STAR Worldwide", "handle": "@stay_5star_updates", "avatar": make_svg_avatar("SK", "%23a855f7")},
    "dispatch_kpop": {"name": "Dispatch Official", "handle": "@kpop_dispatch", "avatar": make_svg_avatar("DP", "%23ef4444")}
}

# 🧠 MOTOR INTELIGENTE DE RESPUESTAS CONTEXTUALES Y LÓGICAS
def generate_smart_reply(author_key, post_text, user_name="Gaerwenill"):
    text = post_text.lower()
    
    is_comeback = any(w in text for w in ["comeback", "album", "song", "single", "music", "cancion", "disco", "release", "mv", "teaser"])
    is_concert = any(w in text for w in ["concert", "tour", "stage", "concierto", "escenario", "show", "stadium", "world tour", "rehearsal", "ensayo"])
    is_food = any(w in text for w in ["food", "brownie", "cook", "cake", "eat", "dinner", "lunch", "pudding", "cheesecake", "coffee", "comida", "cena", "cafe"])
    is_fitness = any(w in text for w in ["gym", "workout", "bicep", "protein", "muscle", "exercise", "gimnasio", "entrenar"])
    is_rest = any(w in text for w in ["sleep", "rest", "tired", "bed", "night", "late", "descansar", "dormir", "noche"])
    is_fashion = any(w in text for w in ["ootd", "style", "photo", "photoshoot", "clothes", "fit", "arte", "paint", "moda"])
    is_praise = any(w in text for w in ["good job", "proud", "best", "great", "thank", "love", "manager", "amazing", "increible"])

    if author_key == "bangchan":
        if is_comeback:
            return f"We've been working so hard in 3RACHA studio for this! Manager @{user_name}, STAYs are not ready for this track! 🔥🎧"
        elif is_concert:
            return f"Checking the stage monitors now! Thank you for organizing everything @{user_name}. Let's make STAY proud tonight! 🧭"
        elif is_rest:
            return f"I know I should sleep early Manager @{user_name}... but just 5 more minutes in the studio! Promise! 😅"
        elif is_praise:
            return f"Thank you so much Manager @{user_name}! We couldn't do any of this without you taking care of us! Big hug! ❤️"
        else:
            return f"Hey @{user_name}! Just finished review with JYP. Everything looks solid! Did you get some coffee today? ☕"

    elif author_key == "leeknow":
        if is_food:
            return f"Manager @{user_name}, if there is no pudding or meat involved in this schedule, I am going on strike with Sooni and Doongi! 🐱🥩"
        elif is_concert:
            return f"Dancers practiced for 9 hours today. My legs are fine, but @{user_name} better buy us hotpot afterwards! 😏"
        elif is_praise:
            return f"Hmph... fine, good job @{user_name}. Now go feed Sooni, Doongi, and Dori! 😼"
        else:
            return f"Did Sooni approve this post @{user_name}? I'm watching you... bring snacks to practice room! 🍮"

    elif author_key == "changbin":
        if is_fitness:
            return f"JUTDAE!! 💪🔥 Did you see my bicep gains today @{user_name}?! Protein shake break is OVER, back to lifting!"
        elif is_comeback:
            return f"The rap verse on this track hits like a truck! Manager @{user_name}, 3RACHA cooked pure fire! 🔊🔥"
        else:
            return f"WE DO THINGS WITH CONVICTION! 👊🔥 Great update Manager @{user_name}! Now who is coming to the gym with me?!"

    elif author_key == "hyunjin":
        if is_fashion:
            return f"The aesthetic of this is stunning @{user_name}! 🎨✨ By the way, Kami bit my favorite sock again... help! 😭"
        elif is_concert:
            return f"The lighting setup on stage looks so artistic! I felt the emotional soul during rehearsal today ✨🎭"
        else:
            return f"Dramatic? Me?! I am simply expressing my artistic soul Manager @{user_name}! 🎨✨ Love this update!"

    elif author_key == "han":
        if is_food or is_comeback:
            return f"I wrote 2 entire songs while eating cheesecake today! You're welcome Manager @{user_name}! 🍰🎵"
        else:
            return f"STAY!! I was feeling introverted today but Manager @{user_name}'s post gave me 100% energy boost! 🦘✨"

    elif author_key == "felix":
        if is_food:
            return f"I just baked fresh homemade chocolate brownies for Manager @{user_name} and the boys! 🍪❤️ Please eat well!"
        elif is_concert or is_comeback:
            return f"My deep voice line is ready! 🔊 Sunshine energy loaded for STAY! Thank you Manager @{user_name} for supporting us! ✨"
        else:
            return f"Hope Manager @{user_name} and all STAYs stay warm and happy today! Sending big hugs! ☀️💙"

    elif author_key == "seungmin":
        if is_comeback or is_concert:
            return f"Vocal warmups completed 100% 🐶 Manager @{user_name}, Changbin hyung was being too noisy while I was recording."
        else:
            return f"Day 1,420 of teasing Changbin hyung. Going great! 🐶👍 Thanks for the update @{user_name}!"

    elif author_key == "in":
        return f"Look at my OOTD for today Manager @{user_name}! 😎👔 The hyungs bought me dinner again, Maknae on top!"

    elif author_key == "felix_sunshine":
        return f"WE LOVE YOU MANAGER @{user_name}!! THANK YOU FOR PROTECTING STRAY KIDS! 😭😭💖💖 #StrayKids #ManagerGaerwenill"

    elif author_key == "dispatch_kpop":
        return f"🚨 BREAKING: SKZ Manager @{user_name} spotted at JYP HQ preparing new global project! Stay tuned for exclusive coverage!"

    return f"STAYs are so excited for this update from Manager @{user_name}! Fighting!! 🔥✨"


# REINICIO Y CACHÉ
if "posts" not in st.session_state or st.sidebar.button("🔄 Reiniciar Sesión / Limpiar Caché"):
    st.session_state.posts = [
        {
            "id": 101,
            "author": "Bang Chan",
            "handle": "@gnabnahc",
            "badge": "STRAY KIDS LIDER",
            "avatar": MEMBERS["bangchan"]["avatar"],
            "time": "15m ago",
            "content": "Late night in 3RACHA studio with Changbin and Han! 🎧 We are crafting something truly special for STAY. Manager @gaerwenill brought us iced americano! ❤️",
            "likes": 84200,
            "comments": [
                {"author": "Felix", "handle": "@yong.lixx", "avatar": MEMBERS["felix"]["avatar"], "text": "Chanie hyung, don't stay up too late! I left brownies on the counter for you & @gaerwenill! 🍪❤️"},
                {"author": "Lee Know", "handle": "@t.leeknowsaurus", "avatar": MEMBERS["leeknow"]["avatar"], "text": "Where is my iced americano @gaerwenill? Sooni is judging you. 🐱"}
            ]
        },
        {
            "id": 102,
            "author": "Gaerwenill (Head Manager)",
            "handle": "@gaerwenill",
            "badge": "JYP HEAD MANAGER",
            "avatar": make_svg_avatar("GW", "%23ec4899"),
            "time": "1h ago",
            "content": "OFFICIAL ANNOUNCEMENT: Stray Kids World Tour 2026 rehearsal is officially under way! Rehearsal stage setup is 100% complete. Get ready STAYs! 🧭✨ #StrayKids #JYP #WorldTour",
            "likes": 125400,
            "comments": [
                {"author": "Changbin", "handle": "@jutdwae", "avatar": MEMBERS["changbin"]["avatar"], "text": "JUTDAE!! Stage energy is going to explode!! 💪🔥"},
                {"author": "Dispatch Official", "handle": "@kpop_dispatch", "avatar": FAN_BOTS["dispatch_kpop"]["avatar"], "text": "🚨 EXCLUSIVE: SKZ Manager @gaerwenill confirms stadium scale tour prep!"}
            ]
        }
    ]

# ENCABEZADO Y HEADER
st.markdown("<h1 style='text-align: center; color: #a855f7; font-weight: 900;'>⭐ Status AI — Stray Kids Edition</h1>", unsafe_allow_html=True)
st.caption("<p style='text-align:center; color:#94a3b8;'>Simulador de Manager de K-Pop • Inteligencia Contextual Real • Sin Límites de Energía</p>", unsafe_allow_html=True)

# BARRA LATERAL
st.sidebar.markdown("### 🧭 Manager Profile")
st.sidebar.write("**User:** @gaerwenill")
st.sidebar.write("**Role:** Head Manager of Stray Kids")
st.sidebar.write("**Agency:** JYP Entertainment")
st.sidebar.write("**Energy:** ⚡ UNLIMITED (100%)")
st.sidebar.write("**Reputation:** 🌟 99/100 (Worldwide Trend #1)")

# PESTAÑAS PRINCIPALES
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Live Feed & Posts", "📸 Member Profiles", "✍️ Create Post as Manager", "💬 Direct Messages (DMs)"])

# TAB 1: FEED
with tab1:
    st.subheader("📱 Community Feed")
    
    for post in st.session_state.posts:
        with st.container():
            col_av, col_body = st.columns([1, 7])
            with col_av:
                st.markdown(f"<img src='{post[\"avatar\"]}' style='width:52px;height:52px;border-radius:50%;'>", unsafe_allow_html=True)
            with col_body:
                st.markdown(f"**{post['author']}** <span class='member-badge'>{post.get('badge','MEMBER')}</span> <span style='color:#64748b;'>{post['handle']} • {post['time']}</span>", unsafe_allow_html=True)
                st.write(post["content"])
                
                st.caption(f"❤️ {post['likes']:,} Likes • 💬 {len(post['comments'])} Comments")
                
                for c in post["comments"]:
                    c_col1, c_col2 = st.columns([1, 10])
                    with c_col1:
                        st.markdown(f"<img src='{c.get(\"avatar\", make_svg_avatar(\"ST\"))}' style='width:32px;height:32px;border-radius:50%;'>", unsafe_allow_html=True)
                    with c_col2:
                        st.markdown(f"<div class='comment-card'><strong>{c['author']}</strong> <span style='color:#64748b;'>{c['handle']}</span><br>{c['text']}</div>", unsafe_allow_html=True)
                
                reply_text = st.text_input(f"Reply to {post['author']} as @gaerwenill...", key=f"inp_{post['id']}")
                if st.button(f"💬 Send Reply", key=f"btn_{post['id']}"):
                    if reply_text:
                        post["comments"].append({
                            "author": "Gaerwenill (Manager)",
                            "handle": "@gaerwenill",
                            "avatar": make_svg_avatar("GW", "%23ec4899"),
                            "text": reply_text
                        })
                        
                        selected_bots = random.sample(list(MEMBERS.keys()), 2)
                        for b_key in selected_bots:
                            bot_data = MEMBERS[b_key]
                            smart_msg = generate_smart_reply(b_key, reply_text)
                            post["comments"].append({
                                "author": bot_data["name"],
                                "handle": bot_data["handle"],
                                "avatar": bot_data["avatar"],
                                "text": smart_msg
                            })
                        
                        st.success("Reply posted! Members reacted with context-aware responses!")
                        st.rerun()

# TAB 2: PERFILES
with tab2:
    st.subheader("📸 Stray Kids Member Profiles")
    cols = st.columns(4)
    for idx, (m_key, m_info) in enumerate(MEMBERS.items()):
        with cols[idx % 4]:
            st.markdown(f"<img src='{m_info[\"avatar\"]}' style='width:80px;height:80px;border-radius:50%;margin-bottom:8px;'>", unsafe_allow_html=True)
            st.markdown(f"**{m_info['name']}** ({m_info['handle']})")
            st.info(f"💭 {m_info['personality']}")

# TAB 3: CREAR POST
with tab3:
    st.subheader("✍️ Create Post as Head Manager (@gaerwenill)")
    post_content = st.text_area("Write update for Stray Kids & STAYs:", placeholder="e.g. Stray Kids just completed rehearsals for the stadium concert! Super proud of the boys! 🔥")
    
    if st.button("🚀 Publish Post to Feed"):
        if post_content:
            new_id = len(st.session_state.posts) + 200
            
            auto_comments = []
            reacting_members = random.sample(list(MEMBERS.keys()), 3) + ["felix_sunshine", "dispatch_kpop"]
            for r_key in reacting_members:
                if r_key in MEMBERS:
                    b_info = MEMBERS[r_key]
                    c_text = generate_smart_reply(r_key, post_content)
                else:
                    b_info = FAN_BOTS[r_key]
                    c_text = generate_smart_reply(r_key, post_content)
                
                auto_comments.append({
                    "author": b_info["name"],
                    "handle": b_info["handle"],
                    "avatar": b_info["avatar"],
                    "text": c_text
                })
            
            st.session_state.posts.insert(0, {
                "id": new_id,
                "author": "Gaerwenill (Head Manager)",
                "handle": "@gaerwenill",
                "badge": "JYP HEAD MANAGER",
                "avatar": make_svg_avatar("GW", "%23ec4899"),
                "time": "Just now",
                "content": post_content,
                "likes": random.randint(15000, 95000),
                "comments": auto_comments
            })
            
            st.balloons()
            st.success("Post published! Stray Kids members and STAY bots reacted in real time based on your post topic!")
            st.rerun()

# TAB 4: DMs
with tab4:
    st.subheader("💬 Direct Messages with Stray Kids")
    selected_member_key = st.selectbox("Select Member to Chat:", options=list(MEMBERS.keys()), format_func=lambda x: f"{MEMBERS[x]['name']} ({MEMBERS[x]['handle']}) - {MEMBERS[x]['role']}")
    
    m_data = MEMBERS[selected_member_key]
    col_m1, col_m2 = st.columns([1, 5])
    with col_m1:
        st.markdown(f"<img src='{m_data[\"avatar\"]}' style='width:80px;height:80px;border-radius:50%;'>", unsafe_allow_html=True)
    with col_m2:
        st.markdown(f"### {m_data['name']} <span class='member-badge'>{m_data['role']}</span>", unsafe_allow_html=True)
        st.caption(f"Status: 🟢 Online • {m_data['personality']}")
    
    dm_input = st.text_input(f"Send DM to {m_data['name']}...", key="dm_inp")
    if st.button("💬 Send Message"):
        if dm_input:
            st.write(f"**You (@gaerwenill):** {dm_input}")
            reply_smart = generate_smart_reply(selected_member_key, dm_input)
            st.markdown(f"<div class='comment-card'><strong>{m_data['name']} ({m_data['handle']}):</strong><br>{reply_smart}</div>", unsafe_allow_html=True)
