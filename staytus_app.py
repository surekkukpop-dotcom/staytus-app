import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - SKZ Edition",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
</style>
""",
    unsafe_allow_html=True,
)

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status AI - SKZ Edition</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        body { background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; min-height: 100vh; overflow-x: hidden; }
        
        .app-container {
            width: 100%; max-width: 480px; background-color: #000000; min-height: 100vh;
            border-left: 1px solid #16181c; border-right: 1px solid #16181c; display: flex;
            flex-direction: column; position: relative; padding-bottom: 70px;
        }

        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.88);
            backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 900;
            background: linear-gradient(45deg, #a855f7, #ec4899);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 6px;
        }

        .stories-container {
            display: flex; gap: 14px; padding: 12px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 5px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 66px; height: 66px; border-radius: 50%; padding: 2px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .story-avatar { width: 60px; height: 60px; border-radius: 50%; border: 2px solid #000; object-fit: cover; background: #16181c; }
        .story-username { font-size: 11px; color: #71767b; width: 66px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }

        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #202327; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 10px; }
        .post-media { width: 100%; border-radius: 14px; margin-bottom: 10px; border: 1px solid #2f3336; max-height: 380px; object-fit: cover; }
        
        .post-actions { display: flex; justify-content: space-between; max-width: 320px; color: #71767b; font-size: 13px; margin-top: 8px; }
        .action-btn { cursor: pointer; display: flex; align-items: center; gap: 6px; transition: color 0.2s; }
        .action-btn:hover { color: #1d9bf0; }
        .action-btn.liked { color: #f91880; }

        .comments-section { margin-top: 12px; padding-top: 10px; border-top: 1px solid #202327; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 10px; font-size: 13.5px; background: #0c0e12; padding: 10px; border-radius: 10px; border: 1px solid #16181c; }
        .comment-avatar { width: 32px; height: 32px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #202327; }
        .comment-body { flex: 1; }
        .comment-author { font-weight: 700; color: #f7f9f9; }
        .comment-text { color: #d9d9d9; margin-top: 2px; }

        .add-comment-box { display: flex; gap: 8px; margin-top: 10px; }
        .add-comment-input { flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 20px; padding: 8px 14px; color: #fff; font-size: 13px; outline: none; }
        .add-comment-btn { background: #a855f7; color: #fff; border: none; border-radius: 20px; padding: 0 14px; font-weight: 600; font-size: 13px; cursor: pointer; }

        .create-post-card { padding: 16px; border-bottom: 1px solid #16181c; background: #0a0c10; }
        .create-post-top { display: flex; gap: 12px; }
        .create-post-textarea { flex: 1; background: transparent; border: none; color: #fff; font-size: 15px; outline: none; resize: none; min-height: 60px; }
        .create-post-actions { display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }

        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #71767b; font-size: 18px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 3px; font-size: 11px; }
        .nav-item i { font-size: 20px; }
        .nav-item.active { color: #a855f7; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }

        .story-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 2000; justify-content: center; align-items: center; }
        .story-modal.active { display: flex; }
        .story-modal-content { width: 100%; max-width: 440px; height: 90vh; background: #111; border-radius: 16px; position: relative; overflow: hidden; display: flex; flex-direction: column; }
        .story-modal-img { width: 100%; height: 75%; object-fit: cover; }
        .story-modal-header { position: absolute; top: 12px; left: 12px; right: 12px; display: flex; align-items: center; gap: 10px; z-index: 10; background: rgba(0,0,0,0.5); padding: 8px 12px; border-radius: 30px; backdrop-filter: blur(8px); }
        .story-modal-avatar { width: 36px; height: 36px; border-radius: 50%; object-fit: cover; }
        .story-modal-close { position: absolute; top: 16px; right: 16px; color: white; font-size: 24px; cursor: pointer; z-index: 20; background: rgba(0,0,0,0.6); width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .story-modal-caption { padding: 16px; background: #111; color: #fff; font-size: 14px; line-height: 1.4; flex: 1; }

        .profile-header-card { padding: 24px 20px; text-align: center; border-bottom: 1px solid #16181c; }
        .profile-avatar-container { position: relative; width: 96px; height: 96px; margin: 0 auto 14px auto; }
        .profile-avatar-img { width: 96px; height: 96px; border-radius: 50%; object-fit: cover; border: 3px solid #a855f7; background: #202327; }
        .change-avatar-btn { position: absolute; bottom: 0; right: 0; background: #a855f7; color: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 14px; border: 2px solid #000; box-shadow: 0 2px 8px rgba(0,0,0,0.5); }
        
        .chat-container { padding: 16px; display: flex; flex-direction: column; gap: 12px; height: calc(100vh - 190px); overflow-y: auto; padding-bottom: 80px; }
        .chat-bubble { max-width: 82%; padding: 12px 16px; border-radius: 18px; font-size: 14.5px; line-height: 1.45; }
        .chat-bubble.incoming { background: #1c1e22; color: #e7e9ea; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid #2a2d32; }
        .chat-bubble.outgoing { background: linear-gradient(135deg, #a855f7, #9333ea); color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
        .chat-member-select { padding: 12px 16px; background: #0c0e12; border-bottom: 1px solid #16181c; display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; }
        .member-chip { padding: 6px 14px; border-radius: 20px; background: #16181c; color: #71767b; font-size: 13px; font-weight: 600; white-space: nowrap; cursor: pointer; border: 1px solid #2a2d32; }
        .member-chip.active { background: #a855f7; color: white; border-color: #a855f7; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- Top Bar -->
        <div class="top-header">
            <div class="app-logo"><i class="fa-solid fa-sparkles"></i> Status</div>
            <div style="color:#a855f7; font-size: 12px; font-weight: 800; background: rgba(168, 85, 247, 0.15); padding: 4px 10px; border-radius: 12px;">
                <i class="fa-solid fa-bolt"></i> UNLIMITED
            </div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- Stories Bar -->
            <div class="stories-container" id="stories-bar"></div>

            <!-- Create Post Card -->
            <div class="create-post-card">
                <div class="create-post-top">
                    <img src="" id="my-avatar-mini" class="post-avatar" referrerpolicy="no-referrer">
                    <textarea id="new-post-text" class="create-post-textarea" placeholder="What's happening in SKZ schedule?"></textarea>
                </div>
                <div class="create-post-actions">
                    <div style="color:#a855f7; font-size: 14px;"><i class="fa-regular fa-image"></i> <i class="fa-regular fa-face-smile" style="margin-left:8px;"></i></div>
                    <button style="background:#a855f7; color:white; border:none; padding: 8px 18px; border-radius:20px; font-weight:700; cursor:pointer;" onclick="createPost()">Post</button>
                </div>
            </div>

            <!-- Main Feed -->
            <div class="feed" id="main-feed"></div>
        </div>

        <!-- TAB 2: DMS -->
        <div id="tab-dms" class="tab-content">
            <div class="chat-member-select" id="chat-member-chips"></div>
            <div class="chat-container" id="chat-box"></div>
            <div style="position: fixed; bottom: 65px; width: 100%; max-width: 480px; background: #000; padding: 10px 16px; display: flex; gap: 8px; border-top: 1px solid #16181c;">
                <input type="text" id="dm-input" style="flex:1; background:#181b20; border:1px solid #2a2d32; border-radius:20px; padding:10px 16px; color:white; outline:none;" placeholder="Type a message...">
                <button style="background:#a855f7; color:white; border:none; padding: 0 18px; border-radius:20px; font-weight:700; cursor:pointer;" onclick="sendDM()">Send</button>
            </div>
        </div>

        <!-- TAB 3: PROFILE -->
        <div id="tab-profile" class="tab-content">
            <div class="profile-header-card">
                <div class="profile-avatar-container">
                    <img src="" id="profile-avatar-main" class="profile-avatar-img" referrerpolicy="no-referrer">
                    <label for="avatar-file-input" class="change-avatar-btn" title="Change Profile Picture">
                        <i class="fa-solid fa-camera"></i>
                    </label>
                    <input type="file" id="avatar-file-input" accept="image/*" style="display:none;" onchange="uploadProfilePic(event)">
                </div>
                <h2 style="font-size: 20px; font-weight: 800; color: #fff;" id="profile-display-name">Gaerwenill</h2>
                <p style="color: #71767b; font-size: 14px;" id="profile-handle">@gaerwenill</p>
                <div style="display:inline-block; margin-top:8px; background:rgba(168, 85, 247, 0.2); color:#a855f7; padding:4px 12px; border-radius:12px; font-size:12px; font-weight:700;">
                    👑 Head Manager of Stray Kids
                </div>
                <div style="margin-top:20px; padding:16px; background:#0e1015; border-radius:14px; border:1px solid #1c2029; text-align:left;">
                    <div style="font-weight:700; color:#fff; font-size:14px; margin-bottom:6px;"><i class="fa-solid fa-gear" style="color:#a855f7;"></i> Profile Settings</div>
                    <p style="font-size:13px; color:#aaa; line-height:1.4;">Tap the camera icon on your profile picture above to upload any custom image from your device gallery. It will update across all posts, comments, and DMs instantly!</p>
                </div>
            </div>
        </div>

        <!-- Bottom Navigation -->
        <div class="bottom-nav">
            <div class="nav-item active" onclick="switchTab('feed', this)"><i class="fa-solid fa-house"></i> Feed</div>
            <div class="nav-item" onclick="switchTab('dms', this)"><i class="fa-regular fa-paper-plane"></i> DMs</div>
            <div class="nav-item" onclick="switchTab('profile', this)"><i class="fa-regular fa-user"></i> Profile</div>
        </div>
    </div>

    <!-- Story Viewer Modal -->
    <div class="story-modal" id="story-modal">
        <div class="story-modal-content">
            <div class="story-modal-close" onclick="closeStory()">&times;</div>
            <div class="story-modal-header">
                <img src="" id="story-author-avatar" class="story-modal-avatar" referrerpolicy="no-referrer">
                <div>
                    <div style="font-weight:700; color:white; font-size:14px;" id="story-author-name"></div>
                    <div style="color:#aaa; font-size:12px;" id="story-author-handle"></div>
                </div>
            </div>
            <img src="" id="story-image-main" class="story-modal-img" referrerpolicy="no-referrer">
            <div class="story-modal-caption" id="story-caption-text"></div>
        </div>
    </div>

    <script>
        // High quality Member avatars & photos
        function makeSvgAvatar(text, bg1, bg2) {
            const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
                <defs>
                    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:${bg1};stop-opacity:1" />
                        <stop offset="100%" style="stop-color:${bg2};stop-opacity:1" />
                    </linearGradient>
                </defs>
                <rect width="200" height="200" rx="100" fill="url(#grad)" />
                <text x="50%" y="54%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="-apple-system, sans-serif" font-size="64" font-weight="800">${text}</text>
            </svg>`;
            return "data:image/svg+xml;base64," + btoa(svg);
        }

        function makeSvgCard(title, bg1, bg2) {
            const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="350" viewBox="0 0 600 350">
                <defs>
                    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:${bg1};stop-opacity:1" />
                        <stop offset="100%" style="stop-color:${bg2};stop-opacity:1" />
                    </linearGradient>
                </defs>
                <rect width="600" height="350" rx="20" fill="url(#g)" />
                <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="-apple-system, sans-serif" font-size="32" font-weight="700">${title}</text>
            </svg>`;
            return "data:image/svg+xml;base64," + btoa(svg);
        }

        const MEMBERS = {
            bangchan: {
                name: "Bang Chan", handle: "@gnabnahc",
                avatar: makeSvgAvatar("BC", "#7c3aed", "#4c1d95"),
                storyImg: makeSvgCard("3RACHA Studio Recording Track #4", "#5b21b6", "#1e1b4b"),
                storyText: "Late night in 3RACHA studio working on track 4. Manager @gaerwenill is keeping us hydrated!",
                replies: ["Late night producing session! Thanks @gaerwenill for arranging dinner.", "STAYs are going to love this new arrangement!"]
            },
            leeknow: {
                name: "Lee Know", handle: "@t.leeknow",
                avatar: makeSvgAvatar("LK", "#059669", "#064e3b"),
                storyImg: makeSvgCard("Dance Studio - Practice Session", "#047857", "#022c22"),
                storyText: "Sooni, Doongi, and Dori approve today's dance practice schedule.",
                replies: ["Did you order pudding @gaerwenill?", "Practice went smoothly today."]
            },
            changbin: {
                name: "Changbin", handle: "@jutdwae",
                avatar: makeSvgAvatar("CB", "#dc2626", "#7f1d1d"),
                storyImg: makeSvgCard("JUTDAE Workout & Gym Session", "#b91c1c", "#450a0a"),
                storyText: "Gym session completed! JUTDAE energy for the world tour rehearsals!",
                replies: ["Conviction in everything we do!", "3RACHA verse recorded successfully."]
            },
            hyunjin: {
                name: "Hyunjin", handle: "@hynjinnnn",
                avatar: makeSvgAvatar("HJ", "#d97706", "#78350f"),
                storyImg: makeSvgCard("Canvas Painting & Art Studio", "#b45309", "#451a03"),
                storyText: "Finished a new canvas painting between shooting schedules today.",
                replies: ["The lighting at today's shoot was amazing.", "Kami was sleeping peacefully when I left home."]
            },
            han: {
                name: "Han Jisung", handle: "@_doolsetnet",
                avatar: makeSvgAvatar("HAN", "#ea580c", "#7c2d12"),
                storyImg: makeSvgCard("Melodic Hook Brainstorming", "#c2410c", "#431407"),
                storyText: "I wrote two melodic hooks while having iced Americano.",
                replies: ["Can we order cheesecake for studio lunch @gaerwenill?", "STAYs, new lyrics coming soon!"]
            },
            felix: {
                name: "Felix", handle: "@yong.lixx",
                avatar: makeSvgAvatar("FLX", "#0891b2", "#164e63"),
                storyImg: makeSvgCard("Homemade Chocolate Chip Cookies", "#0e7490", "#083344"),
                storyText: "Fresh homemade chocolate cookies for Manager @gaerwenill & all the members!",
                replies: ["Hope everyone stays warm today!", "Thank you @gaerwenill for always taking care of us!"]
            },
            seungmin: {
                name: "Seungmin", handle: "@miniverse.___",
                avatar: makeSvgAvatar("SM", "#2563eb", "#1e3a8a"),
                storyImg: makeSvgCard("Vocal Practice & Warmup Studio", "#1d4ed8", "#172554"),
                storyText: "Vocal warmup completed. Ready for the live session.",
                replies: ["Vocal practice went really well today.", "Manager @gaerwenill, Changbin hyung is being noisy."]
            },
            in: {
                name: "I.N", handle: "@i.2.n.8",
                avatar: makeSvgAvatar("IN", "#db2777", "#831843"),
                storyImg: makeSvgCard("Performance Outfit Fitting Session", "#be185d", "#500724"),
                storyText: "Fitting session for tomorrow's performance outfit.",
                replies: ["Maknae outfit approval received!", "Hyungs bought me dinner again today."]
            }
        };

        const OFFICIALS = {
            dispatch: { name: "Dispatch Official", handle: "@kpop_dispatch", avatar: makeSvgAvatar("NEWS", "#b91c1c", "#450a0a") },
            jyp: { name: "JYP Official News", handle: "@jyp_official_news", avatar: makeSvgAvatar("JYP", "#1d4ed8", "#1e3a8a") }
        };

        let defaultAvatar = makeSvgAvatar("GW", "#a855f7", "#581c87");
        let myAvatar = localStorage.getItem("gaerwenill_avatar") || defaultAvatar;

        function updateAvatarDisplay() {
            document.getElementById("my-avatar-mini").src = myAvatar;
            document.getElementById("profile-avatar-main").src = myAvatar;
        }

        function uploadProfilePic(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    myAvatar = e.target.result;
                    localStorage.setItem("gaerwenill_avatar", myAvatar);
                    updateAvatarDisplay();
                    renderFeed();
                };
                reader.readAsDataURL(file);
            }
        }

        let postsData = [
            {
                id: 1,
                author: "Bang Chan", handle: "@gnabnahc", avatar: MEMBERS.bangchan.avatar, verified: true,
                time: "15m", text: "Big thanks to Head Manager @gaerwenill for organizing the upcoming world tour schedule! Everything is running smoothly. STAYs, get ready!",
                media: makeSvgCard("Stray Kids World Tour Rehearsal 2026", "#4c1d95", "#1e1b4b"),
                likes: 48200, commentsCount: 24, liked: false,
                comments: [
                    { author: "Felix", handle: "@yong.lixx", avatar: MEMBERS.felix.avatar, text: "Manager @gaerwenill is the best! Thank you hyung!" },
                    { author: "STAY Tokyo 2026", handle: "@stay_tokyo", avatar: makeSvgAvatar("STAY", "#e11d48", "#881337"), text: "We love Manager @gaerwenill for taking care of our boys!" },
                    { author: "Lee Know", handle: "@t.leeknow", avatar: MEMBERS.leeknow.avatar, text: "Don't forget the dinner schedule after rehearsals!" },
                    { author: "STAY Global", handle: "@stay_global", avatar: makeSvgAvatar("SKZ", "#0284c7", "#0c4a6e"), text: "STRAY KIDS WORLD TOUR IS COMING!!" }
                ]
            },
            {
                id: 2,
                author: "Dispatch Official", handle: "@kpop_dispatch", avatar: OFFICIALS.dispatch.avatar, verified: true,
                time: "1h", text: "EXCLUSIVE: Stray Kids Head Manager @gaerwenill spotted arriving at JYPE Headquarters with 3RACHA for comeback preparation.",
                media: makeSvgCard("DISPATCH EXCLUSIVE - Manager Arrival at JYPE", "#991b1b", "#450a0a"),
                likes: 89400, commentsCount: 42, liked: false,
                comments: [
                    { author: "STAY News", handle: "@stay_news", avatar: makeSvgAvatar("NEWS", "#d97706", "#78350f"), text: "Manager @gaerwenill working overtime! We appreciate all your effort!" },
                    { author: "JYP Official News", handle: "@jyp_official_news", avatar: OFFICIALS.jyp.avatar, text: "Official updates will be released shortly." }
                ]
            }
        ];

        let selectedChatMember = "bangchan";
        let chats = {
            bangchan: [
                { sender: "incoming", text: "Hey @gaerwenill! Thanks for reviewing the stage design. Everything looks great!" }
            ],
            felix: [
                { sender: "incoming", text: "Manager @gaerwenill! I brought some homemade cookies to the office for you!" }
            ],
            leeknow: [
                { sender: "incoming", text: "Did you confirm tomorrow's dance studio booking @gaerwenill?" }
            ],
            hyunjin: [
                { sender: "incoming", text: "The outfit selection for the photo shoot is perfect, thank you!" }
            ]
        };

        function renderStories() {
            let container = document.getElementById("stories-bar");
            let html = "";
            Object.keys(MEMBERS).forEach(key => {
                let m = MEMBERS[key];
                html += `
                    <div class="story-item" onclick="openStory('${key}')">
                        <div class="story-ring">
                            <img src="${m.avatar}" class="story-avatar" referrerpolicy="no-referrer">
                        </div>
                        <span class="story-username">${m.name}</span>
                    </div>
                `;
            });
            container.innerHTML = html;
        }

        function openStory(key) {
            let m = MEMBERS[key];
            document.getElementById("story-author-avatar").src = m.avatar;
            document.getElementById("story-author-name").innerText = m.name;
            document.getElementById("story-author-handle").innerText = m.handle;
            document.getElementById("story-image-main").src = m.storyImg;
            document.getElementById("story-caption-text").innerText = m.storyText;
            document.getElementById("story-modal").classList.add("active");
        }

        function closeStory() {
            document.getElementById("story-modal").classList.remove("active");
        }

        function renderFeed() {
            let feed = document.getElementById("main-feed");
            let html = "";
            postsData.forEach(p => {
                let commentsHtml = "";
                p.comments.forEach(c => {
                    commentsHtml += `
                        <div class="comment-item">
                            <img src="${c.avatar}" class="comment-avatar" referrerpolicy="no-referrer">
                            <div class="comment-body">
                                <span class="comment-author">${c.author}</span> <span style="color:#71767b; font-size:12px;">${c.handle}</span>
                                <div class="comment-text">${c.text}</div>
                            </div>
                        </div>
                    `;
                });

                html += `
                    <div class="post">
                        <img src="${p.avatar}" class="post-avatar" referrerpolicy="no-referrer">
                        <div class="post-content">
                            <div class="post-header">
                                <span class="post-author">${p.author}</span>
                                ${p.verified ? '<i class="fa-solid fa-circle-check verified-badge"></i>' : ''}
                                <span class="post-handle">${p.handle} · ${p.time}</span>
                            </div>
                            <div class="post-text">${p.text}</div>
                            ${p.media ? `<img src="${p.media}" class="post-media" referrerpolicy="no-referrer">` : ''}
                            <div class="post-actions">
                                <div class="action-btn" onclick="toggleComment(${p.id})"><i class="fa-regular fa-comment"></i> ${p.commentsCount}</div>
                                <div class="action-btn"><i class="fa-solid fa-retweet"></i> Re-post</div>
                                <div class="action-btn ${p.liked ? 'liked' : ''}" onclick="toggleLike(${p.id})">
                                    <i class="${p.liked ? 'fa-solid' : 'fa-regular'} fa-heart"></i> ${(p.likes).toLocaleString()}
                                </div>
                            </div>
                            <div class="comments-section" id="comments-${p.id}">
                                ${commentsHtml}
                                <div class="add-comment-box">
                                    <input type="text" class="add-comment-input" id="input-comment-${p.id}" placeholder="Reply as @gaerwenill...">
                                    <button class="add-comment-btn" onclick="addComment(${p.id})">Reply</button>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            });
            feed.innerHTML = html;
        }

        function toggleLike(id) {
            let p = postsData.find(item => item.id === id);
            if (p) {
                p.liked = !p.liked;
                p.likes += p.liked ? 1 : -1;
                renderFeed();
            }
        }

        function addComment(id) {
            let inp = document.getElementById(`input-comment-${id}`);
            if (inp && inp.value.trim() !== '') {
                let p = postsData.find(item => item.id === id);
                if (p) {
                    p.comments.push({ author: "Gaerwenill", handle: "@gaerwenill", avatar: myAvatar, text: inp.value });
                    p.commentsCount += 1;
                    inp.value = '';
                    
                    setTimeout(() => {
                        let randKey = Object.keys(MEMBERS)[Math.floor(Math.random() * Object.keys(MEMBERS).length)];
                        let m = MEMBERS[randKey];
                        let botReply = m.replies[Math.floor(Math.random() * m.replies.length)];
                        p.comments.push({ author: m.name, handle: m.handle, avatar: m.avatar, text: botReply });
                        p.commentsCount += 1;
                        renderFeed();
                    }, 1000);

                    renderFeed();
                }
            }
        }

        function createPost() {
            let txt = document.getElementById("new-post-text").value;
            if (txt.trim() !== '') {
                let newId = postsData.length + 1;
                postsData.unshift({
                    id: newId,
                    author: "Gaerwenill", handle: "@gaerwenill", avatar: myAvatar, verified: true,
                    time: "Just now", text: txt, media: null,
                    likes: 1240, commentsCount: 2, liked: false,
                    comments: [
                        { author: "Bang Chan", handle: "@gnabnahc", avatar: MEMBERS.bangchan.avatar, text: "Got it @gaerwenill! We will follow the schedule." },
                        { author: "Felix", handle: "@yong.lixx", avatar: MEMBERS.felix.avatar, text: "Thank you Manager @gaerwenill!" }
                    ]
                });
                document.getElementById("new-post-text").value = '';
                renderFeed();
            }
        }

        function renderDMs() {
            let chipsContainer = document.getElementById("chat-member-chips");
            let htmlChips = "";
            Object.keys(MEMBERS).forEach(key => {
                let m = MEMBERS[key];
                htmlChips += `<div class="member-chip ${key === selectedChatMember ? 'active' : ''}" onclick="selectChatMember('${key}')">${m.name}</div>`;
            });
            chipsContainer.innerHTML = htmlChips;

            let chatBox = document.getElementById("chat-box");
            let msgs = chats[selectedChatMember] || [];
            let htmlMsgs = "";
            msgs.forEach(m => {
                htmlMsgs += `<div class="chat-bubble ${m.sender}">${m.text}</div>`;
            });
            chatBox.innerHTML = htmlMsgs;
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function selectChatMember(key) {
            selectedChatMember = key;
            if (!chats[selectedChatMember]) chats[selectedChatMember] = [];
            renderDMs();
        }

        function sendDM() {
            let input = document.getElementById("dm-input");
            if (input && input.value.trim() !== '') {
                if (!chats[selectedChatMember]) chats[selectedChatMember] = [];
                chats[selectedChatMember].push({ sender: "outgoing", text: input.value });
                let userText = input.value;
                input.value = '';
                renderDMs();

                setTimeout(() => {
                    let m = MEMBERS[selectedChatMember];
                    let randReply = m.replies[Math.floor(Math.random() * m.replies.length)];
                    chats[selectedChatMember].push({ sender: "incoming", text: `${m.name}: ${randReply}` });
                    renderDMs();
                }, 1000);
            }
        }

        function switchTab(tabName, el) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            el.classList.add('active');
            if (tabName === 'dms') renderDMs();
        }

        updateAvatarDisplay();
        renderStories();
        renderFeed();
        renderDMs();
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
