import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - Stray Kids Edition",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Ocultar todos los elementos nativos de Streamlit para dejar pantalla limpia
st.markdown(
    """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; margin: 0 !important; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stToolbar"] { display: none !important; }
</style>
""",
    unsafe_allow_html=True,
)

html_code = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status AI - Stray Kids Edition</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        body { background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; min-height: 100vh; overflow-x: hidden; }
        
        .app-container {
            width: 100%;
            max-width: 480px;
            background-color: #000000;
            min-height: 100vh;
            border-left: 1px solid #16181c;
            border-right: 1px solid #16181c;
            display: flex;
            flex-direction: column;
            position: relative;
            padding-bottom: 75px;
        }

        /* TOP HEADER */
        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.9);
            backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 800;
            background: linear-gradient(45deg, #a855f7, #ec4899);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 6px;
        }
        .energy-badge {
            background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4);
            padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; display: flex; align-items: center; gap: 4px;
        }

        /* STORIES BAR */
        .stories-container {
            display: flex; gap: 14px; padding: 14px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 6px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 64px; height: 64px; border-radius: 50%; padding: 2px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .story-avatar { width: 58px; height: 58px; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
        .story-username { font-size: 11px; color: #71767b; width: 66px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }

        /* CREATE POST BOX */
        .create-post-box { padding: 14px 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #050505; }
        .user-avatar-sm { width: 42px; height: 42px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 1px solid #2f3336; }
        .post-input-container { flex: 1; display: flex; flex-direction: column; gap: 10px; }
        .post-textarea { width: 100%; background: transparent; border: none; color: #f7f9f9; font-size: 15px; outline: none; resize: none; min-height: 48px; }
        .post-btn-row { display: flex; justify-content: space-between; align-items: center; }
        .post-submit-btn { background: #a855f7; color: #fff; border: none; padding: 8px 18px; border-radius: 20px; font-weight: 700; font-size: 14px; cursor: pointer; transition: 0.2s; }
        .post-submit-btn:hover { background: #9333ea; }

        /* FEED & POSTS */
        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 1px solid #2f3336; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; margin-left: 2px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 10px; }
        .post-media { width: 100%; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; max-height: 320px; object-fit: cover; }
        .post-actions { display: flex; justify-content: space-between; max-width: 320px; color: #71767b; font-size: 13px; margin-top: 6px; }
        .action-item { cursor: pointer; display: flex; align-items: center; gap: 6px; transition: 0.2s; }
        .action-item:hover { color: #a855f7; }
        .action-item.liked { color: #f91880; font-weight: 700; }

        /* COMMENTS SECTION */
        .comments-list { margin-top: 12px; padding-left: 10px; border-left: 2px solid #212327; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 8px; font-size: 13px; line-height: 1.35; background: #0a0a0c; padding: 8px 12px; border-radius: 10px; border: 1px solid #16181c; }
        .comment-avatar { width: 28px; height: 28px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .comment-body { flex: 1; }
        .comment-author { font-weight: 700; color: #f7f9f9; }
        .comment-handle { color: #71767b; font-size: 12px; }
        .comment-text { color: #d9d9d9; margin-top: 2px; }
        .comment-reply-btn { color: #a855f7; font-size: 11px; cursor: pointer; margin-top: 4px; display: inline-block; font-weight: 600; }

        .reply-input-box { margin-top: 8px; display: none; gap: 8px; }
        .reply-input-box.active { display: flex; }
        .reply-input { flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 14px; padding: 6px 12px; color: #fff; font-size: 12px; outline: none; }
        .reply-send-btn { background: #a855f7; color: white; border: none; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 700; cursor: pointer; }

        /* TAB NAVIGATION */
        .tab-content { display: none; }
        .tab-content.active { display: block; }

        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #71767b; font-size: 13px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 2px; font-weight: 600; }
        .nav-item.active { color: #a855f7; }

        /* PROFILE TAB */
        .profile-container { padding: 16px; display: flex; flex-direction: column; align-items: center; }
        .profile-card { width: 100%; background: #0a0a0c; border: 1px solid #16181c; border-radius: 20px; padding: 20px; display: flex; flex-direction: column; align-items: center; position: relative; text-align: center; }
        .avatar-upload-wrapper { position: relative; width: 90px; height: 90px; margin-bottom: 12px; }
        .profile-avatar-large { width: 90px; height: 90px; border-radius: 50%; object-fit: cover; border: 3px solid #a855f7; }
        .camera-badge {
            position: absolute; bottom: 0; right: 0; background: #a855f7; color: white;
            width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-size: 14px; border: 2px solid #000; cursor: pointer;
        }
        #avatar-file-input { display: none; }

        /* DMS TAB */
        .dms-container { display: flex; flex-direction: column; height: calc(100vh - 140px); }
        .member-select-bar { display: flex; gap: 10px; overflow-x: auto; padding: 12px 16px; border-bottom: 1px solid #16181c; background: #050505; scrollbar-width: none; }
        .member-select-bar::-webkit-scrollbar { display: none; }
        .member-pill { padding: 8px 14px; background: #16181c; border-radius: 20px; color: #71767b; font-size: 13px; font-weight: 600; white-space: nowrap; cursor: pointer; border: 1px solid #2f3336; }
        .member-pill.active { background: #a855f7; color: #fff; border-color: #a855f7; }

        .chat-box { flex: 1; padding: 16px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; background: #000; }
        .chat-bubble { max-width: 82%; padding: 10px 14px; border-radius: 18px; font-size: 14px; line-height: 1.4; }
        .chat-bubble.incoming { background: #1a1a1e; color: #e7e9ea; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid #2f3336; }
        .chat-bubble.outgoing { background: #a855f7; color: #fff; align-self: flex-end; border-bottom-right-radius: 4px; }
        .chat-input-bar { padding: 10px 16px; background: #050505; border-top: 1px solid #16181c; display: flex; gap: 10px; position: sticky; bottom: 60px; }
        .chat-input { flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 20px; padding: 10px 16px; color: white; outline: none; font-size: 14px; }
        .chat-send-btn { background: #a855f7; color: white; border: none; padding: 0 18px; border-radius: 20px; font-weight: 700; cursor: pointer; }

        /* FULLSCREEN STORY MODAL */
        .story-modal { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.95); z-index: 2000; display: none; flex-direction: column; align-items: center; justify-content: center; padding: 20px; }
        .story-modal.active { display: flex; }
        .story-card-large { width: 100%; max-width: 400px; height: 80vh; background: #111; border-radius: 20px; overflow: hidden; position: relative; display: flex; flex-direction: column; border: 1px solid #333; }
        .story-modal-img { width: 100%; height: 75%; object-fit: cover; }
        .story-modal-info { padding: 16px; background: #16181c; flex: 1; display: flex; flex-direction: column; justify-content: space-between; }
        .story-close-btn { position: absolute; top: 16px; right: 16px; background: rgba(0,0,0,0.6); color: white; border: none; width: 36px; height: 36px; border-radius: 50%; font-size: 18px; cursor: pointer; z-index: 10; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- TOP HEADER -->
        <div class="top-header">
            <div class="app-logo"><span>✨</span> STATUS AI</div>
            <div class="energy-badge">⚡ UNLIMITED ENERGY</div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- STORIES BAR -->
            <div class="stories-container" id="stories-bar"></div>

            <!-- CREATE POST BOX -->
            <div class="create-post-box">
                <img id="my-avatar-sm" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23a855f7'/><text x='50' y='60' font-size='40' font-weight='bold' fill='white' text-anchor='middle'>G</text></svg>" class="user-avatar-sm">
                <div class="post-input-container">
                    <textarea id="new-post-text" class="post-textarea" placeholder="Post update as Manager @gaerwenill..."></textarea>
                    <div class="post-btn-row">
                        <span style="font-size:12px; color:#71767b;">Public to Stray Kids & STAYs</span>
                        <button class="post-submit-btn" onclick="submitNewPost()">Post</button>
                    </div>
                </div>
            </div>

            <!-- FEED LIST -->
            <div class="feed" id="feed-list"></div>
        </div>

        <!-- TAB 2: PROFILE -->
        <div id="tab-profile" class="tab-content">
            <div class="profile-container">
                <div class="profile-card">
                    <div class="avatar-upload-wrapper">
                        <img id="my-avatar-lg" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23a855f7'/><text x='50' y='60' font-size='40' font-weight='bold' fill='white' text-anchor='middle'>G</text></svg>" class="profile-avatar-large">
                        <label for="avatar-file-input" class="camera-badge">📷</label>
                        <input type="file" id="avatar-file-input" accept="image/*" onchange="uploadMyAvatar(event)">
                    </div>
                    <h2 style="color:#f7f9f9; font-size:20px; font-weight:800;">Gaerwenill</h2>
                    <p style="color:#a855f7; font-size:14px; font-weight:600; margin-top:2px;">@gaerwenill</p>
                    <p style="color:#71767b; font-size:13px; margin-top:8px;">Head Manager of Stray Kids · JYP Entertainment</p>
                    <div style="display:flex; gap:20px; margin-top:16px; font-size:13px; color:#e7e9ea;">
                        <span><strong>8</strong> Members Managed</span>
                        <span><strong>1.2M</strong> STAY Followers</span>
                    </div>
                    <button style="margin-top:20px; background:#16181c; border:1px solid #333; color:white; padding:10px 24px; border-radius:20px; font-size:13px; font-weight:700; cursor:pointer;" onclick="document.getElementById('avatar-file-input').click()">Change Profile Photo</button>
                </div>
            </div>
        </div>

        <!-- TAB 3: DMS -->
        <div id="tab-dms" class="tab-content">
            <div class="dms-container">
                <div class="member-select-bar" id="dm-members-bar"></div>
                <div class="chat-box" id="dm-chat-box"></div>
                <div class="chat-input-bar">
                    <input type="text" id="dm-input-text" class="chat-input" placeholder="Message member as @gaerwenill..." onkeypress="if(event.key==='Enter') sendDirectMessage()">
                    <button class="chat-send-btn" onclick="sendDirectMessage()">Send</button>
                </div>
            </div>
        </div>

        <!-- BOTTOM NAV -->
        <div class="bottom-nav">
            <a class="nav-item active" onclick="switchTab('feed', this)"><span>🏠</span><span>Feed</span></a>
            <a class="nav-item" onclick="switchTab('profile', this)"><span>👤</span><span>Profile</span></a>
            <a class="nav-item" onclick="switchTab('dms', this)"><span>💬</span><span>DMs</span></a>
        </div>
    </div>

    <!-- STORY FULLSCREEN MODAL -->
    <div class="story-modal" id="story-modal">
        <div class="story-card-large">
            <button class="story-close-btn" onclick="closeStoryModal()">✕</button>
            <img id="story-modal-img" class="story-modal-img" src="">
            <div class="story-modal-info">
                <div>
                    <h3 id="story-modal-author" style="color:white; font-size:16px; font-weight:800;"></h3>
                    <p id="story-modal-caption" style="color:#d9d9d9; font-size:14px; margin-top:6px;"></p>
                </div>
                <div style="display:flex; gap:10px; margin-top:10px;">
                    <input type="text" placeholder="Reply to story..." style="flex:1; background:#000; border:1px solid #333; border-radius:16px; padding:8px 12px; color:white; font-size:13px;">
                    <button style="background:#a855f7; color:white; border:none; padding:0 14px; border-radius:16px; font-weight:700;" onclick="closeStoryModal()">Send</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // BASE64 GRAPHIC ASSETS FOR 100% RELIABILITY ON ALL MOBILE BROWSERS
        function createAvatarSVG(text, bgHex) {
            return "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'><rect width='120' height='120' fill='%23" + bgHex + "'/><text x='60' y='72' font-size='44' font-weight='bold' fill='white' text-anchor='middle' font-family='sans-serif'>" + text + "</text></svg>";
        }

        function createCardSVG(title, subtitle, bgHex) {
            return "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='600' height='350' viewBox='0 0 600 350'><rect width='600' height='350' fill='%23" + bgHex + "'/><circle cx='500' cy='80' r='120' fill='white' opacity='0.08'/><text x='40' y='180' font-size='32' font-weight='bold' fill='white' font-family='sans-serif'>" + title + "</text><text x='40' y='225' font-size='20' fill='%23e2e8f0' font-family='sans-serif'>" + subtitle + "</text></svg>";
        }

        let userAvatar = createAvatarSVG("G", "a855f7");

        const SKZ_MEMBERS = [
            { id: "bangchan", name: "Bang Chan", handle: "@gnabnahc", avatar: createAvatarSVG("BC", "4f46e5"), storyImg: createCardSVG("3RACHA Studio Session", "Late night producing World Tour tracklist", "311465"), replyTemplate: "Thanks @gaerwenill! The boys and I are reviewing the rehearsal notes now." },
            { id: "leeknow", name: "Lee Know", handle: "@t.leeknow", avatar: createAvatarSVG("LK", "059669"), storyImg: createCardSVG("Cats & Practice", "Sooni, Doongi, and Dori approved the choreography", "064e3b"), replyTemplate: "Got your message @gaerwenill. Tell the kitchen to save pudding for us." },
            { id: "changbin", name: "Changbin", handle: "@jutdwae", avatar: createAvatarSVG("CB", "dc2626"), storyImg: createCardSVG("Gym & JUTDAE", "Conviction is key! 3RACHA studio break", "7f1d1d"), replyTemplate: "JUTDAE!! Ready for tomorrow's vocal check Manager @gaerwenill!" },
            { id: "hyunjin", name: "Hyunjin", handle: "@hynjinnnn", avatar: createAvatarSVG("HJ", "d97706"), storyImg: createCardSVG("Art Studio Painting", "New canvas finished before stage rehearsal", "78350f"), replyTemplate: "Thank you Manager @gaerwenill! I will make sure my outfit fitting is on time." },
            { id: "han", name: "Han Jisung", handle: "@_doolsetnet", avatar: createAvatarSVG("HN", "2563eb"), storyImg: createCardSVG("Lyrical Inspiration", "Cheesecake break in the recording booth", "1e3a8a"), replyTemplate: "I wrote two new rap verses for track 4! Check your email @gaerwenill!" },
            { id: "felix", name: "Felix", handle: "@yong.lixx", avatar: createAvatarSVG("FL", "ec4899"), storyImg: createCardSVG("Fresh Cookies Baked", "Homemade brownies for @gaerwenill & 3RACHA", "831843"), replyTemplate: "Manager @gaerwenill! I saved extra chocolate chip cookies for you in the lounge!" },
            { id: "seungmin", name: "Seungmin", handle: "@miniverse.___", avatar: createAvatarSVG("SM", "0891b2"), storyImg: createCardSVG("Vocal Recording", "Warmup done for the upcoming album stage", "164e63"), replyTemplate: "Vocal warmup completed @gaerwenill. Changbin hyung is being noisy as usual." },
            { id: "in", name: "I.N", handle: "@i.2.n.8", avatar: createAvatarSVG("IN", "9333ea"), storyImg: createCardSVG("Maknae OOTD", "Outfit check before evening broadcast", "581c87"), replyTemplate: "Thanks @gaerwenill hyung/nuna! Maknae energy is fully charged for tonight!" }
        ];

        const OFFICIAL_ACCOUNTS = {
            dispatch: { name: "Dispatch Official", handle: "@kpop_dispatch", avatar: createAvatarSVG("DIS", "b91c1c") },
            jyp: { name: "JYP Entertainment", handle: "@jyp_official_news", avatar: createAvatarSVG("JYP", "1d4ed8") },
            stay_updates: { name: "STAY World Updates", handle: "@stay_updates", avatar: createAvatarSVG("STAY", "db2777") },
            stay_latam: { name: "STAY Latam", handle: "@stay_latam", avatar: createAvatarSVG("LAT", "059669") }
        };

        let activeDMUserId = "bangchan";

        let postsData = [
            {
                id: 1, author: SKZ_MEMBERS[0].name, handle: SKZ_MEMBERS[0].handle, avatar: SKZ_MEMBERS[0].avatar, verified: true,
                time: "15m", text: "Huge shoutout to our head manager @gaerwenill for organizing the entire World Tour rehearsal schedule! STAYs, get ready!",
                media: createCardSVG("STRAY KIDS WORLD TOUR 2026", "Live Rehearsal Stage at JYPE Center", "311465"),
                likes: 48200, comments: [
                    { author: SKZ_MEMBERS[5].name, handle: SKZ_MEMBERS[5].handle, avatar: SKZ_MEMBERS[5].avatar, text: "Manager @gaerwenill worked so hard today! Brought cookies for everyone!" },
                    { author: OFFICIAL_ACCOUNTS.stay_updates.name, handle: OFFICIAL_ACCOUNTS.stay_updates.handle, avatar: OFFICIAL_ACCOUNTS.stay_updates.avatar, text: "WE LOVE YOU MANAGER @gaerwenill! THANK YOU FOR PROTECTING SKZ!" },
                    { author: OFFICIAL_ACCOUNTS.stay_latam.name, handle: OFFICIAL_ACCOUNTS.stay_latam.handle, avatar: OFFICIAL_ACCOUNTS.stay_latam.avatar, text: "STAYs around the world are ready! Thank you Manager @gaerwenill!" }
                ]
            },
            {
                id: 2, author: SKZ_MEMBERS[5].name, handle: SKZ_MEMBERS[5].handle, avatar: SKZ_MEMBERS[5].avatar, verified: true,
                time: "45m", text: "Baked fresh chocolate chip brownies for Manager @gaerwenill and all the members during studio break!",
                media: createCardSVG("Felix's Homemade Bakery", "Fresh Brownies for @gaerwenill & Members", "831843"),
                likes: 92400, comments: [
                    { author: SKZ_MEMBERS[1].name, handle: SKZ_MEMBERS[1].handle, avatar: SKZ_MEMBERS[1].avatar, text: "Where is my share @yong.lixx? Did Manager @gaerwenill eat them all?" },
                    { author: SKZ_MEMBERS[2].name, handle: SKZ_MEMBERS[2].handle, avatar: SKZ_MEMBERS[2].avatar, text: "Protein brownies next time! Great job Felix!" }
                ]
            },
            {
                id: 3, author: OFFICIAL_ACCOUNTS.dispatch.name, handle: OFFICIAL_ACCOUNTS.dispatch.handle, avatar: OFFICIAL_ACCOUNTS.dispatch.avatar, verified: true,
                time: "2h", text: "BREAKING: Stray Kids Head Manager @gaerwenill spotted arriving at JYP Center for final stage review.",
                media: createCardSVG("DISPATCH EXCLUSIVE", "Manager @gaerwenill Arriving at JYP Center", "b91c1c"),
                likes: 134000, comments: [
                    { author: OFFICIAL_ACCOUNTS.jyp.name, handle: OFFICIAL_ACCOUNTS.jyp.handle, avatar: OFFICIAL_ACCOUNTS.jyp.avatar, text: "Official preparations underway under Manager @gaerwenill." }
                ]
            }
        ];

        let dmHistory = {
            bangchan: [
                { sender: "incoming", text: "Hey @gaerwenill! Thanks for reviewing the schedule. Do you have a second to confirm tomorrow's soundcheck time?" }
            ]
        };

        // RENDER STORIES BAR
        function renderStories() {
            let container = document.getElementById("stories-bar");
            let html = "";
            SKZ_MEMBERS.forEach((m, idx) => {
                html += `
                    <div class="story-item" onclick="openStoryModal(${idx})">
                        <div class="story-ring"><img src="${m.avatar}" class="story-avatar"></div>
                        <span class="story-username">${m.handle}</span>
                    </div>
                `;
            });
            container.innerHTML = html;
        }

        // RENDER FEED
        function renderFeed() {
            let container = document.getElementById("feed-list");
            let html = "";
            postsData.forEach((p, pIdx) => {
                let commentsHtml = "";
                p.comments.forEach((c, cIdx) => {
                    commentsHtml += `
                        <div class="comment-item">
                            <img src="${c.avatar}" class="comment-avatar">
                            <div class="comment-body">
                                <div><span class="comment-author">${c.author}</span> <span class="comment-handle">${c.handle}</span></div>
                                <div class="comment-text">${c.text}</div>
                                <span class="comment-reply-btn" onclick="toggleReplyBox(${pIdx}, ${cIdx})">💬 Reply</span>
                                <div class="reply-input-box" id="reply-box-${pIdx}-${cIdx}">
                                    <input type="text" class="reply-input" id="reply-input-${pIdx}-${cIdx}" placeholder="Reply to ${c.handle} as @gaerwenill...">
                                    <button class="reply-send-btn" onclick="sendCommentReply(${pIdx}, ${cIdx}, '${c.handle}')">Send</button>
                                </div>
                            </div>
                        </div>
                    `;
                });

                html += `
                    <div class="post">
                        <img src="${p.avatar}" class="post-avatar">
                        <div class="post-content">
                            <div class="post-header">
                                <span class="post-author">${p.author}</span>
                                ${p.verified ? '<span class="verified-badge">☑️</span>' : ''}
                                <span class="post-handle">${p.handle} · ${p.time}</span>
                            </div>
                            <div class="post-text">${p.text}</div>
                            ${p.media ? `<img src="${p.media}" class="post-media">` : ''}
                            <div class="post-actions">
                                <div class="action-item ${p.liked ? 'liked' : ''}" onclick="toggleLike(${pIdx})">
                                    <span>${p.liked ? '❤️' : '🤍'}</span> <span>${p.likes.toLocaleString()}</span>
                                </div>
                                <div class="action-item"><span>💬</span> <span>${p.comments.length}</span></div>
                                <div class="action-item"><span>🔄</span> <span>Share</span></div>
                            </div>
                            <div class="comments-list">
                                ${commentsHtml}
                            </div>
                        </div>
                    </div>
                `;
            });
            container.innerHTML = html;
        }

        // TOGGLE LIKE
        function toggleLike(pIdx) {
            if (postsData[pIdx].liked) {
                postsData[pIdx].liked = false;
                postsData[pIdx].likes--;
            } else {
                postsData[pIdx].liked = true;
                postsData[pIdx].likes++;
            }
            renderFeed();
        }

        // SUBMIT NEW POST AS MANAGER
        function submitNewPost() {
            let input = document.getElementById("new-post-text");
            let text = input.value.trim();
            if (text !== "") {
                let newPost = {
                    id: Date.now(),
                    author: "Gaerwenill",
                    handle: "@gaerwenill",
                    avatar: userAvatar,
                    verified: true,
                    time: "Just now",
                    text: text,
                    likes: 1240,
                    comments: [
                        { author: SKZ_MEMBERS[0].name, handle: SKZ_MEMBERS[0].handle, avatar: SKZ_MEMBERS[0].avatar, text: "Got it Manager @gaerwenill! 3RACHA is on it!" },
                        { author: SKZ_MEMBERS[5].name, handle: SKZ_MEMBERS[5].handle, avatar: SKZ_MEMBERS[5].avatar, text: "Thank you Manager @gaerwenill! ❤️✨" }
                    ]
                };
                postsData.unshift(newPost);
                input.value = "";
                renderFeed();
            }
        }

        // TOGGLE REPLY INPUT BOX
        function toggleReplyBox(pIdx, cIdx) {
            let box = document.getElementById(`reply-box-${pIdx}-${cIdx}`);
            if (box) {
                box.classList.toggle("active");
            }
        }

        // SEND REPLY TO COMMENT
        function sendCommentReply(pIdx, cIdx, targetHandle) {
            let input = document.getElementById(`reply-input-${pIdx}-${cIdx}`);
            let text = input.value.trim();
            if (text !== "") {
                postsData[pIdx].comments.push({
                    author: "Gaerwenill",
                    handle: "@gaerwenill",
                    avatar: userAvatar,
                    text: `${targetHandle} ${text}`
                });
                renderFeed();
            }
        }

        // UPLOAD USER AVATAR
        function uploadMyAvatar(event) {
            let file = event.target.files[0];
            if (file) {
                let reader = new FileReader();
                reader.onload = function(e) {
                    userAvatar = e.target.result;
                    document.getElementById("my-avatar-sm").src = userAvatar;
                    document.getElementById("my-avatar-lg").src = userAvatar;
                    renderFeed();
                };
                reader.readAsDataURL(file);
            }
        }

        // DMs TAB LOGIC
        function renderDMMembersBar() {
            let bar = document.getElementById("dm-members-bar");
            let html = "";
            SKZ_MEMBERS.forEach(m => {
                let active = (m.id === activeDMUserId) ? "active" : "";
                html += `<div class="member-pill ${active}" onclick="selectDMMember('${m.id}')">${m.name}</div>`;
            });
            bar.innerHTML = html;
        }

        function selectDMMember(memberId) {
            activeDMUserId = memberId;
            renderDMMembersBar();
            renderDMChatBox();
        }

        function renderDMChatBox() {
            let box = document.getElementById("dm-chat-box");
            let msgs = dmHistory[activeDMUserId] || [];
            let html = "";
            msgs.forEach(m => {
                html += `<div class="chat-bubble ${m.sender}">${m.text}</div>`;
            });
            box.innerHTML = html;
            box.scrollTop = box.scrollHeight;
        }

        function sendDirectMessage() {
            let input = document.getElementById("dm-input-text");
            let text = input.value.trim();
            if (text !== "") {
                if (!dmHistory[activeDMUserId]) dmHistory[activeDMUserId] = [];
                dmHistory[activeDMUserId].push({ sender: "outgoing", text: text });
                input.value = "";
                renderDMChatBox();

                setTimeout(() => {
                    let member = SKZ_MEMBERS.find(m => m.id === activeDMUserId);
                    let replyText = member ? member.replyTemplate : "Got your message Manager @gaerwenill!";
                    dmHistory[activeDMUserId].push({ sender: "incoming", text: replyText });
                    renderDMChatBox();
                }, 1200);
            }
        }

        // STORY MODAL LOGIC
        function openStoryModal(idx) {
            let member = SKZ_MEMBERS[idx];
            document.getElementById("story-modal-img").src = member.storyImg;
            document.getElementById("story-modal-author").innerText = member.name + " (" + member.handle + ")";
            document.getElementById("story-modal-caption").innerText = "Recent story update from " + member.name + " for Manager @gaerwenill";
            document.getElementById("story-modal").classList.add("active");
        }

        function closeStoryModal() {
            document.getElementById("story-modal").classList.remove("active");
        }

        // TAB SWITCHING
        function switchTab(tabName, el) {
            document.querySelectorAll(".tab-content").forEach(t => t.classList.remove("active"));
            document.querySelectorAll(".nav-item").forEach(n => n.classList.remove("active"));
            document.getElementById("tab-" + tabName).classList.add("active");
            el.classList.add("active");
        }

        // INITIALIZE APP
        renderStories();
        renderFeed();
        renderDMMembersBar();
        renderDMChatBox();
    </script>
</body>
</html>
"""

components.html(html_code, height=950, scrolling=True)
