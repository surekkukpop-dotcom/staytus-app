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
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
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

        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.90);
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

        /* STORIES BAR */
        .stories-container {
            display: flex; gap: 14px; padding: 12px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none; background: #000;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 64px; height: 64px; border-radius: 50%; padding: 2.5px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .story-avatar-img { width: 56px; height: 56px; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
        .story-username { font-size: 11px; color: #71767b; width: 64px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }

        /* CREATE POST BOX */
        .create-post-box { padding: 14px 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #050505; }
        .user-avatar-small { width: 42px; height: 42px; border-radius: 50%; object-fit: cover; border: 1.5px solid #a855f7; }
        .create-post-input { flex: 1; background: transparent; border: none; color: #fff; font-size: 15px; outline: none; resize: none; min-height: 40px; }
        .create-post-actions { display: flex; justify-content: space-between; align-items: center; margin-top: 8px; }
        .post-btn { background: #a855f7; color: #fff; border: none; padding: 8px 18px; border-radius: 20px; font-weight: 700; font-size: 14px; cursor: pointer; transition: 0.2s; }
        .post-btn:hover { background: #9333ea; }

        /* FEED & POSTS */
        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 10px; }
        .post-image { width: 100%; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; max-height: 320px; object-fit: cover; }
        .post-actions { display: flex; justify-content: space-between; max-width: 350px; color: #71767b; font-size: 13.5px; margin-top: 8px; }
        .action-btn { cursor: pointer; display: flex; align-items: center; gap: 6px; transition: 0.2s; }
        .action-btn:hover { color: #a855f7; }
        .action-btn.liked { color: #f91880; }

        /* COMMENTS THREAD */
        .comments-list { margin-top: 12px; padding-left: 12px; border-left: 2px solid #1e232a; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 10px; font-size: 13.5px; }
        .comment-avatar { width: 32px; height: 32px; border-radius: 50%; object-fit: cover; }
        .comment-body { flex: 1; background: #111418; padding: 8px 12px; border-radius: 12px; }
        .comment-author { font-weight: 700; color: #f7f9f9; font-size: 13px; }
        .comment-text { color: #d9d9d9; margin-top: 2px; }
        .comment-reply-btn { font-size: 11px; color: #a855f7; cursor: pointer; margin-top: 4px; display: inline-block; }

        /* BOTTOM NAV */
        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #71767b; font-size: 20px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 2px; }
        .nav-item.active { color: #f7f9f9; }
        .nav-label { font-size: 10px; font-weight: 600; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }

        /* PROFILE TAB */
        .profile-header { position: relative; }
        .profile-banner { width: 100%; height: 130px; background: linear-gradient(135deg, #7928CA, #FF0080); }
        .profile-avatar-wrapper { position: relative; width: 90px; height: 90px; margin-top: -45px; margin-left: 16px; }
        .profile-avatar-img { width: 90px; height: 90px; border-radius: 50%; border: 4px solid #000; object-fit: cover; background: #202327; }
        .change-avatar-badge {
            position: absolute; bottom: 2px; right: 2px; background: #a855f7; color: #fff;
            width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
            cursor: pointer; border: 2px solid #000; font-size: 12px;
        }
        .profile-info { padding: 16px; border-bottom: 1px solid #16181c; }
        .profile-name { font-size: 20px; font-weight: 800; color: #fff; }
        .profile-handle { color: #71767b; font-size: 14px; margin-bottom: 8px; }
        .profile-bio { font-size: 14px; color: #e7e9ea; line-height: 1.4; margin-bottom: 12px; }
        .profile-stats { display: flex; gap: 20px; font-size: 14px; color: #71767b; }
        .profile-stats span { color: #fff; font-weight: 700; }

        /* DMS TAB */
        .dms-header { padding: 16px; border-bottom: 1px solid #16181c; font-size: 18px; font-weight: 800; }
        .member-selector { display: flex; gap: 10px; padding: 12px 16px; overflow-x: auto; border-bottom: 1px solid #16181c; scrollbar-width: none; }
        .member-pill { padding: 8px 14px; border-radius: 20px; background: #16181c; color: #71767b; font-size: 13px; font-weight: 600; cursor: pointer; white-space: nowrap; display: flex; align-items: center; gap: 6px; }
        .member-pill.active { background: #a855f7; color: #fff; }
        .chat-box { padding: 16px; display: flex; flex-direction: column; gap: 12px; height: calc(100vh - 240px); overflow-y: auto; }
        .chat-bubble { max-width: 82%; padding: 12px 16px; border-radius: 18px; font-size: 14.5px; line-height: 1.4; }
        .chat-bubble.incoming { background: #202327; color: #e7e9ea; align-self: flex-start; border-bottom-left-radius: 4px; }
        .chat-bubble.outgoing { background: #a855f7; color: #fff; align-self: flex-end; border-bottom-right-radius: 4px; }
        .chat-input-bar { position: fixed; bottom: 65px; width: 100%; max-width: 480px; background: #000; padding: 10px 16px; display: flex; gap: 10px; border-top: 1px solid #16181c; }
        .chat-input { flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 20px; padding: 10px 16px; color: #fff; outline: none; font-size: 14px; }

        /* STORY POPUP MODAL */
        .story-modal { display: none; position: fixed; inset: 0; background: rgba(0, 0, 0, 0.95); z-index: 2000; justify-content: center; align-items: center; }
        .story-modal.active { display: flex; }
        .story-card { width: 90%; max-width: 400px; height: 75vh; background: #111; border-radius: 20px; position: relative; overflow: hidden; display: flex; flex-direction: column; }
        .story-header { position: absolute; top: 12px; left: 12px; right: 12px; display: flex; align-items: center; justify-content: space-between; z-index: 10; color: white; text-shadow: 0 1px 4px rgba(0,0,0,0.8); }
        .story-user { display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 14px; }
        .story-close { font-size: 22px; cursor: pointer; color: white; }
        .story-img-main { width: 100%; height: 100%; object-fit: cover; }
        .story-footer-text { position: absolute; bottom: 20px; left: 16px; right: 16px; color: white; background: rgba(0,0,0,0.65); backdrop-filter: blur(8px); padding: 12px 16px; border-radius: 12px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- TOP HEADER -->
        <div class="top-header">
            <div class="app-logo"><i class="fa-solid fa-sparkles"></i> Status AI</div>
            <div style="color:#a855f7; font-size: 12px; font-weight: 800; background: rgba(168,85,247,0.15); padding: 4px 10px; border-radius: 12px;">
                ⚡ UNLIMITED
            </div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- STORIES BAR -->
            <div class="stories-container" id="stories-bar"></div>

            <!-- CREATE POST -->
            <div class="create-post-box">
                <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ec4899'/><text x='50%' y='55%' dominant-baseline='middle' text-anchor='middle' fill='%23ffffff' font-family='sans-serif' font-weight='bold' font-size='36'>G</text></svg>" class="user-avatar-small current-user-img">
                <div style="flex:1;">
                    <textarea class="create-post-input" id="new-post-text" placeholder="Post update as Manager @gaerwenill..."></textarea>
                    <div class="create-post-actions">
                        <span style="color:#a855f7; font-size: 16px;"><i class="fa-regular fa-image"></i> <i class="fa-solid fa-chart-simple" style="margin-left:8px;"></i></span>
                        <button class="post-btn" onclick="publishPost()">Post</button>
                    </div>
                </div>
            </div>

            <!-- FEED LIST -->
            <div class="feed" id="feed-posts"></div>
        </div>

        <!-- TAB 2: DMS -->
        <div id="tab-dms" class="tab-content">
            <div class="dms-header">Direct Messages</div>
            <div class="member-selector" id="member-selector"></div>
            <div class="chat-box" id="chat-box"></div>
            <div class="chat-input-bar">
                <input type="text" id="dm-input" class="chat-input" placeholder="Message SKZ...">
                <button class="post-btn" onclick="sendDM()">Send</button>
            </div>
        </div>

        <!-- TAB 3: PROFILE -->
        <div id="tab-profile" class="tab-content">
            <div class="profile-header">
                <div class="profile-banner"></div>
                <div class="profile-avatar-wrapper">
                    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ec4899'/><text x='50%' y='55%' dominant-baseline='middle' text-anchor='middle' fill='%23ffffff' font-family='sans-serif' font-weight='bold' font-size='36'>G</text></svg>" class="profile-avatar-img current-user-img" id="profile-avatar-display">
                    <label for="avatar-input-file" class="change-avatar-badge">
                        <i class="fa-solid fa-camera"></i>
                    </label>
                    <input type="file" id="avatar-input-file" accept="image/*" style="display:none;" onchange="uploadAvatar(event)">
                </div>
            </div>
            <div class="profile-info">
                <div class="profile-name">Gaerwenill <i class="fa-solid fa-circle-check verified-badge"></i></div>
                <div class="profile-handle">@gaerwenill</div>
                <div class="profile-bio">Head Manager of Stray Kids 🧭 | JYP Entertainment | Coordinating World Tour 2026 💖</div>
                <div class="profile-stats">
                    <div><span>8</span> Following</div>
                    <div><span>1.4M</span> Followers</div>
                    <div><span>99/100</span> Rep</div>
                </div>
            </div>
            <div style="padding: 16px; font-weight: 700; color:#71767b; font-size: 13px;">MY RECENT POSTS</div>
            <div id="my-posts-list"></div>
        </div>

        <!-- BOTTOM NAV -->
        <div class="bottom-nav">
            <div class="nav-item active" onclick="switchTab('feed', this)">
                <i class="fa-solid fa-house"></i>
                <span class="nav-label">Feed</span>
            </div>
            <div class="nav-item" onclick="switchTab('dms', this)">
                <i class="fa-solid fa-paper-plane"></i>
                <span class="nav-label">DMs</span>
            </div>
            <div class="nav-item" onclick="switchTab('profile', this)">
                <i class="fa-solid fa-user"></i>
                <span class="nav-label">Profile</span>
            </div>
        </div>
    </div>

    <!-- STORY POPUP MODAL -->
    <div class="story-modal" id="story-modal">
        <div class="story-card">
            <div class="story-header">
                <div class="story-user">
                    <img id="modal-user-img" style="width:32px; height:32px; border-radius:50%; object-fit:cover;">
                    <span id="modal-user-name"></span>
                </div>
                <span class="story-close" onclick="closeStory()">&times;</span>
            </div>
            <img id="modal-story-img" class="story-img-main">
            <div class="story-footer-text" id="modal-story-caption"></div>
        </div>
    </div>

    <script>
        // DATA & ASSETS - Embedded SVG Data URLs for 100% Guaranteed Image Render everywhere
        function svgAvatar(bg, text) {
            return `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='${bg}'/><text x='50%' y='55%' dominant-baseline='middle' text-anchor='middle' fill='%23ffffff' font-family='sans-serif' font-weight='bold' font-size='36'>${text}</text></svg>`;
        }

        function svgCard(bg, title, subtitle) {
            return `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='600' height='400' viewBox='0 0 600 400'><rect width='600' height='400' fill='${bg}'/><text x='50%' y='45%' dominant-baseline='middle' text-anchor='middle' fill='%23ffffff' font-family='sans-serif' font-weight='bold' font-size='28'>${title}</text><text x='50%' y='60%' dominant-baseline='middle' text-anchor='middle' fill='%23e2e8f0' font-family='sans-serif' font-size='18'>${subtitle}</text></svg>`;
        }

        let currentUserAvatar = svgAvatar('%23ec4899', 'G');

        const MEMBERS = [
            { id: "chan", name: "Bang Chan", handle: "@gnabnahc", avatar: svgAvatar('%233b82f6', 'BC'), storyImg: svgCard('%231e3a8a', '3RACHA Studio 🎧', 'Late night track production'), storyCap: "Late night recording session at 3RACHA studio" },
            { id: "felix", name: "Felix", handle: "@yong.lixx", avatar: svgAvatar('%23eab308', 'FL'), storyImg: svgCard('%23854d0e', 'Homemade Brownies 🍪', 'For Manager @gaerwenill'), storyCap: "Fresh batch of homemade brownies for @gaerwenill!" },
            { id: "leeknow", name: "Lee Know", handle: "@t.leeknow", avatar: svgAvatar('%2322c55e', 'LK'), storyImg: svgCard('%2314532d', 'Cats Corner 🐱', 'Sooni, Doongi & Dori'), storyCap: "Sooni, Doongi, and Dori approve this schedule" },
            { id: "hyunjin", name: "Hyunjin", handle: "@hynjinnnn", avatar: svgAvatar('%23a855f7', 'HJ'), storyImg: svgCard('%23581c87', 'Art Studio 🎨', 'New canvas painting finished'), storyCap: "Finished painting in my art room" },
            { id: "changbin", name: "Changbin", handle: "@jutdwae", avatar: svgAvatar('%23ef4444', 'CB'), storyImg: svgCard('%237f1d1d', 'Gym Session 💪', 'JUTDAE energy 100%'), storyCap: "JUTDAE energy after 3 hours gym session!" },
            { id: "han", name: "Han", handle: "@_doolsetnet", avatar: svgAvatar('%2306b6d4', 'HN'), storyImg: svgCard('%23164e63', 'Songwriting 🎵', 'Comeback demo track'), storyCap: "Writing new tracks for comeback" },
            { id: "seungmin", name: "Seungmin", handle: "@miniverse.___", avatar: svgAvatar('%236366f1', 'SM'), storyImg: svgCard('%23312e81', 'Vocal Practice 🐶', 'Warmup session done'), storyCap: "Vocal warmup completed for today" },
            { id: "in", name: "I.N", handle: "@i.2.n.8", avatar: svgAvatar('%23f97316', 'IN'), storyImg: svgCard('%237c2d12', 'Today OOTD 😎', 'Maknae style'), storyCap: "Today's OOTD check for schedule!" }
        ];

        let selectedMemberId = "chan";

        let postsData = [
            {
                id: 1, author: "Bang Chan", handle: "@gnabnahc", avatar: MEMBERS[0].avatar, verified: true, time: "15m",
                text: "Huge thanks to our Head Manager @gaerwenill for organizing the entire World Tour 2026 rehearsal schedule! STAYs get ready!",
                postImg: svgCard('%231e293b', 'STRAY KIDS WORLD TOUR 2026 🧭', 'Live Rehearsal Stage'),
                likes: 45200, liked: false,
                comments: [
                    { author: "Felix", handle: "@yong.lixx", avatar: MEMBERS[1].avatar, text: "Chanie hyung is right! Manager @gaerwenill is the best!" },
                    { author: "STAY Official", handle: "@stay_updates", avatar: svgAvatar('%23ec4899', 'ST'), text: "WE LOVE YOU MANAGER @gaerwenill!! THANK YOU FOR PROTECTING OUR BOYS!" },
                    { author: "Lee Know", handle: "@t.leeknow", avatar: MEMBERS[2].avatar, text: "Now buy us meat after practice @gaerwenill!" },
                    { author: "STAY Latam", handle: "@stay_latam", avatar: svgAvatar('%23f43f5e', 'LA'), text: "We are so ready for World Tour!!" },
                    { author: "SKZ Tokyo Fans", handle: "@skz_tokyo", avatar: svgAvatar('%238b5cf6', 'TK'), text: "See you in Tokyo Dome!!" }
                ]
            },
            {
                id: 2, author: "Felix", handle: "@yong.lixx", avatar: MEMBERS[1].avatar, verified: true, time: "42m",
                text: "Made fresh chocolate chip cookies for @gaerwenill and all 3RACHA members today! Hope everyone stays warm ✨🍪",
                postImg: svgCard('%2378350f', 'Felix Homemade Brownies 🍪', 'Fresh from oven'),
                likes: 89100, liked: false,
                comments: [
                    { author: "Hyunjin", handle: "@hynjinnnn", avatar: MEMBERS[3].avatar, text: "Save some for me and @gaerwenill!!" },
                    { author: "STAY Global", handle: "@stay_global", avatar: svgAvatar('%2310b981', 'SG'), text: "Felix is literally an angel 😭❤️" },
                    { author: "Changbin", handle: "@jutdwae", avatar: MEMBERS[4].avatar, text: "Protein cookies next Felix!!" }
                ]
            },
            {
                id: 3, author: "Dispatch Official", handle: "@kpop_dispatch", avatar: svgAvatar('%23dc2626', 'DP'), verified: true, time: "2h",
                text: "BREAKING: Stray Kids Head Manager @gaerwenill spotted arriving at JYPE Headquarters for emergency comeback meeting.",
                postImg: svgCard('%23991b1b', 'DISPATCH EXCLUSIVE 🚨', 'Manager @gaerwenill at JYP Center'),
                likes: 120400, liked: false,
                comments: [
                    { author: "SKZ Charts", handle: "@skz_chart_data", avatar: svgAvatar('%230284c7', 'CD'), text: "COMEBACK IS COMING GUYS STAY TUNED!!" },
                    { author: "JYP Official", handle: "@jyp_official_news", avatar: svgAvatar('%232563eb', 'JYP'), text: "Official statement releasing soon." }
                ]
            }
        ];

        let dmsData = {
            chan: [
                { sender: "them", text: "Hey Manager @gaerwenill! Thanks for arranging the rehearsal time. Do you have a second to check track 3 mix?" }
            ],
            felix: [
                { sender: "them", text: "Manager @gaerwenill!! Did you try the brownies I left on your desk? 🍪" }
            ],
            leeknow: [
                { sender: "them", text: "Manager @gaerwenill, Seungmin is teasing Changbin again. Come mediate please haha." }
            ],
            hyunjin: [
                { sender: "them", text: "Hi @gaerwenill! What time is our fitting tomorrow?" }
            ],
            changbin: [
                { sender: "them", text: "JUTDAE!! Ready for gym session after recording @gaerwenill!" }
            ],
            han: [
                { sender: "them", text: "I wrote 2 new verses @gaerwenill! Sending audio demo now!" }
            ],
            seungmin: [
                { sender: "them", text: "Vocal recording finished @gaerwenill. Everything went smoothly!" }
            ],
            in: [
                { sender: "them", text: "Manager @gaerwenill, can we get iced americano for everyone?" }
            ]
        };

        // RENDER FUNCTIONS
        function renderStories() {
            let html = "";
            MEMBERS.forEach((m, idx) => {
                html += `
                    <div class="story-item" onclick="openStory(${idx})">
                        <div class="story-ring">
                            <img src="${m.avatar}" class="story-avatar-img">
                        </div>
                        <span class="story-username">${m.handle}</span>
                    </div>
                `;
            });
            document.getElementById("stories-bar").innerHTML = html;
        }

        function renderFeed() {
            let html = "";
            postsData.forEach(p => {
                let commentsHtml = "";
                p.comments.forEach((c) => {
                    commentsHtml += `
                        <div class="comment-item">
                            <img src="${c.avatar}" class="comment-avatar">
                            <div class="comment-body">
                                <div class="comment-author">${c.author} <span style="color:#71767b; font-weight:normal;">${c.handle}</span></div>
                                <div class="comment-text">${c.text}</div>
                                <span class="comment-reply-btn" onclick="replyToComment(${p.id}, '${c.handle}')"><i class="fa-solid fa-reply"></i> Reply</span>
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
                                ${p.verified ? '<i class="fa-solid fa-circle-check verified-badge"></i>' : ''}
                                <span class="post-handle">${p.handle} · ${p.time}</span>
                            </div>
                            <div class="post-text">${p.text}</div>
                            ${p.postImg ? `<img src="${p.postImg}" class="post-image">` : ''}
                            <div class="post-actions">
                                <span class="action-btn" onclick="focusComment(${p.id})"><i class="fa-regular fa-comment"></i> ${p.comments.length}</span>
                                <span class="action-btn"><i class="fa-solid fa-retweet"></i> 1.2K</span>
                                <span class="action-btn ${p.liked ? 'liked' : ''}" onclick="toggleLike(${p.id})">
                                    <i class="${p.liked ? 'fa-solid' : 'fa-regular'} fa-heart"></i> ${p.likes.toLocaleString()}
                                </span>
                            </div>
                            <div class="comments-list">${commentsHtml}</div>
                        </div>
                    </div>
                `;
            });
            document.getElementById("feed-posts").innerHTML = html;
        }

        function renderMemberSelector() {
            let html = "";
            MEMBERS.forEach(m => {
                let activeClass = m.id === selectedMemberId ? 'active' : '';
                html += `
                    <div class="member-pill ${activeClass}" onclick="selectMember('${m.id}')">
                        <img src="${m.avatar}" style="width:20px; height:20px; border-radius:50%; object-fit:cover;">
                        ${m.name}
                    </div>
                `;
            });
            document.getElementById("member-selector").innerHTML = html;
            renderChat();
        }

        function renderChat() {
            let msgs = dmsData[selectedMemberId] || [];
            let html = "";
            let currentMem = MEMBERS.find(m => m.id === selectedMemberId);
            msgs.forEach(m => {
                let isOut = m.sender === "me";
                html += `
                    <div class="chat-bubble ${isOut ? 'outgoing' : 'incoming'}">
                        <strong>${isOut ? '@gaerwenill' : currentMem.name}:</strong><br>
                        ${m.text}
                    </div>
                `;
            });
            let chatBox = document.getElementById("chat-box");
            chatBox.innerHTML = html;
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        // ACTIONS
        function toggleLike(postId) {
            let post = postsData.find(p => p.id === postId);
            if (post) {
                post.liked = !post.liked;
                post.likes += post.liked ? 1 : -1;
                renderFeed();
            }
        }

        function publishPost() {
            let input = document.getElementById("new-post-text");
            let text = input.value.trim();
            if (text) {
                let newP = {
                    id: Date.now(),
                    author: "Gaerwenill",
                    handle: "@gaerwenill",
                    avatar: currentUserAvatar,
                    verified: true,
                    time: "Just now",
                    text: text,
                    likes: 1,
                    liked: true,
                    comments: [
                        { author: "Bang Chan", handle: "@gnabnahc", avatar: MEMBERS[0].avatar, text: "Got it Manager @gaerwenill! We will follow this schedule!" },
                        { author: "Felix", handle: "@yong.lixx", avatar: MEMBERS[1].avatar, text: "Thank you @gaerwenill!!" }
                    ]
                };
                postsData.unshift(newP);
                input.value = "";
                renderFeed();
                renderMyPosts();
            }
        }

        function replyToComment(postId, handle) {
            let post = postsData.find(p => p.id === postId);
            if (post) {
                let replyText = prompt(`Reply to ${handle} as @gaerwenill:`);
                if (replyText) {
                    post.comments.push({
                        author: "Gaerwenill",
                        handle: "@gaerwenill",
                        avatar: currentUserAvatar,
                        text: replyText
                    });
                    renderFeed();
                }
            }
        }

        function focusComment(postId) {
            replyToComment(postId, "this post");
        }

        function selectMember(id) {
            selectedMemberId = id;
            renderMemberSelector();
        }

        function sendDM() {
            let input = document.getElementById("dm-input");
            let text = input.value.trim();
            if (text) {
                if (!dmsData[selectedMemberId]) dmsData[selectedMemberId] = [];
                dmsData[selectedMemberId].push({ sender: "me", text: text });
                input.value = "";
                renderChat();

                setTimeout(() => {
                    let mem = MEMBERS.find(m => m.id === selectedMemberId);
                    let replies = [
                        `Thank you Manager @gaerwenill! Really appreciate your help as always.`,
                        `Got your message @gaerwenill! I will tell the rest of the members right away.`,
                        `Sounds great @gaerwenill! See you at JYPE building in a bit!`
                    ];
                    let randomReply = replies[Math.floor(Math.random() * replies.length)];
                    dmsData[selectedMemberId].push({ sender: "them", text: randomReply });
                    renderChat();
                }, 1000);
            }
        }

        function uploadAvatar(event) {
            let file = event.target.files[0];
            if (file) {
                let reader = new FileReader();
                reader.onload = function(e) {
                    currentUserAvatar = e.target.result;
                    document.querySelectorAll(".current-user-img").forEach(img => {
                        img.src = currentUserAvatar;
                    });
                    postsData.forEach(p => {
                        if (p.handle === "@gaerwenill") p.avatar = currentUserAvatar;
                        p.comments.forEach(c => {
                            if (c.handle === "@gaerwenill") c.avatar = currentUserAvatar;
                        });
                    });
                    renderFeed();
                    renderMyPosts();
                };
                reader.readAsDataURL(file);
            }
        }

        function openStory(idx) {
            let mem = MEMBERS[idx];
            document.getElementById("modal-user-img").src = mem.avatar;
            document.getElementById("modal-user-name").innerText = mem.name + " (" + mem.handle + ")";
            document.getElementById("modal-story-img").src = mem.storyImg;
            document.getElementById("modal-story-caption").innerText = mem.storyCap;
            document.getElementById("story-modal").classList.add("active");
        }

        function closeStory() {
            document.getElementById("story-modal").classList.remove("active");
        }

        function switchTab(tabName, el) {
            document.querySelectorAll(".tab-content").forEach(t => t.classList.remove("active"));
            document.querySelectorAll(".nav-item").forEach(n => n.classList.remove("active"));
            document.getElementById("tab-" + tabName).classList.add("active");
            el.classList.add("active");
        }

        function renderMyPosts() {
            let myPosts = postsData.filter(p => p.handle === "@gaerwenill");
            let html = "";
            myPosts.forEach(p => {
                html += `
                    <div style="padding:12px 16px; border-bottom:1px solid #16181c;">
                        <div style="font-weight:700;">${p.text}</div>
                        <div style="color:#71767b; font-size:12px; margin-top:4px;">${p.time} · ❤️ ${p.likes}</div>
                    </div>
                `;
            });
            document.getElementById("my-posts-list").innerHTML = html;
        }

        // INIT
        renderStories();
        renderFeed();
        renderMemberSelector();
        renderMyPosts();
    </script>
</body>
</html>
"""

components.html(html_code, height=920, scrolling=True)
